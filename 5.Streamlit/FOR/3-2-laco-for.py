# Escrever um algoritmo que solicite ao usuário um numero
# faça a contagem regressiva
# a partir do número informado até o número 1
# aguardando um segundo para exibir cada número.

import streamlit as st
import time


st.title("Countin'!")
st.header("Select a number from 1 to 100 for the countdown.")

n1 = st.number_input ("Type in a number: ", min_value= 2, max_value=100, step = 1)

if st.button("Start"):
    for i in range (n1, 0,-1):
        st.write(i)
        time.sleep(1)
    st.header ("End")
else:
    st.info("Input a number.")