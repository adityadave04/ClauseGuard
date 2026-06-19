# Technical Decisions

This document explains the key technical choices made while building
ClauseGuard, and why. Filled in progressively as each piece is built —
sections marked TBD get written in the commit that implements them, while
the reasoning is still fresh.

## 1. Chunking strategy
_(TBD — RAG ingestion commit)_

## 2. Agent framework choice
_(TBD — agent graph commit)_

## 3. Reranking approach
_(TBD — RAG retrieval commit)_

## 4. Vector DB choice

Qdrant Cloud (hosted, free tier) was chosen over a local Chroma instance to
keep the whole project cloud-native — no local database process to start,
manage, or lose state on between sessions, and it forces the "configure
everything via .env" requirement to actually be exercised end-to-end
(URL + API key, not a file path).

## 5. LLM provider choice

Groq was chosen for the LLM layer: free tier, very fast inference (matters
for an agent making several calls per query), and an OpenAI-compatible API
that LangGraph/LangChain support natively. The provider is selected
entirely through `LLM_PROVIDER` / `LLM_API_KEY` / `LLM_MODEL` in `.env` —
swapping to Gemini or another provider is a config change, not a code
change.

## 6. Known limitations / ambiguities in the source contract

Documenting these now, before building the extraction tool, so the
implementation can be deliberate about them rather than accidentally
getting them wrong:

- **Contract value conflict.** The cover page and Clause 3.1 both define
  "Contract Value" as INR 2,40,00,000, and 3.1 explicitly caps total
  contract value at that figure "unless agreed by Change Order." Schedule
  D's fee breakdown table, however, sums to INR 2,54,00,000, with a
  footnote attributing the gap to a contingency reserve "subject to
  reconciliation audit" — i.e., not yet an approved Change Order. The
  extraction tool is built to prefer the defined-term value (24,000,000)
  over the schedule subtotal, since that's the legally operative figure.
  A naive "grab the number near the word total" approach would get this
  wrong.

- **Ambiguous notice period.** The contract contains at least five
  different notice periods depending on context: the cover page's generic
  30-day written notice, 90 days for non-renewal (8.2) and for termination
  for convenience (8.4), 15 days for late-payment suspension (3.4.2), and
  5 business days for emergency Change Orders (2.3.3). The required schema
  has one `notice_period_days` field. We populate it from the cover page's
  explicitly labeled "Notice Period" term (30 days), since it's the one
  defined as a standalone contract term rather than embedded in a specific
  clause's logic — but this is a genuine schema/contract mismatch worth
  flagging rather than silently resolving.
