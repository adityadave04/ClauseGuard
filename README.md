# ClauseGuard

ClauseGuard is a contract intelligence assistant built to explore how RAG pipelines and agent frameworks can be used for practical legal-document analysis.

It provides three capabilities:

* Ask questions about a contract
* Perform a risk scan
* Extract important contract metadata

---

# Features

## Uploading Contracts

Contracts are uploaded through the Streamlit interface.

The uploaded PDF is processed and indexed automatically. No source-code changes or configuration updates are required to analyze a different agreement.

For scanned documents, OCR support is available through Tesseract and Poppler.

---

## Ask Anything

Query the contract in natural language.

Examples:

* Can either party terminate for convenience?
* What are the payment terms?
* What obligations survive termination?
* Which law governs the agreement?

Responses include section references from the contract.

---

## Risk Scan

Identifies potentially important clauses and highlights risks.

The output contains:

* Severity
* Section number
* Issue
* Recommendation

---

## Metadata Extraction

Extracts structured information such as:

* Agreement number
* Service provider
* Client
* Governing law
* Payment terms
* Notice period
* Termination fee
* SLA percentage

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
* Tesseract OCR
* pdf2image

---

# Project Structure

ClauseGuard/

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
decisions.md
requirements.txt
Dockerfile

---

# Setup

Create a virtual environment:

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

Create a `.env` file based on `.env.example`.

## LLM

```env
GROK_API_KEY=your_grok_api_key
LLM_MODEL=xai/grok-3-mini
```

Keeping the model name configurable makes it easy to switch providers without changing code.

---

## Vector Database

```env
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_COLLECTION=contracts
```

---

## OCR

```env
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
POPPLER_PATH=C:\path\to\poppler\Library\bin
```

These are required only for scanned PDFs.

PyMuPDF is used first. OCR is used only if no text layer is found.

---

# Running FastAPI

Start the API:

```bash
uvicorn api.main:app --reload
```

Health endpoint:

```text
http://127.0.0.1:8000/health
```

---

# Running Streamlit

Start the UI:

```bash
streamlit run ui/app.py
```

UI:

```text
http://localhost:8501
```

---

# Tests

Run all tests:

```bash
pytest -s
```

Current status:

9 tests passing.

---

# Architecture

Streamlit UI

↓

FastAPI

↓

LangGraph

↓

Tools

↓

Retriever

↓

Cross Encoder Reranker

↓

Qdrant

↓

Embeddings

---

# Future Improvements

* PDF upload support
* Chat history
* Report generation
* Multi-document support
* Authentication
* Deployment
* Evaluation framework

---

# License

MIT License
