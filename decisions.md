# Architectural Decisions

This document captures some of the design decisions made while building ClauseGuard.

---

# 1. Retrieval-Augmented Generation (RAG)

## Decision

Use a RAG pipeline instead of passing the entire contract directly to the LLM.

## Reason

Contracts can be long and exceed the effective context window of smaller models.

Retrieving only the relevant sections:

* reduces token usage,
* improves answer quality,
* and makes section citations possible.

---

# 2. Vector Database

## Decision

Use Qdrant as the vector store.

## Reason

Qdrant provides:

* efficient semantic search,
* good Python support,
* cloud-hosted deployments,
* and simple APIs.

---

# 3. Embedding Model

## Decision

Use:

BAAI/bge-small-en-v1.5

## Reason

The model is lightweight and provides good semantic retrieval performance while still being practical for local development.

---

# 4. Cross Encoder Reranking

## Decision

Use:

cross-encoder/ms-marco-MiniLM-L-6-v2

## Reason

Initial vector retrieval may return loosely related chunks.

Reranking improves relevance and reduces hallucinations by selecting the most useful sections before sending context to the LLM.

---

# 5. OCR Strategy

## Decision

Attempt text extraction with PyMuPDF first and use OCR only when required.

OCR stack:

* Tesseract
* pdf2image
* Poppler

## Reason

Most PDFs already contain a text layer.

Using OCR only as a fallback keeps processing faster while still supporting scanned documents.

---

# 6. Agent Framework

## Decision

Use LangGraph.

## Reason

The graph-based approach makes it easy to route requests between different tools and leaves room for future expansion.

Current tools:

* Ask Anything
* Risk Scanner
* Metadata Extractor

---

# 7. API Layer

## Decision

Use FastAPI.

## Reason

FastAPI provides:

* simple REST endpoints,
* automatic validation,
* and easy integration with Streamlit.

---

# 8. UI

## Decision

Use Streamlit.

## Reason

The focus of the project is on backend intelligence rather than frontend development.

Streamlit allows rapid prototyping with minimal overhead.

---

# 9. LLM Abstraction

## Decision

Use LiteLLM.

## Reason

LiteLLM makes it easy to switch providers without changing application logic.

Current model:

xai/grok-3-mini

Possible alternatives:

* GPT-4o
* Claude
* Gemini

The model name itself is stored in configuration.

---

# 10. Configuration Management

## Decision

Store external configuration in environment variables.

## Reason

Secrets and machine-specific values should not be hardcoded.

Environment variables include:

* GROK_API_KEY
* LLM_MODEL
* QDRANT_URL
* QDRANT_API_KEY
* QDRANT_COLLECTION
* TESSERACT_PATH
* POPPLER_PATH
* LOG_LEVEL

This keeps code portable across environments.

---

# 11. Contract Input

## Decision

Accept contracts through the Streamlit UI instead of using a fixed file path.

## Reason

Contracts are runtime inputs, not configuration.

Allowing file upload makes the application reusable without changing source code whenever a new agreement needs to be analyzed.

---

# 12. OCR Dependencies

## Decision

Keep Tesseract and Poppler paths outside the code.

## Reason

Installation paths vary across machines and operating systems.

Tesseract performs OCR on scanned images, while Poppler converts PDF pages into images before OCR.

Keeping these paths in environment variables avoids machine-specific hardcoding.

---

# 13. Structured Outputs

## Decision

Return JSON from the Risk Scanner and Metadata Extractor.

## Reason

Structured outputs are easier to:

* display in the UI,
* download,
* and integrate with future reporting workflows.

---

# Future Improvements

Potential improvements include:

* chat history,
* PDF report generation,
* authentication,
* multi-document support,
* evaluation framework,
* deployment,
* and multi-agent workflows.
