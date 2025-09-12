# Escrever um programa de computador que solicite do usuário 4 notas e, ao final, apresente a média.

import streamlit as st
import time

st.title("Grades!")
st.header("Input the student's grades.")

soma = 0
avr = 0 #para soma  defaultar como 0 no começo

for i in range (1,5):
    n1 = st.number_input (f"Type in {i}º grade: ", min_value= 0, max_value= 10, step = 1)
    soma = soma + n1 #para a soma ser a mesma coisa do numero
    #soma += numero
    avr = soma/4
   
if st.button("Start"):
    st.success (f"The average is: {avr}")
else:
    st.info("Input a number.")