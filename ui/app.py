"""
Streamlit UI — placeholder.

TODO (API + UI integration commit): three sections —
  1. Ask Anything   — text input -> answer with section citation
  2. Risk Scan       — button -> structured JSON risk report
  3. Key Data Extract — button -> structured JSON matching the required schema
All three calling the FastAPI routes in api/routes.py, which in turn call
the single shared agent_graph instance.
"""

import streamlit as st

st.set_page_config(page_title="ClauseGuard", page_icon="📄")
st.title("ClauseGuard")
st.caption("Contract Intelligence Agent")

st.info(
    "Scaffolding complete. Ask Anything, Risk Scan, and Key Data Extract "
    "tools land in upcoming commits."
)
