import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco : Endereco

pessoa1 = Pessoa(nome=input("Digite seu nome: "), email= input ("Digite seu e-mail: "),
                endereco= Endereco (input("Digite seu endereço: "), numero=input("Digite o número da sua casa: "), cidade= input("Digite sua cidade: ")))

print(f"Nome: {pessoa1.nome}, E-mail: {pessoa1.email}, Endereço: {pessoa1.endereco.logradouro}, Número: {pessoa1.endereco.numero}, Cidade: {pessoa1.endereco.cidade}")

