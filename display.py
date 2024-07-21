import streamlit as st

def display_data(df):
    if df is not None:
        st.write("### Data Overview")
        st.write(df.head())
        
        st.write("### Basic Statistics")
        st.write(df.describe())
