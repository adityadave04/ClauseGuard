from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from config.settings import settings

from models.chunk import Chunk


class VectorStore:

    def __init__(self):

        self.client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )

    def create_collection(self):

        collections = [
            c.name
            for c in self.client.get_collections().collections
        ]

        if settings.QDRANT_COLLECTION not in collections:

            self.client.create_collection(
                collection_name=settings.QDRANT_COLLECTION,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

    def upsert_chunks(
            self,
            chunks: list[Chunk],
            vectors: list[list[float]]
    ):

        points = []

        for chunk, vector in zip(chunks, vectors):

            points.append(
                PointStruct(
                    id=chunk.id,
                    vector=vector,
                    payload={
                        "text": chunk.text,
                        "section_number": chunk.section_number,
                        "section_title": chunk.section_title,
                        "page_number": chunk.page_number
                    }
                )
            )

        self.client.upsert(
            collection_name=settings.QDRANT_COLLECTION,
            points=points
        )

    def search(
            self,
            query_vector: list[float],
            top_k: int = 10
    ):

        results = self.client.query_points(
            collection_name=settings.QDRANT_COLLECTION,
            query=query_vector,
            limit=top_k
        )

        return results.points