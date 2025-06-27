import streamlit as st
import pandas as pd
import os
import subprocess

st.title("📊 CSV Analyzer")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded: {uploaded_file.name}")

    st.write("### Preview of CSV")
    df = pd.read_csv(file_path)
    st.dataframe(df.head())

    if st.button("🧹 Clean CSV"):
        subprocess.call(["bash", "scripts/clean_csv.sh", file_path])

    if st.button("📄 Generate Report"):
        subprocess.call(["bash", "scripts/generate_report.sh", file_path])
