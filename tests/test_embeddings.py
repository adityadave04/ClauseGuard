from rag.embeddings import EmbeddingModel


def test_embeddings():

    model = EmbeddingModel()

    vec = model.embed_text(
        "Termination for convenience"
    )

    print(len(vec))

    assert len(vec) > 0
    