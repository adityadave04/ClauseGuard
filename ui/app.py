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
    st.header("Examples")
    st.markdown("""

* Can either party terminate for convenience?
* What are the payment terms?
* What obligations survive termination?
* What is the limitation of liability?
* Which law governs the agreement?
""")

# Session state

if "result" not in st.session_state:
    st.session_state.result = None

# Question input

query = st.text_input(
    "Ask a question about the contract",
    placeholder="e.g. What obligations survive termination?"
)

col1, col2 = st.columns([1, 1])

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

# Clear button

if clear_clicked:
    st.session_state.result = None
    st.rerun()

# Ask button

if ask_clicked:
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        try:
            with st.spinner("Searching contract..."):
                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    params={
                        "query": query
                    }
                )
                st.session_state.result = response.json()
        except Exception as e:
            st.error(f"Error: {e}")

# Show answer

if st.session_state.result:
    result = st.session_state.result
    st.divider()
    st.subheader("Answer")
    st.markdown(
        result["response"]["answer"]
    )
    st.divider()
    st.subheader("Sources")
    for source in result["response"]["sources"]:
        st.markdown(
            f"""
* **Section {source['section_number']}**
  * {source['section_title']}
"""
        )
