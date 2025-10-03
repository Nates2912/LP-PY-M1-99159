#Escreva um algoritimo que socilicite do úsuario um número e mostre a tabuada de multiplicação do número informado

import streamlit as st
import time


st.title("Multiplication table!")
st.header("Select a number from 1 to 10 to view its table.")

n1 = st.number_input ("Type in a number: ", min_value= 0, max_value=10, step = 1)

if st.button("Start"):
    for i in range (1,11):
        st.write(f"{n1} x {i} = {n1 * i}")
        time.sleep(1) #cria tempo entre os numeros aparecendo na tela, nao funciona sem import time
        n = n1 * i 
    st.header ("Fim")

#antigo
# st.write(f"{n1} x {i} = {n}")