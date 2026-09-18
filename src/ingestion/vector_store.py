import weaviate
import weaviate.classes as wvc
from sentence_transformers import SentenceTransformer
from src.ingestion.chunker import TFTChunker

class TFTVectorStore:
    def __init__(self):
        # Connect to local docker container
        self.client = weaviate.connect_to_local()
        self.collection_name = "TFTPatchNotes"

        self.embed_model = SentenceTransformer("all-MiniLM-L6-v2")

    def setup_schema(self):
        if self.client.collections.exists(self.collection_name):
            return self.client.collections.get(self.collection_name)

        print(f"Creating Weaviate Collection: {self.collection_name}")
        collection = self.client.collections.create(
            name=self.collection_name,
            vectorizer_config=wvc.config.Configure.Vectorizer.none(),
            properties=[
                wvc.config.Property(name="text", data_type=wvc.config.DataType.TEXT),
                wvc.config.Property(name="souce", data_type=wvc.config.DataType.TEXT),
            ]
        )

        return collection

    def ingest_chunks(self, chunks: list):
        collection = self.setup_schema()

        texts = [chunk["text"] for chunk in chunks]
        print(f"Generating embeddings for {len(texts)} chunks")
        embeddings = self.embed_model.encode(texts, show_progress_bar=True).tolist()

        with collection.batch.dynamic() as batch:
            for chunk, vector in zip(chunks, embeddings):
                batch.add_object(
                    properties={
                        "text": chunk["text"],
                        "source": chunk["source"]
                    },
                    vector=vector
                )

        if len(collection.batch.failed_objects) > 0:
            print(f"Failed to import {len(collection.batch.failed_objects)} objects.")
        else:
            print(f"Successfully indexed {len(chunks)} chunks in Weaviate!")
    def close(self):
        self.client.close()

if __name__ == "__main__":
    chunker = TFTChunker()
    chunks = chunker.chunk_file("latest_patch.md")

    store = TFTVectorStore()
    try:
        store.ingest_chunks(chunks)
    finally:
        store.close()