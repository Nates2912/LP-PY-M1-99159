import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    data: str
    rg: str
    cpf: str

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nData de nascimento: {self.data} \nRG: {self.rg} \nCPF: {self.cpf} \n")

lista_de_funcionarios = []
QUANTIDADE_FUNCIONARIOS = 2

for i in range (QUANTIDADE_FUNCIONARIOS):
    funcionario = Funcionario(
    nome = input ("Digite seu nome: "), data = int(input("Digite sua data de nascimento: ")), rg = int(input("Digite seu RG: ")), cpf = int(input("Digite seu CPF: "))
    )
    lista_de_funcionarios.append(funcionario)

    nome_do_arquivo = "funcionarios.csv"
    with open(nome_do_arquivo, "a") as arquivos_funcionarios:
        for funcionario in lista_de_funcionarios:
            arquivos_funcionarios.write(f"{funcionario.nome}, {funcionario.data}, {funcionario.rg}, {funcionario.cpf}\n")
            print("Dados salvos com sucesso.")

print("\nExibindo todos os funcionarios: ")
lista = []
try: 
    with open (nome_do_arquivo, "r") as arquivo:
        lista_todos_funcionarios = arquivo.readlines()
        for funcionario in lista_todos_funcionarios:
            nome, data, rg, cpf = funcionario.strip().split(",")
            dados_funcionario = Funcionario(nome=nome, data=data, rg=rg, cpf=cpf)
            lista.append(dados_funcionario)
    for funcionario in lista:
        funcionario.exibir_dados()
except FileNotFoundError:
    print("Erro.")



