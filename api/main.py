"""
FastAPI application entrypoint.
"""

import logging

from fastapi import FastAPI

logging.basicConfig(level="INFO")
logger = logging.getLogger("clauseguard")

app = FastAPI(
title="ClauseGuard",
description="Contract Intelligence Agent — Ask Anything, Risk Scan, Key Data Extract",
version="0.1.0",
)

@app.get("/health")
def health_check():
    logger.info("Health check called")
    return {"status": "ok"}

from agent.graph import contract_agent

@app.post("/ask")
def ask(query: str):

    response = contract_agent.invoke(
        {
            "query": query
        }
    )

    return response