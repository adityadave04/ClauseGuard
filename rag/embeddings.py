from sentence_transformers import SentenceTransformer
import os

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

class EmbeddingModel:

    _model = None

    def __init__(self):

        if EmbeddingModel._model is None:
            EmbeddingModel._model = SentenceTransformer(
                "BAAI/bge-small-en-v1.5"
            )

        self.model = EmbeddingModel._model

    def embed_text(self, text: str):
        return self.model.encode(
            text,
            normalize_embeddings=True
        ).tolist()

    def embed_batch(self, texts: list[str]):
        return self.model.encode(
            texts,
            normalize_embeddings=True
        ).tolist()