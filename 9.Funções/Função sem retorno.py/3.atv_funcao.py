import os
os.system("cls")

#função com passagem de parametros (parentesis)
#criando a funçao
def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Type in a number: "))

tabuada(numero)

