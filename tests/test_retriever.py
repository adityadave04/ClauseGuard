from rag.retriever import Retriever


def test_retriever():

    retriever = Retriever()

    results = retriever.retrieve(
        "termination for convenience"
    )

    assert len(results) > 0

    print()

    for chunk in results[:5]:

        print(
            chunk["score"],
            chunk["section_number"],
            chunk["section_title"]
        )