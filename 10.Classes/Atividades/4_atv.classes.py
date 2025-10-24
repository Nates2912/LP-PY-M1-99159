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
    def mostrar_dados_entrega(self):
        print(f"Nome: {self.nome}\nEndereço: {self.endereco}")
    def mostrar_dados_email_marketing(self):
        print(f"Nome: {self.nome}\nE-mail: {self.email}")

#Da pra fazer varias variaveis com as mesmas funçoes com isso
print("Solicitando os dados da pessoa")
pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                 email=input("Digite sua e-mail: "),
                 endereco=input("Digite sua endereço: "))
                 
os.system("cls")

print("Exibindo os dados da pessoa")
pessoa1.mostrar_dados_entrega()
pessoa1.mostrar_dados_email_marketing()
