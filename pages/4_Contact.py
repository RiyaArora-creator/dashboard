import streamlit as st

st.title("Contact")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

st.button("Submit")
