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
    cpf: str
@dataclass
class Pet:
    nome: str
    idade: int
    peso: str

#Exemplo de uso da classe
pessoa1 = Pessoa("Alice",30,"086.756.066.32")
pet1 = Pet("Bob",4, "5kg")


print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nCPF: {pessoa1.cpf}")

print("Pet:")
print(f"Nome: {pet1.nome}\nIdade: {pet1.idade}\nPeso: {pet1.peso}")

