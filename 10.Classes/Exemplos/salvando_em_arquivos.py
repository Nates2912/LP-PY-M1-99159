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

print("Salvando dados")
arquivo = "dados_alunos.txt"

with open(arquivo, "a") as arquivo_alunos: # O "a" adiciona e e nao apaga o antigo
    for alunos in lista_alunos:
        arquivo_alunos.write(f"{alunos.nome}, {alunos.idade}\n") 
    print("Salvo com sucesso!")
