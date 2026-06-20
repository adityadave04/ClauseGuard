import json
import requests
import streamlit as st

st.set_page_config(
page_title="ClauseGuard",
page_icon="📄",
layout="wide"
)

st.title("📄 ClauseGuard")
st.caption("AI Contract Intelligence Assistant")

# Sidebar

with st.sidebar:
    st.header("ClauseGuard")

    mode = st.radio(
        "Choose Tool",
        [
            "Ask Anything",
            "Risk Scan",
            "Key Data Extract"
        ]
    )

    st.divider()

    st.subheader("Examples")

    st.markdown("""
* Can either party terminate for convenience?
* What are the payment terms?
* What obligations survive termination?
* What is the limitation of liability?
* Which law governs the agreement?
""")

# Session state

if "answer" not in st.session_state:
    st.session_state.answer = None

if "risks" not in st.session_state:
    st.session_state.risks = None

if "metadata" not in st.session_state:
    st.session_state.metadata = None

# --------------------------------------------------

# FILE UPLOAD

# --------------------------------------------------

st.subheader("📤 Upload Contract")

uploaded_file = st.file_uploader(
    "Upload a contract",
    type=["pdf"]
)

if uploaded_file:
    with open("temp_contract.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("✅ Contract uploaded successfully!")

# --------------------------------------------------

# ASK ANYTHING

# --------------------------------------------------

if mode == "Ask Anything":
    query = st.text_input(
        "Ask a question about the contract"
    )

    col1, col2 = st.columns(2)

    with col1:
        ask_clicked = st.button(
            "Ask",
            use_container_width=True
        )

    with col2:
        clear_clicked = st.button(
            "Clear",
            use_container_width=True
        )

    if clear_clicked:
        st.session_state.answer = None
        st.rerun()

    if ask_clicked:
        if not query.strip():
            st.warning(
                "Please enter a question."
            )
        else:
            with st.spinner(
                "Searching contract..."
            ):
                try:
                    response = requests.post(
                        "http://127.0.0.1:8000/ask",
                        params={
                            "query": query
                        }
                    )
                    response.raise_for_status()
                    st.session_state.answer = response.json()
                except Exception as e:
                    st.error(
                        f"Error: {e}"
                    )

    if st.session_state.answer:
        result = st.session_state.answer
        st.divider()
        st.subheader("Answer")
        st.markdown(
            result["response"]["answer"]
        )
        st.download_button(
            "⬇ Download Answer",
            data=result["response"]["answer"],
            file_name="answer.txt",
            use_container_width=True
        )
        st.divider()
        st.subheader("Sources")
        for source in result["response"]["sources"]:
            st.markdown(
                f"- **Section {source['section_number']}** — {source['section_title']}"
            )

# --------------------------------------------------

# RISK SCAN

# --------------------------------------------------

elif mode == "Risk Scan":
    st.subheader(
        "⚠️ Contract Risk Analysis"
    )

    col1, col2 = st.columns(2)

    with col1:
        scan_clicked = st.button(
            "Analyze Risks",
            use_container_width=True
        )

    with col2:
        clear_clicked = st.button(
            "Clear",
            use_container_width=True
        )

    if clear_clicked:
        st.session_state.risks = None
        st.rerun()

    if scan_clicked:
        with st.spinner(
            "Scanning contract..."
        ):
            try:
                response = requests.get(
                    "http://127.0.0.1:8000/risk"
                )
                response.raise_for_status()
                st.session_state.risks = (
                    response.json()["risks"]
                )
            except Exception as e:
                st.error(
                    f"Error: {e}"
                )

    if st.session_state.risks:
        st.divider()
        for risk in st.session_state.risks:
            severity = risk["severity"]
            if severity == "HIGH":
                st.error(
                    f"{risk['title']} ({risk['section_number']})"
                )
            elif severity == "MEDIUM":
                st.warning(
                    f"{risk['title']} ({risk['section_number']})"
                )
            else:
                st.info(
                    f"{risk['title']} ({risk['section_number']})"
                )
            st.write(
                "**Issue:**"
            )
            st.write(
                risk["issue"]
            )
            st.write(
                "**Recommendation:**"
            )
            st.write(
                risk["recommendation"]
            )
            st.divider()
        st.download_button(
            "⬇ Download Risk Report",
            data=json.dumps(
                st.session_state.risks,
                indent=2
            ),
            file_name="risk_report.json",
            mime="application/json",
            use_container_width=True
        )

# --------------------------------------------------

# KEY DATA EXTRACT

# --------------------------------------------------

elif mode == "Key Data Extract":
    st.subheader(
        "📄 Key Contract Data"
    )

    if st.button(
        "Extract Metadata",
        use_container_width=True
    ):
        with st.spinner(
            "Extracting metadata..."
        ):
            try:
                response = requests.get(
                    "http://127.0.0.1:8000/extract"
                )
                response.raise_for_status()
                st.session_state.metadata = (
                    response.json()["metadata"]
                )
            except Exception as e:
                st.error(
                    f"Error: {e}"
                )

    if st.session_state.metadata:
        metadata = st.session_state.metadata
        st.divider()
        st.subheader(
            "Extracted Metadata"
        )
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "Payment Terms (Days)",
                metadata["payment_terms_days"]
            )
            st.metric(
                "Notice Period (Days)",
                metadata["notice_period_days"]
            )
        with col2:
            st.metric(
                "Termination Fee %",
                metadata["termination_fee_percent"]
            )
            st.metric(
                "Uptime SLA %",
                metadata["uptime_sla_percent"]
            )
        st.write(
            "Agreement Number"
        )
        st.code(
            metadata["agreement_number"]
        )
        st.success(
            metadata["service_provider"]
        )
        st.info(
            metadata["client"]
        )
        st.write(
            metadata["governing_law"]
        )
        st.download_button(
            "⬇ Download Metadata",
            data=json.dumps(
                metadata,
                indent=2
            ),
            file_name="metadata.json",
            mime="application/json",
            use_container_width=True
        )
