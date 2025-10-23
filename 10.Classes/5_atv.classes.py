import os
os.system("cls")

#traz a ferramenta.
from dataclasses import dataclass

#aplica essa ferramenta à classe.
@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str
   
    def mostrar_dados(self):
       
        print(f"Nome: {self.nome}\nEndereço: {self.endereco}\nE-mail: {self.email}")
    def mostrar_nome(self):
        
        print(f"Nome: {self.nome}")

#Da pra fazer varias variaveis com as mesmas funçoes com isso
print("Solicitando os dados da pessoa")
#vetor!!!
lista_pessoas = []
for i in range(2):
    pessoa = Pessoa(nome=input("Digite seu nome: "),
                    email=input("Digite sua e-mail: "),
                    endereco=input("Digite sua endereço: "))
    lista_pessoas.append(pessoa)

os.system("cls")

print("\nExibindo os dados pessoais")
for pessoa in lista_pessoas:
    pessoa.mostrar_dados()

print("\nExibindo o nome")
for pessoa in lista_pessoas:
    pessoa.mostrar_nome()
