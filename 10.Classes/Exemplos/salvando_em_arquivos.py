import os
os.system("cls")

#exemplo - texto que desejo salvar
texto = "Senai"

from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    idade: int
   
lista_alunos = []

for i in range (3):
    alunos = Aluno (nome= input("Digite seu nome: "), idade= int(input("Digite seu idade: ")))
    lista_alunos.append(alunos)

for alunos in lista_alunos:
    alunos.mostrar_dados()
