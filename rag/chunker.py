"""
Semantic clause-based chunking for the contract PDF.

TODO (RAG ingestion commit):
- Extract text from data/contract.pdf using pdfplumber, preserving page
  numbers per block of text
- Split on the document's natural structure: top-level `SECTION N — TITLE`
  headers and `N.N Title` subsection headers (NOT naive character/token
  splitting — see decisions.md, Section 1, for the full justification)
- Each chunk = one N.N subsection, e.g. "5.4 Limitation of Liability"
  becomes a single chunk containing all of 5.4.1 through 5.4.4. This
  matters because 5.4.3 ("Exceptions") only makes sense attached to 5.4.1
  and 5.4.2 — splitting at the N.N.N level would separate an exception
  clause from the rule it modifies and break citation accuracy.
- Attach metadata to every chunk: section_number, section_title, page_number
- Serialize the two tables (Schedule C SLA credit tiers, Schedule D fee
  breakdown) as their own chunks, row-by-row as text, since tabular data
  doesn't fit the N.N heading pattern
- Output: list[Chunk] where Chunk = {text, section_number, section_title,
  page_number} — consumed by rag/embeddings.py and rag/vector_store.py
"""
