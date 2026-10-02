from sentence_transformers import CrossEncoder

class TFTReRanker:
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.model = CrossEncoder(model_name)

    def rerank(self, query: str, chunks: list[dict], top_n: int = 3) -> list[dict]:
        if not chunks:
            return []

        pairs = [[query, chunk["text"]] for chunk in chunks]
        scores = self.model.predict(pairs)

        for i, score in enumerate(scores):
            chunks[i]["score"] = float(score)

        ranked_chunks = sorted(chunks, key=lambda x: x["score"], reverse=True)
        return ranked_chunks[:top_n]

