"""
LangGraph agent graph definition — the core of ClauseGuard.

This module owns the single agent instance that all three tools (Ask
Anything, Risk Scan, Key Data Extract) run through, per the assignment's
"one unified AI agent... not three separate scripts" requirement.

TODO (agent graph commit):
- Define a StateGraph with a router node that decides which tool(s) to call
  based on the incoming request (free-text question vs. button-triggered
  Risk Scan / Extract)
- Wire in the three tool nodes:
    - ask_anything   -> calls into rag/retriever.py + rag/reranker.py
    - risk_scan      -> scans contract chunks against the keyword taxonomy
    - extract_data   -> pulls the fixed JSON schema from the contract
- Add a multi-tool chaining edge: e.g. a free-text question like "what's
  our termination exposure" should route through BOTH risk_scan and
  ask_anything, then synthesize — this is what the rubric calls
  "multi-tool flows" (extract data then cross-check against a risk flag)
- Compile the graph and export `agent_graph` for api/routes.py to invoke
- Add structured logging at every tool-call boundary (tool name, input,
  output) per the "basic logging for agent tool calls" requirement

Tool 1 (Ask Anything) is built first, as a standalone node function, before
the full router/conditional-edge logic is added — see rag/ for that work.
"""
