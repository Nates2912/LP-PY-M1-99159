#verifique a media
#solicite ao usuario a media do aluno
#se maior ou igual a 7, mostre  como aprovado
#caso contrario, mostre como reprovado
#usando streamlit

import streamlit as st

st.title("Grade verification!")

average = st.number_input ("Type in their grade: ", min_value= 0, max_value=10)

# gra1 = st.number_input ("Type in their first grade: ", min_value= 0, max_value=10)
# gra2 = st.number_input ("Type in their second grade: ", min_value= 0, max_value=10)
# gra3 = st.number_input ("Type in their third grade: ", min_value= 0, max_value=10)
# gra4 = st.number_input ("Type in their fourth grade: ", min_value= 0, max_value=10)

# average = (gra1 + gra2 + gra3 + gra4) / 4


if st.button("RESULTS"):
    if average >=7:
        st.success("APPROVED")
    else:
        st.error("NOT APPROVED")    #ou st.warning

else:
    st.info("Type it right dude lmao")

# if st.button("RESULTS"):
#     if average >=7:
#         st.write("APPROVED")
#     else:
#         st.write("NOT APPROVED")

# else:
#     st.warning("Type it right dude lmao")