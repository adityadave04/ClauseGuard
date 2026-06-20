from rag.retriever import Retriever
from rag.reranker import Reranker


def test_reranker():

    retriever = Retriever()

    chunks = retriever.retrieve(
        "termination for convenience"
    )

    reranker = Reranker()

    ranked = reranker.rerank(
        "termination for convenience",
        chunks
    )

    print()

    for chunk in ranked:

        print(
            chunk["rerank_score"],
            chunk["section_number"],
            chunk["section_title"]
        )

    assert len(ranked) > 0