import os
import yaml
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.retrieval.hybrid import TFTHybridRetriever
from src.retrieval.reranker import TFTReRanker

load_dotenv()

def load_prompt_config(path: str = "configs/prompts/v2_generation.yaml") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

class TFTRAGPipeline:
    def __init__(self, prompt_config_path: str = "configs/prompts/v2_generation.yaml"):
        # self.retriever = TFTDenseRetriever(top_k=3)
        self.retriever = TFTHybridRetriever(top_k=6, alpha=0.5)
        self.reranker = TFTReRanker()

        # Load external prompt
        prompt_data = load_prompt_config(prompt_config_path)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", prompt_data["system_template"]),
            ("user", prompt_data["user_template"])
        ])

        # Gemini 3.5 Flash for generation
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.5-flash",
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0.1
        )
        self.output_parser = StrOutputParser()

    def _format_docs(self, docs: list) -> str:
        # formats with chunks identifiers
        formatted = []
        for i, doc in enumerate(docs, start=1):
            score = doc.get("score", 0.0)
            formatted.append(f"[Source: {doc['source']} - Chunk {i} | ReRank Score: {score:.3f}]\n{doc['text']}\n")
        return "\n---\n".join(formatted)

    def run(self, query: str):

        # Hybrid Retrieval (BM25 + Dense)
        initial_chunks = self.retriever.retrieve(query)

        # Cross-Encoder Reranking
        ranked_chunks = self.reranker.rerank(query, initial_chunks, top_n=3)

        # Format Context
        formatted_chunks = self._format_docs(ranked_chunks)

        # Construct LCEL runnable chain
        chain = self.prompt | self.llm | self.output_parser

        # Generate answer
        answer = chain.invoke({
            "context": formatted_chunks,
            "question": query
        })

        return {
            "query": query,
            "answer": answer,
            "context_chunks": ranked_chunks
        }

    def close(self):
        return self.retriever.close()

if __name__ == "__main__":
    pipeline = TFTRAGPipeline()
    try:
        # Test 1: Grounded question
        print("=== TEST 1: Supported Query ===")
        res1 = pipeline.run("What balance changes were made to Ashe?")
        print(res1["answer"])

        # Test 2: Unanswerable query (Testing Refusal Guardrail)
        print("\n=== TEST 2: Unsupported Query (Refusal Test) ===")
        res2 = pipeline.run("What are the patch changes for League of Legends Summoner's Rift Baron Nashor?")
        print(res2["answer"])
    finally:
        pipeline.close()