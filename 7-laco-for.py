import streamlit as st
import time

st.title ("Laço de repetição - FOR")

st.header("Contagem de 1 a 10")

#como faz para o usuario digitar
n1 = st.number_input ("Quantas vezes você quer que conte: ", min_value= 0, max_value=100)

if st.button("Iniciar"):
    for i in range(1,n1 + 1):
        st.write(i)
        time.sleep(1) #cria tempo entre os numeros aparecendo na tela, nao funciona sem import time
    st.header ("Fim")