"""
Centralized application configuration.

Loads all required environment variables from .env (see .env.example for the
full list with descriptions) and exposes them as a single Settings object.
This is the ONLY place that should read environment variables directly —
every other module imports `settings` from here instead of touching
os.environ itself. That keeps the "zero hardcoded credentials" and "runs
with only .env configuration, no model-specific code changes" requirements
enforceable in one place: swapping LLM provider/model/vector DB cluster
never requires touching code, only .env values.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- LLM ---
    # provider is a label used by agent/graph.py to pick the right LangChain
    # chat model client (e.g. "groq", "gemini"). Adding a new provider means
    # adding one branch in that factory function, never touching call sites.
    llm_provider: str = "groq"
    llm_api_key: str
    llm_model: str = "llama-3.3-70b-versatile"

    # --- Vector DB (Qdrant Cloud) ---
    qdrant_url: str
    qdrant_api_key: str
    qdrant_collection_name: str = "clauseguard_contract"

    # --- Embeddings / Reranker ---
    # Both run locally in-process via sentence-transformers — no API key,
    # no external hosting, just a model file pulled from HuggingFace once.
    embedding_model_name: str = "all-MiniLM-L6-v2"
    reranker_model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"

    # --- RAG pipeline tuning ---
    retrieval_top_k: int = 10
    rerank_top_n: int = 4

    # --- App ---
    log_level: str = "INFO"
    app_env: str = "development"
    contract_pdf_path: str = "./data/contract.pdf"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
