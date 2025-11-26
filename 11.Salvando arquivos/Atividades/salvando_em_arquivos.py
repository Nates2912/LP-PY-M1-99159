import os
os.system("cls")

quantidade_alunos= 2
lista_alunos = []

from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    idade: int
    telefone: str
    email: str

print("Solicitando dados:")
for i in range (quantidade_alunos):
    alunos = Aluno (
        nome= input("\nDigite seu nome: "), 
        idade= int(input("Digite sua idade: ")), 
        telefone= input("Digite seu telefone: "), 
        email= input("Digite seu E-mail: ")
    )
    lista_alunos.append(alunos)

print("Exibindo dados: ")
arquivo = "dados_alunos.txt"

with open(arquivo, "a") as arquivo_alunos: # O "a" adiciona e e nao apaga o antigo
    for alunos in lista_alunos:
        arquivo_alunos.write(f"{alunos.nome},\n {alunos.idade},\n{alunos.telefone},\n{alunos.email}") 
    print("Salvo com sucesso!")
