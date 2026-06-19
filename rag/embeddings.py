"""
Embedding generation via sentence-transformers.

Runs locally in-process (model loaded from EMBEDDING_MODEL_NAME in config) —
no external API call, no API key, no separate service to host or manage.

TODO (RAG ingestion commit):
- Load the SentenceTransformer model once (module-level, not per-call) using
  settings.embedding_model_name
- embed_texts(texts: list[str]) -> list[list[float]], used by both:
    - ingestion (rag/vector_store.py, embedding chunks before upsert)
    - query time (rag/retriever.py, embedding the incoming question)
"""
