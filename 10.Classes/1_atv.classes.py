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
pessoa1 = Pessoa("Alice",30, 55 ,1.67)

#usando pessoa1 ja que foi definido que e igual a classe Pessoa
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nPeso: {pessoa1.peso}kg\nAltura: {pessoa1.altura}m")