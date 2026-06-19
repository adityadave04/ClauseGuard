"""
Route handlers for the three ClauseGuard tools.

TODO (API + UI integration commit):
- POST /ask          -> Tool 1, Ask Anything (RAG)
- POST /risk-scan     -> Tool 2, Risk Scan
- POST /extract       -> Tool 3, Key Data Extract

All three must call into the SAME compiled agent_graph instance from
agent/graph.py — not three separate scripts or three separate LLM calls —
per the assignment's explicit "all three features must go through the same
agent instance" requirement. Each route should be a thin wrapper: validate
the request, invoke agent_graph.invoke(...), handle/log errors, return JSON.
"""
