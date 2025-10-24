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



lista_pessoas = []
for i in range(4):
    print("\nSolicitando os dados da pessoa")
    pessoa = Pessoa(nome=input("Digite seu nome: "),
                    idade=input("Digite sua idade: "),
                    peso=input("Digite seu peso: "),
                    altura=input("Digite sua altura: "))
    lista_pessoas.append(pessoa)

os.system("cls")

for pessoa in lista_pessoas:
    print("\nExibindo os dados do cliente")
    pessoa.mostrar_dados()

