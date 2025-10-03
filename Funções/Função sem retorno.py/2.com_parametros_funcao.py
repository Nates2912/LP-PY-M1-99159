import os
os.system("cls")

#função com passagem de parametros (parentesis)
#criando a funçao
def saudacao(nome):
    print(f"Hello, {nome}! Welcome!")

#solicitando dados
nome = input("Type in your name: ")

#"chamando" a funçao
saudacao(nome)
