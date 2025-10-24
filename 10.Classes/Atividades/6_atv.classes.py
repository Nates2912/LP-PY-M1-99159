import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    cpf: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.telefone}")
    def mostrar_sms(self):
        print(f"\nTelefone: {self.telefone}")

lista__clientes = []

for i in range (3):
    clientes = Cliente (nome= input("Digite seu nome: "), cpf= input("Digite seu cpf: "), telefone= input("Digite seu telefone: "))
    lista__clientes.append(clientes)

for clientes in lista__clientes:
    clientes.mostrar_dados()
for clientes in lista__clientes:
    clientes.mostrar_sms()
