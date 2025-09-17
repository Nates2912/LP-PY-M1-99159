import streamlit as st

st.title("Grades! Again...")
st.header("Type in the students grades.")

pas = "1"
log = "1"

User = st.text_input("User: ")
Password = st.text_input("Password:", type = "password")

if st.button("Enter"):
    if User == log and Password == pas:
            st.success ("Welcome back!")
    else:
        st.error("Invalid, try again.")
