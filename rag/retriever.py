from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.embedder = EmbeddingModel()
        self.store = VectorStore()

    def retrieve(
        self,
        query: str,
        top_k: int = 10
    ):

        query_vector = self.embedder.embed_text(query)

        results = self.store.search(
            query_vector=query_vector,
            top_k=top_k
        )

        chunks = []

        for result in results:

            chunks.append(
                {
                    "text": result.payload["text"],
                    "section_number": result.payload["section_number"],
                    "section_title": result.payload["section_title"],
                    "page_number": result.payload["page_number"],
                    "score": result.score
                }
            )

        return chunks