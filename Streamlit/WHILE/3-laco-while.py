import streamlit as st

st.title("Pares e Ímpares!")
st.header("Escreva números, isso ira mostrar quantos são pares e quantos são ímpares.")

n1 = st.number_input("Digite uma nota: " , step= 1)

if st.button("Verficar"):
    if n1 < 0 or n1 > 10:
        st.warning("Deve ser entre 0 e 10.")
    else:
        st.info(f"Nota: {n1}")

    