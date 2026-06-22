import streamlit as st

st.set_page_config(page_title="HRIS Dashboard", layout="wide")

st.title("HRIS Workforce Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Employees", "250")
col2.metric("Present Today", "220")
col3.metric("Absent", "30")
col4.metric("Departments", "12")

st.divider()

st.subheader("Welcome")
st.write("This is my first HRIS dashboard.")
