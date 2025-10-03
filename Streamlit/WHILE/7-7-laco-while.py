# Escreva um algoritmo que leia três notas de um aluno.
#Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
# Após receber as notas dentro dos parâmetros acima, calcule a média 
# Verifique se o aluno está aprovado, recuperação ou reprovado considerando os seguintes critérios: 
# Se a média for a partir de 7, aprovado; 
# Se a média for entre 5 e 6,9, o aluno está em recuperação; 
# Caso seja menor que 5, o aluno está reprovado.

import streamlit as st

st.title("Grades!")
st.header("Input the student's grades.")


soma = 0
avr = 0 #para soma  defaultar como 0 no começo

for i in range (1,4):
    n1 = st.number_input (f"Type in {i}º grade: ", min_value= 0, max_value= 10)
    soma = soma + n1 

avr = soma/3
   
if st.button("Start"):

    if avr >=7:
        st.info (f"The average is: {avr:.1f}")
        st.success ("Good job! approved!")
    elif avr >=5 and avr <6.9 :
        st.info (f"The average is: {avr:.1f}")
        st.warning ("Caution, you might not get approved...")
    elif avr <5:
        st.info(f"The average is: {avr:.1f}")
        st.error ("Not approved. Will have to repeat the year.")
    
else:
    st.info("Input a number.")