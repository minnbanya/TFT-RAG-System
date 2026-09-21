import os
import yaml
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from src.retrieval.top_k import TFTDenseRetriever

load_dotenv()

def load_prompt_config(path: str = "configs/prompts/v1_generation.yaml") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

class TFTRAGPipeline:
    def __init__(self, prompt_config_path: str = "configs/prompts/v1_generation.yaml"):
        self.retriever = TFTDenseRetriever(top_k=3)

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
            source_tag = f"[Source: {doc['source']} - Chunk {i}]"
            formatted.append(f"{source_tag}\n{doc['text']}\n")
        return "\n---\n".join(formatted)

    def run(self, query: str):
        # Retrieve top-k chunks
        retrieved_chunks = self.retriever.retrieve(query)
        formatted_chunks = self._format_docs(retrieved_chunks)

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
            "retrieved_chunks": retrieved_chunks
        }

    def close(self):
        return self.retriever.close()

if __name__ == "__main__":
    pipeline = TFTRAGPipeline()
    try:
        query = "What balance changes were made to Ashe in this patch?"
        result = pipeline.run(query)
        
        print("\n=== USER QUESTION ===")
        print(result["query"])
        print("\n=== GENERATED RESPONSE (WITH CITATIONS) ===")
        print(result["answer"])
    finally:
        pipeline.close()