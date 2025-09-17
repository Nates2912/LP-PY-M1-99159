# import os
# os.system("cls")

# print ("Laço de repetição - While")

# QN=2
# soma = 0

# for i in range (QN):
#     while True:
#         n1 = int(input(f"Type in {i+1}º grade: "))
#         if n1 >=0 and n1 <=10:
#                 break
#     soma = soma + n1            

# avr = soma/QN

# print(f"The average was {avr}") 


import streamlit as st

st.title("Pares e Ímpares!")
st.header("Escreva números, isso ira mostrar quantos são pares e quantos são ímpares.")
        

soma = 0
avr = 0 #para soma  defaultar como 0 no começo

for i in range (1,4):
    n1 = st.number_input (f"Type in {i}º grade: ", min_value= 0, max_value= 10)