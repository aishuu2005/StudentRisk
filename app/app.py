import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Engagement Risk", layout="wide")

st.title("🎓 Student Engagement Risk Dashboard")

st.markdown("""
This dashboard helps identify students at **risk of disengagement** early,
so institutions can take timely action ✅.
""")

# File upload section
uploaded_file = st.file_uploader("📂 Upload Student Data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Preview of Uploaded Data")
    st.dataframe(df.head())

    # TEMP placeholder — before ML model is added
    st.warning("⚠️ Risk scoring model not yet connected. ML team is working!")

# Sidebar filters (UI ready for later)
st.sidebar.header("Filters")
st.sidebar.checkbox("Show Only High-Risk Students", value=False)

# Footer
st.markdown("---")
st.caption("Hackathon MVP - Team StudentRisk")
