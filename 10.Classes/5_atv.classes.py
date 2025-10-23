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
   
    #pegando os dados da classe abaixo com self

    def mostrar_dados(self):
        print("Exibindo os dados pessoais")
        print(f"Nome: {self.nome}\nEndereço: {self.endereco}\nE-mail: {self.email}")
    def mostrar_nome(self):
        print("Exibindo o nome")
        print(f"Nome: {self.nome}")

#Da pra fazer varias variaveis com as mesmas funçoes com isso
print("Solicitando os dados da pessoa")
pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                 email=input("Digite sua e-mail: "),
                 endereco=input("Digite sua endereço: "))
                 
pessoa2 = Pessoa(nome=input("Digite seu nome: "),
                 email=input("Digite sua e-mail: "),
                 endereco=input("Digite sua endereço: "))
                 
os.system("cls")

pessoa1.mostrar_dados()
pessoa1.mostrar_nome()
pessoa2.mostrar_dados()
pessoa2.mostrar_nome()
