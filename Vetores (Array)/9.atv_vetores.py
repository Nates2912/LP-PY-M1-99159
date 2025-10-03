import os
os.system ("cls")

#como cria um vetor (lista)

lista_num = []

#inserindo elas
for i in range (3):
    num1 = int(input(f"Type the {i+1}º number: "))
    if num1 < 0:
        num1 = 0
    lista_num.append(num1)


for num1 in lista_num:
    print(f"Number: {num1}")



        

