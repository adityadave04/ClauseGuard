"""
Tool implementations invoked by the LangGraph agent (agent/graph.py).

Each tool here should be a plain Python function with a clear typed
signature, decorated/wrapped for LangGraph tool-calling. Keeping the tool
bodies here (rather than inline in graph.py) keeps the graph definition
readable as just routing logic.

TODO:
- risk_scan(contract_chunks) -> structured JSON risk report with clause
  references and risk reasons, checked against every category in the
  Section 7 keyword taxonomy from the assignment brief (Liability,
  Termination, Financial Risk, Legal/Dispute, Obligations, Data & IP)
- extract_data(contract_chunks) -> JSON matching the required schema
  (Section 8 of the brief), validated against real contract values
"""
