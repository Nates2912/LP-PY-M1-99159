import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Pessoa:
    nome: str
    endereco : Endereco

pessoa1 = Pessoa(nome="Marta", endereco= Endereco(logradouro="RUA A", numero=23))

print(f"Nome: {pessoa1.nome}")
print(f"Endereço: {pessoa1.endereco.logradouro}")
print(f"Número: {pessoa1.endereco.numero}")
