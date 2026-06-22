import streamlit as st

st.title("Solutions")

st.write("""
Explore workforce solutions designed for modern organizations.
""")

col1,col2,col3 = st.columns(3)

with col1:
    st.info("People Operations")

with col2:
    st.success("Workforce Analytics")

with col3:
    st.warning("Talent Management")
