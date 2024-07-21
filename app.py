import streamlit as st
from upload import upload_file
from display import display_data
from visualization import plot_visualizations
from recommendations import recommend_analysis
from management import manage_data

def main():
    st.title("Exploratory Data Analysis Tool")
    
    df = upload_file()
    
    if df is not None:
        display_data(df)
        plot_visualizations(df)
        recommend_analysis(df)
        manage_data(df)

if __name__ == "__main__":
    main()
