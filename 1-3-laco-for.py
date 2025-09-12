#Escreva um algoritmo que solicite ao usuário 5 valores inteiros e ao final mostre: 
#quantos números são pares; 
#quantos números são ímpares;


import streamlit as st
import time

st.title("Pares e Ímpares!")
st.header("Escreva números, isso ira mostrar quantos são pares e quantos são ímpares.")

pares = 0 #Para definir 0
impares = 0 #Para definir 0


for i in range (1,6):
    n1 = st.number_input (f"Escreva o {i}º número: ", min_value= 1, max_value= 100, step = 1)
    if n1 % 2 == 0:
        pares = pares + 1 
    else:
        impares = impares + 1
if st.button("Verificar"):
    st.info(f"Quantidade de pares: {pares}")
    st.info(f"Quantidade de ímpares: {impares}")
    st.header("Fim.")
