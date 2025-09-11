#fazer um algoritimo que pede 5 numeros e dps os soma

import streamlit as st
import time

st.title("Summin' up!")
st.header("Type in 5 numbers to sum em' up.")

soma = 0 #para soma  defaultar como 0 no começo

for i in range (1,6):
    n1 = st.number_input (f"Type in {i}: ", min_value= 2, step = 1)
    soma = soma + n1 #para a soma ser a mesma coisa do numero
    #soma += numero
    
if st.button("Start"):
    st.success (f"The sum is: {soma}")
else:
    st.info("Input a number.")