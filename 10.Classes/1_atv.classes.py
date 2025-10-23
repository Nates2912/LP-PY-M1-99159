import os
os.system("cls")

#traz a ferramenta.
from dataclasses import dataclass

#aplica essa ferramenta à classe.
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float


#fazendo pessoa1 ser igual a Pessoa 
print("Solicitando os dados da pessoa")
pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                 idade=int(input("Digite sua idade: ")), 
                 peso=float(input("Digite seu peso: ")) ,
                 altura=float(input("Digite sua altura: ")))

#usando pessoa1 ja que foi definido que e igual a classe Pessoa
print("\n Exibindo os dados da pessoa")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nPeso: {pessoa1.peso}kg\nAltura: {pessoa1.altura}m")