import json
import os
import sys
import types
import asyncio
from dotenv import load_dotenv

# --- RAGAS BUG WORKAROUND ---
dummy_chat = types.ModuleType("langchain_community.chat_models.vertexai")
dummy_chat.ChatVertexAI = type("ChatVertexAI", (object,), {})
sys.modules["langchain_community.chat_models.vertexai"] = dummy_chat
# -----------------------------------------

from ragas.metrics.collections import Faithfulness
from ragas.llms import llm_factory
from openai import AsyncOpenAI
from src.pipeline.chain import TFTRAGPipeline

load_dotenv()

async def run_evaluation():
    dataset_path = "data/eval/golden_dataset.json"
    with open(dataset_path, "r", encoding="utf-8") as f:
        qa_pairs = json.load(f)

    pipeline = TFTRAGPipeline()
    
    # Set up the LLM Judge using the native AsyncOpenAI client routed to Google
    gemini_async_client = AsyncOpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        max_retries=5  # FIXED: Automatically retry on 503 errors using exponential backoff
    )
    
    ragas_llm = llm_factory("gemini-3.5-flash", provider="openai", client=gemini_async_client)
    
    # Instantiate the modern metric
    scorer = Faithfulness(llm=ragas_llm)
    
    print(f"Generating pipeline responses and evaluating {len(qa_pairs)} questions...")
    total_score = 0.0
    
    for i, pair in enumerate(qa_pairs, start=1):
        query = pair["question"]
        
        result = pipeline.run(query)
        answer = result["answer"]
        contexts = [chunk["text"] for chunk in result["context_chunks"]]
        
        score_result = await scorer.ascore(
            user_input=query,
            response=answer,
            retrieved_contexts=contexts
        )
        
        score_value = score_result.value if hasattr(score_result, "value") else float(score_result)
        total_score += score_value
        print(f"Question {i} | Faithfulness: {score_value:.2f}")

        # RATE LIMIT PROTECTOR: Pause before evaluating the next question
        if i < len(qa_pairs):
            print("Sleeping for 5 seconds to respect free-tier rate limits...")
            await asyncio.sleep(5)
        
    pipeline.close()
    
    avg_score = total_score / len(qa_pairs) if qa_pairs else 0.0
    
    print("\n=== EVALUATION RESULTS ===")
    print(f"Average Faithfulness Score: {avg_score:.2f}")
    
    if avg_score < 0.8:
        print(f"\nBUILD FAILED: Faithfulness score {avg_score:.2f} is below the 0.8 threshold.")
        sys.exit(1)
    else:
        print(f"\nBUILD PASSED: Faithfulness score {avg_score:.2f} meets production standards.")
        sys.exit(0)

if __name__ == "__main__":
    asyncio.run(run_evaluation())