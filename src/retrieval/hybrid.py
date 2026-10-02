import weaviate
from sentence_transformers import SentenceTransformer

class TFTHybridRetriever:
    def __init__(self, top_k: int = 6, alpha: float = 0.5):
        self.client = weaviate.connect_to_local()
        self.collection = self.client.collections.get("TFTPatchNotes")
        self.embed_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.top_k = top_k
        self.alpha = alpha # 0.0 = pure BM25, 1.0 = pure vector, 0.5 = 

    def retrieve(self, query: str):
        query_vector = self.embed_model.encode(query).tolist()

        # Native Hybrid Search (BM25 + Dense Vector)
        response = self.collection.query.hybrid(
            query=query,
            vector=query_vector,
            alpha=self.alpha,
            limit=self.top_k
        )

        return [
            {"text": obj.properties["text"], "source": obj.properties["source"]}
            for obj in response.objects
        ]

    def close(self):
        self.client.close()

if __name__ == "__main__":
    retriever = TFTHybridRetriever(top_k=3)
    try:
        results = retriever.retrieve("Ashe damage bugfix")
        print(f"Retrieved {len(results)} chunks using Hybrid Search.")
        for r in results:
            print("-", r["text"][:120].strip(), "...")
    finally:
        retriever.close()