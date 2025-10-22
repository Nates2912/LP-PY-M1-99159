import os
os.system("cls")

#função com passagem de parametros (parentesis)
#criando a funçao
def saudacao(nome, age):
    print(f"Hello, {nome}! Welcome!")
    print(f"You're {age} years old.")

#solicitando dados
nome = input("Type in your name: ")
age = int(input("Type in your age: "))

#"chamando" a funçao
saudacao(nome, age)
