# Escrever um programa de computador que solicite do usuário 3 notas 
# ao final, apresente a média e mostre para o usuário se o aluno está aprovado, em recuperação ou reprovado. 

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
    elif avr >=4 and avr <7 :
        st.info (f"The average is: {avr:.1f}")
        st.warning ("Caution, you might not get approved...")
    elif avr <4:
        st.info(f"The average is: {avr:.1f}")
        st.error ("Not approved. Will have to repeat the year.")
    
else:
    st.info("Input a number.")
