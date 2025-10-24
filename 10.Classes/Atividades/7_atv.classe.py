import os
os.system("cls")
from dataclasses import dataclass


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

    def mostrar_dados(self):
        print(f"\n==CLIENTE==\n Nome: {self.nome}\n E-mail: {self.email}\n==ENDEREÇO==\n Logadouro:: {self.endereco.logradouro}\n Número: {self.endereco.numero}\n Cidade: {self.endereco.cidade}")

pessoa1 = Pessoa(nome=input("Digite seu nome: "), email= input ("Digite seu e-mail: "),
                endereco= Endereco (input("Digite seu endereço: "), numero=input("Digite o número da sua casa: "), cidade= input("Digite sua cidade: ")))

pessoa1.mostrar_dados()

