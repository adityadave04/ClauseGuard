"""
Query-time retrieval from Qdrant.

TODO (RAG retrieval + reranking commit):
- embed the incoming question via rag/embeddings.py
- query Qdrant for top settings.retrieval_top_k candidate chunks
- return chunks with their text, metadata (section/page), and similarity
  score, ready to be passed into rag/reranker.py
"""
