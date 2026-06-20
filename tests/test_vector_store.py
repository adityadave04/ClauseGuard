from rag.chunker import ContractChunker
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


def test_vector_store():

    chunker = ContractChunker(
        r"C:\Users\adity\Downloads\Sample_contract_doc.pdf"
    )

    chunks = chunker.create_chunks()

    embedder = EmbeddingModel()

    vectors = embedder.embed_batch(
        [chunk.text for chunk in chunks]
    )

    store = VectorStore()

    store.create_collection()

    store.upsert_chunks(
        chunks,
        vectors
    )

    query_vector = embedder.embed_text(
        "termination for convenience"
    )

    results = store.search(
        query_vector
    )

    assert len(results) > 0

    print()

    for result in results[:3]:

        print(
            result.payload["section_number"],
            result.payload["section_title"]
        )