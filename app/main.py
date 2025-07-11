import streamlit as st
import pandas as pd
import os
import subprocess

st.title("📊 CSV Analyzer")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    # Save the uploaded file
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ Uploaded: {uploaded_file.name}")

    # Preview uploaded CSV
    st.write("### 📋 CSV Preview")
    df = pd.read_csv(file_path)
    st.dataframe(df.head())

    # Button to clean CSV
    if st.button("🧹 Clean CSV"):
        result = subprocess.run(["bash", "scripts/clean_csv.sh", file_path])
        if result.returncode == 0:
            st.success("✅ CSV cleaned successfully!")
        else:
            st.error(f"❌ Error cleaning CSV:\n{result.stderr}")

    # Button to generate report
    if st.button("📄 Generate Report"):
        result = subprocess.run(["bash", "scripts/generate_report.sh", file_path])
        if result.returncode == 0:
            st.success("✅ Report generated successfully!")
        else:
            st.error(f"❌ Error generating report:\n{result.stderr}")
