# ClauseGuard — Contract Intelligence Agent

> Status: scaffolding complete (Commit 1). Core agent/RAG logic lands in
> subsequent commits — this README fills in as each piece is built.

A single AI agent (LangGraph) with three tools that make one contract
document instantly queryable, risk-scannable, and data-extractable:

1. **Ask Anything** — natural language Q&A over the contract, every answer
   includes a citation (section number + short quote)
2. **Risk Scan** — agent autonomously flags clauses matching a risk-keyword
   taxonomy, returns structured JSON
3. **Key Data Extract** — pulls a fixed JSON schema of contract terms
   (parties, value, term, governing law, liability cap, etc.)

All three tools run through one shared LangGraph agent instance.

## Tech stack

| Layer | Choice | Why |
|---|---|---|
| Backend | FastAPI | typed request/response models, fast to demo |
| UI | Streamlit | fastest path to a working 3-tool interface |
| Agent framework | LangGraph | explicit graph, easy to walk through node-by-node live |
| LLM | Groq (swap via `.env`) | free tier, fast inference, OpenAI-compatible |
| Embeddings | sentence-transformers, local | no API key, no extra hosted service |
| Vector DB | Qdrant Cloud (free tier) | hosted, no local infra to manage |
| Reranker | cross-encoder, local | real reranking step, fully explainable |

## Project structure

```
clauseguard/
├── agent/        # LangGraph graph definition + tool implementations
├── rag/          # Chunking, embeddings, vector store, retrieval, reranking
├── prompts/      # Versioned system prompts
├── api/          # FastAPI route handlers
├── ui/           # Streamlit frontend
├── tests/        # test_rag.py, test_tools.py
├── data/         # Source contract PDF
├── config.py     # Central settings loader (reads .env — see config.py)
├── .env.example  # Every required env var, documented
├── decisions.md  # Why each technical choice was made
└── README.md
```

## Setup (~5 minutes)

1. Open this repo in GitHub Codespaces (or clone locally)
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Copy the env template and fill in real values:
   ```
   cp .env.example .env
   ```
   - `LLM_API_KEY` — free key from [console.groq.com](https://console.groq.com)
   - `QDRANT_URL` / `QDRANT_API_KEY` — free cluster from [cloud.qdrant.io](https://cloud.qdrant.io)
4. Run the API:
   ```
   uvicorn api.main:app --reload
   ```
5. In a second terminal, run the UI:
   ```
   streamlit run ui/app.py
   ```
6. Confirm it's alive:
   ```
   curl localhost:8000/health
   ```

## Architecture

_(ASCII diagram of the agent graph added once it's built)_

## Running tests

```
pytest tests/
```

## Known limitations

_(documented honestly as each tool is built — see decisions.md)_
