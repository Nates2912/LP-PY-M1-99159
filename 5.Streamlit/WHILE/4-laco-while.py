# Escreva um algoritmo que solicite duas notas para um aluno. 


# Caso seja menor que 0 ou maior que 10, mostre a pergunta
# novamente.



# Calcule e mostre a média aritmética do aluno.



# import os
# os.system("cls")

# print ("Laço de repetição - While")

# soma = 0

#     while True:
#         n1 = int(input(f"Type in {i+1}º grade: "))
#         if n1 <0 and n1 >10:
#            print("invalid")
#         else:
#               soma = soma + n1            
#               break

# avr = soma/QN

# print(f"The average was {avr}") 


import streamlit as st

st.title("Grades! Again...")
st.header("Type in the students grades.")
        
n1 = st.number_input (f"Type in 1º grade: ", min_value= 0, max_value= 10, step =1)
n2 = st.number_input (f"Type in 2º grade: ", min_value= 0, max_value= 10, step =1)

avr = (n1+n2)/2

if st. button ("Calcular média"):
    st.info(f"Average: {avr}")