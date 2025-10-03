#crie um programa que solicite o usuario e o login, se tiver errado ele vai pedir denovo, se passar de 3, ele para

import streamlit as st

st.title("User interface.")
st.header("Type in your User and Password (You have 3 attempts.)")

pas = "1"
log = "1"

#VARIAVEIS INTERNAS DO STREAMLIT
st.session_state.setdefault("desabilitar", False)
st.session_state.setdefault("tentativas", 0)

User =st.text_input("User: ", disabled= st.session_state.desabilitar)
Password = st.text_input("Password:", type = "password", disabled= st.session_state.desabilitar)

if st.button("Login"):
    if User == log and Password == pas:
            st.success ("Welcome back!")
    else:
        st.session_state.tentativas +=1
        if st.session_state.tentativas <=3:            
            st.warning(f"Invalid, {st.session_state.tentativas}º attempt.")
        else:
             st.session_state.desabilitar = True
             st.error("No attempts left.")
else: 
    st.info('Insert the User and password.')
