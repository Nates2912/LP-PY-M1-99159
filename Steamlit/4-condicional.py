#verifique a idade de uma pessoa
#se menor que 18, mostre: menor de idade
#caso contrario, mostre: maior de idade
#usando streamlit

import streamlit as st

st.title("Age verification")

idade = st.number_input ("Type in your age: ", min_value= 0, max_value=130, step=1)

if st.button("Verify"):
    if idade < 18:
        st.write("Minor")
    else:
        st.write("Adult")

else:
    st.warning("Type it right")