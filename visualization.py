import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_visualizations(df):
    if df is not None:
        st.write("### Visualizations")
        
        # Line Chart
        if 'date' in df.columns:
            st.line_chart(df['date'])
        
        # Bar Chart
        if 'category' in df.columns:
            category_counts = df['category'].value_counts()
            st.bar_chart(category_counts)
        
        # Pie Chart
        if 'category' in df.columns:
            category_counts = df['category'].value_counts()
            fig, ax = plt.subplots()
            ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
            st.pyplot(fig)
