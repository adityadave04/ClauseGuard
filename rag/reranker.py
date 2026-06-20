from sentence_transformers import CrossEncoder


class Reranker:

    _model = None

    def __init__(self):

        if Reranker._model is None:
            Reranker._model = CrossEncoder(
                "cross-encoder/ms-marco-MiniLM-L-6-v2"
            )

        self.model = Reranker._model

    def rerank(
        self,
        query: str,
        chunks: list[dict],
        top_k: int = 4
    ):

        pairs = [
            (query, chunk["text"])
            for chunk in chunks
        ]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(chunks, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            {
                **chunk,
                "rerank_score": float(score)
            }
            for chunk, score in ranked[:top_k]
        ]