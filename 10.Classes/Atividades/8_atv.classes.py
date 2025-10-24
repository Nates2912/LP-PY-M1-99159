import os
os.system("cls")

#traz a ferramenta.
from dataclasses import dataclass

#aplica essa ferramenta à classe.
@dataclass
class Pessoa:
    nome: str
    idade: str
    peso: float
    altura: float
   
    def mostrar_dados(self):
       
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}")


print("Solicitando os dados da pessoa")

lista_pessoas = []
for i in range(4):
    pessoa = Pessoa(nome=input("Digite seu nome: "),
                    idade=input("Digite sua idade: "),
                    peso=input("Digite seu peso: "),
                    altura=input("Digite sua altura: "))
    lista_pessoas.append(pessoa)

os.system("cls")

print("\nExibindo os dados pessoais")
for pessoa in lista_pessoas:
    pessoa.mostrar_dados()

