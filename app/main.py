import streamlit as st
import pandas as pd
import subprocess
import os

st.set_page_config(layout="wide")
st.title("📊 Smart CSV Analyzer")

uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])

if uploaded_file:
    # Save uploaded file
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File saved as {file_path}")

    # Show file preview
    df = pd.read_csv(file_path)
    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe())

    if st.button("🧹 Clean CSV (Shell Script)"):
        subprocess.run(["bash", "scripts/clean_csv.sh", file_path])
        st.success("Cleaned CSV saved in /reports")

    if st.button("📄 Generate Report (Shell Script)"):
        subprocess.run(["bash", "scripts/generate_report.sh", file_path])
        st.success("Report generated in /reports")

    if st.button("🌀 Git Auto-Commit Report"):
        subprocess.run(["bash", "scripts/git_logger.sh"])
        st.success("Report committed to Git repository")
