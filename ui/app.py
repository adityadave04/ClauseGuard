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

# ----------------------------------------

# ASK ANYTHING

# ----------------------------------------

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
                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    params={
                        "query": query
                    }
                )
                st.session_state.answer = response.json()

    if st.session_state.answer:
        result = st.session_state.answer
        st.divider()
        st.subheader("Answer")
        st.markdown(
            result["response"]["answer"]
        )
        st.divider()
        st.subheader("Sources")
        for source in result["response"]["sources"]:
            st.markdown(
                f"- **Section {source['section_number']}** — {source['section_title']}"
            )

# ----------------------------------------

# RISK SCAN

# ----------------------------------------

elif mode == "Risk Scan":
    st.subheader("⚠️ Contract Risk Analysis")

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
            response = requests.get(
                "http://127.0.0.1:8000/risk"
            )
            st.session_state.risks = response.json()["risks"]

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

elif mode == "Key Data Extract":

    st.subheader("📄 Key Contract Data")

    if st.button(
        "Extract Metadata",
        use_container_width=True
    ):

        with st.spinner(
            "Extracting metadata..."
        ):

            response = requests.get(
                "http://127.0.0.1:8000/extract"
            )

            st.session_state.metadata = (
                response.json()["metadata"]
            )

    if st.session_state.metadata:

        st.divider()

        st.subheader("Extracted Metadata")

        st.json(
            st.session_state.metadata
        )