"""
Cross-encoder reranking step — satisfies the "at least one reranking step
after initial retrieval" requirement.

TODO (RAG retrieval + reranking commit):
- Load CrossEncoder(settings.reranker_model_name) once, module-level
- rerank(question: str, candidates: list[Chunk]) -> list[Chunk]:
    score every (question, chunk.text) pair, sort descending, return the
    top settings.rerank_top_n chunks
- This runs locally in-process, same as the embedding model — no extra
  hosted service needed
"""
