import os
os.system("cls")

#função com passagem de parametros (parentesis)
#criando a funçao
def saudacao(nome, age, height, weight):
    print(f"Hello, {nome}! Welcome!")
    print(f"You're {age} years old.")
    print(f"You're {height} meters tall.")
    print(f"You're weigh {weight} kilos.")

#solicitando dados
nome = input("Type in your name: ")
age = int(input("Type in your age: "))
height = float(input("Type in your height: "))
weight = float(input("Type in your weight: "))

#"chamando" a funçao
saudacao(nome, age, height, weight)
