# Architectural Decisions

This document records key design decisions made during the development of ClauseGuard.

---

# 1. Retrieval-Augmented Generation (RAG)

## Decision

Use a RAG architecture instead of passing the entire contract directly to the LLM.

## Reason

* Reduces context size.
* Improves response quality.
* Enables citation of relevant sections.
* Scales to larger contracts.

---

# 2. Vector Database

## Decision

Use Qdrant.

## Reason

* Simple API.
* Managed cloud offering available.
* Efficient similarity search.
* Good Python support.

---

# 3. Embedding Model

## Decision

Use sentence-transformers.

Model:

all-MiniLM-L6-v2

## Reason

* Lightweight.
* Fast inference.
* Good semantic search quality.
* Suitable for local execution.

---

# 4. Cross Encoder Reranker

## Decision

Use:

cross-encoder/ms-marco-MiniLM-L-6-v2

## Reason

* Improves retrieval accuracy.
* Better relevance ranking.
* Reduces hallucinations.

---

# 5. OCR Strategy

## Decision

Use PyMuPDF first and OCR only when necessary.

OCR stack:

* pdf2image
* pytesseract

## Reason

* Faster when PDFs already contain text.
* OCR fallback supports scanned documents.

---

# 6. Agent Framework

## Decision

Use LangGraph.

## Reason

* Clear graph-based workflow.
* Easy routing between tools.
* Supports future expansion.

---

# 7. Tool-Based Architecture

## Decision

Create separate tools:

* Ask Tool
* Risk Scanner
* Metadata Extractor

## Reason

* Separation of concerns.
* Easier testing.
* Easier future extension.

---

# 8. API Framework

## Decision

Use FastAPI.

## Reason

* Fast development.
* Automatic documentation.
* Simple REST endpoints.

Endpoints:

* /ask
* /risk
* /extract

---

# 9. UI Framework

## Decision

Use Streamlit.

## Reason

* Rapid prototyping.
* Minimal frontend code.
* Easy integration with APIs.

---

# 10. LLM Layer

## Decision

Use LiteLLM.

## Reason

* Provider abstraction.
* Easy model switching.
* Supports multiple vendors.

Current model:

grok-3-mini

Future models:

* GPT-4o
* Claude
* Gemini

---

# 11. Session State

## Decision

Use Streamlit session state.

## Reason

* Preserve responses.
* Support clear functionality.
* Improve user experience.

---

# 12. Risk Analysis

## Decision

Use LLM-generated structured JSON.

## Reason

* Easy UI rendering.
* Structured outputs.
* Supports future reporting.

Fields:

* severity
* section_number
* title
* issue
* recommendation

---

# 13. Metadata Extraction

## Decision

Extract key information into JSON.

## Reason

Provides structured contract information:

* agreement_number
* service_provider
* client
* governing_law
* payment_terms_days
* notice_period_days
* termination_fee_percent
* uptime_sla_percent

---

# 14. Docker

## Decision

Provide Docker support but defer container deployment.

## Reason

* Current local environment sufficient.
* Disk space limitations.
* Docker can be added later without changing application logic.

---

# Future Improvements

* Multi-document support.
* Authentication.
* Report generation.
* Chat history.
* PDF export.
* Deployment.
* Batch processing.
* Multi-agent workflows.
* Evaluation framework.
