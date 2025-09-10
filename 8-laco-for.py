import streamlit as st
import time

st.title ("Laço de repetição - FOR")

st.header("Contagem de 100 a 120")

if st.button("Iniciar"):
    for i in range(100,120+1, 2):
        st.info(i)
        time.sleep(1) #cria tempo entre os numeros aparecendo na tela, nao funciona sem import time
    st.header ("Fim")