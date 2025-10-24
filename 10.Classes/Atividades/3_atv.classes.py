import os
os.system("cls")

#traz a ferramenta.
from dataclasses import dataclass

#aplica essa ferramenta à classe.
@dataclass
class Pessoa:
    nome: str
    idade: int
   
    #pegando os dados da classe abaixo com self
    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nidade: {self.idade}")

#Da pra fazer varias variaveis com as mesmas funçoes com isso
print("Solicitando os dados da pessoa")
pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                 idade=input("Digite sua Idade: "))
                 
pessoa2 = Pessoa(nome=input("Digite seu nome: "),
                 idade=input("Digite sua Idade: "))
                 
os.system("cls")

print("Exibindo os dados da pessoa")
pessoa1.mostrar_dados()
pessoa2.mostrar_dados()