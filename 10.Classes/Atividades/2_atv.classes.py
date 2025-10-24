import os
os.system("cls")

#traz a ferramenta.
from dataclasses import dataclass

#aplica essa ferramenta à classe.
@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: str
    endereco: str


#fazendo pessoa1 ser igual a Pessoa 
print("Solicitando os dados da pessoa")
pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                 email=input("Digite sua e-mail: "), 
                 telefone=input("Digite seu telefone: ") ,
                 endereco=input("Digite sua endereço: "))

#usando pessoa1 ja que foi definido que e igual a classe Pessoa
print("\n Exibindo os dados da pessoa")
print(f"Nome: {pessoa1.nome}\ne-mail: {pessoa1.email}\ntelefone: {pessoa1.telefone}\nendereço: {pessoa1.endereco}")