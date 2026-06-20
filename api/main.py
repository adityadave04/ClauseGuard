"""
FastAPI application entrypoint.

For now this only exposes a health check, so we can verify the app boots
correctly from .env configuration before any agent/RAG logic exists.
Routes for the three ClauseGuard tools get added to api/routes.py once the
agent graph (agent/graph.py) is implemented — see that file's TODO.
"""

import logging

from fastapi import FastAPI

from config.settings import settings

logging.basicConfig(level=settings.log_level)
logger = logging.getLogger("clauseguard")

app = FastAPI(
    title="ClauseGuard",
    description="Contract Intelligence Agent — Ask Anything, Risk Scan, Key Data Extract",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    """Liveness check that also confirms .env config loaded without error."""
    logger.info("Health check called")
    return {
        "status": "ok",
        "app_env": settings.app_env,
        "llm_provider": settings.llm_provider,
    }
