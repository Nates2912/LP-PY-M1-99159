import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    dataadmissao: str
    matricula: str
    endereco: str

@dataclass
class Cliente:
    nome: str
    data_aniversario: str
    endereco: str

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nData de nascimento: {self.data} \nRG: {self.rg} \nCPF: {self.cpf} \n")

lista_de_funcionarios = []
lista_de_clientes = []
QUANTIDADE_FUNCIONARIOS = 2
QUANTIDADE_CLIENTES= 2

for i in range (QUANTIDADE_FUNCIONARIOS):
    funcionario = Funcionario(
    nome= input ("Digite seu nome: "), dataadmissao= int(input("Digite sua data de admissão: ")), matricula= int(input("Digite sua matricula: ")), endereco= ("Digite seu endereço: ")
    )
    lista_de_funcionarios.append(funcionario)
    
    cliente = Cliente(
    nome= input ("Digite seu nome: "), data_aniversario = ("Digite sua data de admissão: "), endereco= ("Digite seu endereço: ")
    )
    lista_de_clientes.append(cliente)

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
