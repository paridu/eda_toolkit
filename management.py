import streamlit as st

def manage_data(df):
    st.write("### Data Management")
    
    if df is not None:
        category_filter = st.sidebar.selectbox("Filter by Category", df['category'].unique())
        filtered_df = df[df['category'] == category_filter]
        st.write(filtered_df)
        
        sort_by = st.sidebar.selectbox("Sort by", df.columns)
        sorted_df = df.sort_values(by=sort_by)
        st.write(sorted_df)
