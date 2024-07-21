import pandas as pd
import streamlit as st

def recommend_analysis(df):
    st.write("### Analysis Recommendations")
    
    for column in df.columns:
        dtype = df[column].dtype
        if pd.api.types.is_numeric_dtype(dtype):
            st.write(f"For numeric column '{column}': Consider histogram, boxplot, or trend analysis.")
        elif pd.api.types.is_categorical_dtype(dtype):
            st.write(f"For categorical column '{column}': Consider bar charts or pie charts.")
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            st.write(f"For datetime column '{column}': Consider time series analysis or trend visualization.")
