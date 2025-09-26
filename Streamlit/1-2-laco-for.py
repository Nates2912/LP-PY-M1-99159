#Escrever um algoritimo que mostre os números ímpares entre 1 e 20, no steamlit.

import streamlit as st
import time

st.title ("Laço de repetição - FOR")

st.header("Contagem de 1 entre 20 só com números impares")

if st.button("Iniciar"):
    for i in range(1,20, 2):
        st.info(i)
        time.sleep(0.5) #cria tempo entre os numeros aparecendo na tela, nao funciona sem import time
    st.header ("Fim")