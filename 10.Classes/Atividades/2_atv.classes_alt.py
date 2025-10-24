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

    #pegando os dados da classe abaixo com self
    def mostrar_dados(self):
        print(f"Nome: {self.nome}\ne-mail: {self.email}\ntelefone: {self.telefone}\nendereço: {self.endereco}")

#fazendo pessoa1 ser igual a Pessoa 
print("Solicitando os dados da pessoa")
pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                 email=input("Digite sua e-mail: "), 
                 telefone=input("Digite seu telefone: ") ,
                 endereco=input("Digite sua endereço: "))

os.system("cls")

print("Exibindo os dados da pessoa")
pessoa1.mostrar_dados()