# ClauseGuard

ClauseGuard is an AI-powered Contract Intelligence Assistant built using FastAPI, Streamlit, LangGraph, Qdrant, and LLMs.

It provides three core capabilities:

* Ask Anything about a contract
* Risk Analysis
* Key Data Extraction

---

# Features

## Ask Anything

Query contracts in natural language.

Examples:

* Can either party terminate for convenience?
* What are the payment terms?
* What obligations survive termination?
* Which law governs the agreement?

---

## Risk Scanner

Automatically identifies:

* Liability risks
* Indemnity risks
* Termination risks
* Confidentiality risks

Provides:

* Severity
* Issue
* Recommendation

---

## Key Data Extract

Extracts important information such as:

* Agreement number
* Service provider
* Client
* Governing law
* Payment terms
* Notice period
* Termination fee
* Uptime SLA

---

# Architecture

```text
Streamlit UI
     ↓
FastAPI
     ↓
LangGraph Agent
     ↓
Tools
     ↓
Retriever
     ↓
Reranker
     ↓
Qdrant Vector Store
     ↓
Embeddings
```

---

# Tech Stack

* Python 3.12
* FastAPI
* Streamlit
* LangGraph
* LiteLLM
* Qdrant
* Sentence Transformers
* Cross Encoder
* PyMuPDF
* Pytesseract OCR
* pdf2image
* HuggingFace

---

# Project Structure

```text
ClauseGuard

agent/
api/
config/
data/
llm/
models/
prompts/
rag/
tests/
ui/

README.md
requirements.txt
Dockerfile
```

---

# Installation

Create virtual environment:

```bash
python -m venv .venv312
```

Activate:

Windows

```bash
.venv312\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROK_API_KEY=your_key

QDRANT_URL=your_url
QDRANT_API_KEY=your_key

QDRANT_COLLECTION=contracts
```

---

# Running FastAPI

Terminal 1:

```bash
uvicorn api.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Health endpoint:

```text
http://127.0.0.1:8000/health
```

---

# Running Streamlit

Terminal 2:

```bash
streamlit run ui/app.py
```

UI:

```text
http://localhost:8501
```

---

# Core Capabilities

## Ask Anything

Uses:

* Semantic Retrieval
* Cross Encoder Reranking
* LLM-based Answer Generation

---

## Risk Analysis

Identifies:

* HIGH risks
* MEDIUM risks
* LOW risks

and provides recommendations.

---

## Metadata Extraction

Extracts structured contract information in JSON format.

---

# OCR Support

If a PDF contains no text layer:

* PyMuPDF extraction is attempted first.
* OCR fallback using Tesseract and pdf2image is used automatically.

---

# Future Improvements

* Chat history
* Report generation
* Deployment
* Authentication
* Multi-document support
* Batch processing

---

# Example Questions

* Can either party terminate for convenience?
* What obligations survive termination?
* What is the limitation of liability?
* Which law governs the agreement?
* What are the payment terms?

---

# License

MIT License
