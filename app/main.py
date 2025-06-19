import streamlit as st
import pandas as pd
from app.utils import summarize_data

st.title("📊 CSV Data Analyzer")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of your data:")
    st.dataframe(df)

    st.subheader("Data Summary")
    summary = summarize_data(df)
    st.json(summary)
