import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    dataadmissao: str
    matricula: str
    endereco: str

    def exibir_dados(self):
        print(f"==FUNCIONÁRIOS== \n Nome: {self.nome} \nData de admissão: {self.dataadmissao} \nMatrícula: {self.matricula} \nEndereço: {self.endereco} \n")

@dataclass
class Cliente:
    nome: str
    data_aniversario: str
    endereco: str

    def exibir_dados(self):
        print(f"==CLIENTES== \n Nome: {self.nome} \nData de nascimento: {self.data_aniversario} \nEndereço: {self.endereco}\n")

lista_de_funcionarios = []
lista_de_clientes = []
QUANTIDADE_FUNCIONARIOS = 1
QUANTIDADE_CLIENTES= 1

for i in range (QUANTIDADE_FUNCIONARIOS):
    print ("Funcionários")
    funcionario = Funcionario(
    nome= input ("Digite seu nome: "), dataadmissao= input("Digite sua data de admissão: "), matricula= input("Digite sua matricula: "), endereco= input("Digite seu endereço: ")
    )
    lista_de_funcionarios.append(funcionario)
    
for i in range (QUANTIDADE_CLIENTES):
    print ("==Cliente==")
    cliente = Cliente(
    nome= input ("Digite seu nome: "), data_aniversario= input ("Digite sua data de nascimento: "), endereco= input("Digite seu endereço: ")
    )
    lista_de_clientes.append(cliente)

#criaçao do arquivo

    nome_do_arquivo = "funcionarios.csv"
    with open(nome_do_arquivo, "a") as arquivos_funcionarios:
        for funcionario in lista_de_funcionarios:
            arquivos_funcionarios.write(f"{funcionario.nome}, {funcionario.dataadmissao}, {funcionario.matricula}, {funcionario.endereco}\n")
            print("Dados salvos com sucesso.")
    nome_do_arquivo2 = "clientes.csv"
    with open(nome_do_arquivo2, "a") as arquivos_clientes:
        for cliente in lista_de_clientes:
            arquivos_clientes.write(f"{cliente.nome}, {cliente.data_aniversario}, {cliente.endereco}\n")
            print("Dados salvos com sucesso.")


print("\nExibindo todos os funcionários: ")
lista = []
try: 
    with open (nome_do_arquivo, "r") as arquivo:
        lista_todos_funcionarios = arquivo.readlines()
        for funcionario in lista_todos_funcionarios:
            nome, dataadmissao, matricula, endereco = funcionario.strip().split(",")
            dados_funcionario = Funcionario(nome=nome, dataadmissao=dataadmissao, matricula=matricula, endereco=endereco)
            lista.append(dados_funcionario)
    for funcionario in lista:
        funcionario.exibir_dados()
except FileNotFoundError:
    print("Erro.")


print("\nExibindo todos os clientes: ")
lista = []
try: 
    with open (nome_do_arquivo2, "r") as arquivos_clientes:
        lista_de_clientes = arquivos_clientes.readlines()
        for cliente in lista_de_clientes:
            nome, data_aniversario, endereco = cliente.strip().split(",")
            dados_cliente = Cliente(nome=nome, data_aniversario=data_aniversario, endereco=endereco)
            lista.append(dados_cliente)
    for cliente in lista:
        cliente.exibir_dados()
except FileNotFoundError:
    print("Erro.")
