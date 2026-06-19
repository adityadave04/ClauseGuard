# Prompts

All system prompts used by the agent live here as standalone files, not
inline strings buried in agent/ or rag/ code. This is so prompts can be
versioned and diffed independently of code logic, per the assignment's
"All system prompts, versioned and commented" requirement.

**Convention:** `<tool_name>_v<version>.py`, with a comment block at the
top of every prompt file explaining what it does and what changed from the
previous version (if any).

Expected files, added as each tool is built:
- `rag_answer_v1.py` — Ask Anything synthesis prompt (cites section + quote)
- `risk_scan_v1.py` — Risk Scan prompt (keyword-aware, flags close variants)
- `extract_data_v1.py` — Key Data Extract prompt (enforces the JSON schema)
