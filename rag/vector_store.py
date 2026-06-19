"""
Qdrant Cloud client wrapper — collection setup and chunk upsert.

TODO (RAG ingestion commit):
- Connect using settings.qdrant_url / settings.qdrant_api_key
- create_collection(): create settings.qdrant_collection_name with the
  correct vector size for settings.embedding_model_name (384 for
  all-MiniLM-L6-v2), idempotent — skip if it already exists
- upsert_chunks(chunks): embed each chunk's text via rag/embeddings.py and
  upsert as Qdrant points, storing section_number/section_title/page_number
  as point payload (this is what makes citations possible later)
"""
