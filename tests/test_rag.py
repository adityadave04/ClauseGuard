"""
Tests for the RAG pipeline (chunking, retrieval, reranking).

TODO (RAG commits):
- test_chunker_splits_on_section_boundaries(): verify chunks align with
  N.N headings and each chunk carries section_number/section_title/page
- test_chunker_keeps_subclauses_together(): 5.4 should be ONE chunk
  containing 5.4.1-5.4.4, not four separate chunks
- test_retrieval_returns_relevant_chunk(): query "what is the liability
  cap?" should surface the chunk for Section 5.4 in the top results
- test_reranker_improves_ordering(): a deliberately noisy candidate set
  should end up correctly ordered after reranking
"""
