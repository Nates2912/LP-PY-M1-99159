import streamlit as st

st.title("Algorithm")

n1 = st.number_input ("Type in your first number: ", min_value= 0, max_value=100)
n2 = st.number_input ("Type in your second number: ", min_value= 0, max_value=100)


sum = n1 + n2
avr = sum /2
pro = n1 * n2
big = max(n1, n2)
sma = min(n1, n2)


if st.button("RESULTS"):  #added later on in the code
    if n1 and n2:  #added later on in the code
        st.write(f"The sum of the two numbers is {sum}.")
        st.write(f"The average of the two numbers is {avr}.")
        st.write(f"The product of the two numbers is {pro}.")
        st.write(f"The bigger number is {big}.")
        st.write(f"The smaller number is {sma}.")

else:
    st.info("Type in the numbers.")  #added later on in the code
#no terminal, streamlit run .\6-laco.py
