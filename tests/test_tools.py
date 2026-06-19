"""
Tests for the agent tools (Risk Scan, Key Data Extract).

TODO (agent commits):
- test_risk_scan_flags_liability_cap(): Section 5.4 should appear in the
  risk report under the Liability category
- test_risk_scan_flags_termination_fee(): Section 8.4 should appear under
  Termination
- test_risk_scan_catches_close_variant(): the 18% p.a. late-payment
  interest in 3.4.1 should be flagged even though the literal word
  "penalty" never appears in the text — exercises the "close variants"
  requirement, not just exact keyword matching
- test_extract_data_matches_schema(): output keys match the required
  schema exactly
- test_extract_data_correct_values(): spot-check against the verified
  answer key, e.g. contract_value_inr == 24000000 (NOT the Schedule D
  subtotal of 25400000 — see decisions.md for why)
"""
