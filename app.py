from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

import pandas as pd
import streamlit as st
import json

from pipeline.pipeline import pipeline
from helper.convert_df_to_docs import create_docx


st.title("FMCG Deal Intelligence 📩")

# Initialize session state
if "df" not in st.session_state:
    st.session_state.df = None

# Button to trigger pipeline
if st.button("Generate Newsletter"):
    with st.spinner("Fetching and processing data..."):
        st.session_state.df = pipeline()

# If data exists → show + allow download
if st.session_state.df is not None:
    df = st.session_state.df

    st.success("Newsletter generated!")

    # Preview (optional but useful)
    st.dataframe(df)

    # CSV (in-memory)
    csv = df[['title', 'summary', 'total_score']].to_csv(index=False)

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="top_news.csv",
        mime="text/csv"
    )

    # DOCX
    docx_file = create_docx(df)

    st.download_button(
        label="Download DOCX",
        data=docx_file,
        file_name="top_news.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )










