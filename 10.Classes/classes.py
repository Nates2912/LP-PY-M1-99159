import os
os.system("cls")

from dataclasses import dataclass

#estrutura de dados - classe
#cada classe tem seu proprio class
#usado para usar os mesmos nomes para variaveis

@dataclass
class Pessoa:
    nome: str
    idade: int
@dataclass
class Pet:
    nome: str
    idade: int

#Exemplo de uso da classe
pessoa1 = Pessoa("Alice",30)
pet1 = Pet("Bob",4)

print("Pessoa:")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}")

print("Pet:")
print(f"Nome: {pet1.nome}\nIdade: {pet1.idade}")

