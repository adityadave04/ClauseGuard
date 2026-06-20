import logging

from fastapi import FastAPI

from agent.risk_scanner import RiskScanner
from agent.extractor import MetadataExtractor
from agent.graph import contract_agent

from config.settings import settings

logging.basicConfig(
level=settings.LOG_LEVEL
)

logger = logging.getLogger(
"clauseguard"
)

app = FastAPI(
title="ClauseGuard",
version="0.1.0"
)

risk_scanner = RiskScanner()
extractor = MetadataExtractor()

@app.get("/health")
def health_check():

    return {
        "status": "ok"
    }

@app.post("/ask")
def ask(
    query: str
):
    result = contract_agent.invoke(
        {
            "query": query
        }
    )
    return result

@app.get("/risk")
def risk():
    risks = risk_scanner.scan()
    return {
        "risks": risks
    }

@app.get("/extract")
def extract():
    metadata = extractor.extract()
    return {
        "metadata": metadata
    }