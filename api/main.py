"""
FastAPI application entrypoint.
"""

import logging

from fastapi import FastAPI
from agent.risk_scanner import RiskScanner

from agent.extractor import MetadataExtractor

extractor = MetadataExtractor()
scanner = RiskScanner()

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



@app.get("/risk")
def risk_scan():

    risks = scanner.scan()

    return {
        "risks": risks
    }

@app.get("/extract")
def extract():

    metadata = extractor.extract()

    return {
        "metadata": metadata
    }