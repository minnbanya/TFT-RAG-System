import weaviate
from sentence_transformers import SentenceTransformer

class TFTDenseRetriever:
    def __init__(self, top_k: int = 3):
        self.client = weaviate.connect_to_local()
        self.collection_name = "TFTPatchNotes"

        self.embed_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.top_k = top_k
    
    def retrieve(self, query: str):
        collection = self.client.collections.get(self.collection_name)

        print(f"Embedding query: {query}")
        # Embedding query
        query_vector = self.embed_model.encode(query).tolist()

        # Near-vector dense search
        response = collection.query.near_vector(
            near_vector=query_vector,
            limit=self.top_k
        )

        # Result text and source
        results = []
        for obj in response.objects:
            results.append({
                "text": obj.properties["text"],
                "source": obj.properties["source"],
            })

        return results

    def close(self):
        self.client.close()

if __name__ == "__main__":
    retriever = TFTDenseRetriever(top_k=3)
    try:
        test_query = "What are the changes made to Draven?"
        chunks = retriever.retrieve(test_query)

        print(f"\nTop {len(chunks)} retrieved chunks:\n")
        for i, chunk in enumerate(chunks):
            print(f"--- Chunk {i+1} | Source: {chunk['source']} ---")
            # Print the first 250 characters of the retrieved chunk
            print(chunk["text"][:250] + "...\n")
    finally:
        retriever.close()

