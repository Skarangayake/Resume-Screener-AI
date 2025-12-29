import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="centered"
)
# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "job_desc" not in st.session_state:
    st.session_state.job_desc = ""

# --------------------------------------------------
# CUSTOM CSS (ALL GREEN BUTTONS)
# --------------------------------------------------
st.markdown("""
<style>
.stButton > button {
    background-color: #22c55e !important;
    color: white !important;
    font-weight: 600;
    border-radius: 8px;
    padding: 0.6rem 1.4rem;
    border: none;
}
.stButton > button:hover {
    background-color: #16a34a !important;
}
textarea {
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🤖 AI Resume Screener")
st.markdown("---")

# --------------------------------------------------
# JOB DESCRIPTION SECTION
# --------------------------------------------------
st.subheader("📝 Job Description")
st.write("Type or paste the job description below")

st.session_state.job_desc = st.text_area(
    "Enter job description here...",
    height=180,
    value=st.session_state.job_desc
)

# Upload job description (TXT)
jd_file = st.file_uploader(
    "Or upload job description file (TXT only)",
    type=["txt"]
)

if jd_file:
    st.session_state.job_desc = jd_file.read().decode("utf-8", errors="ignore")
    st.success("Job description loaded from file")

# --------------------------------------------------
# BUTTONS
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    check = st.button("✅ Check Resume")

with col2:
    clear = st.button("❌ Clear Description")

# --------------------------------------------------
# BUTTON LOGIC
# --------------------------------------------------
if check:
    if not st.session_state.job_desc.strip():
        st.warning("Please enter a job description")
    else:
        st.success("Job description received successfully ✅")

if clear:
    st.session_state.job_desc = ""
    st.success("Job description cleared")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption("AI Resume Screener | Job Description Module by KARAN")