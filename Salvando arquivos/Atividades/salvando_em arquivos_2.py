import os
os.system
from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: str

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}")

lista_de_pacientes = []
QUANTIDADE_PACIENTES = 2

for i in range (QUANTIDADE_PACIENTES):
    paciente = Paciente(
    nome = input ("Digite seu nome:"), idade = int(input("Digite sua Idade:"))
    )
    lista_de_pacientes.append(paciente)

    nome_do_arquivo = "dados_pacientes.csv"
    with open(nome_do_arquivo, "a") as arquivos_pacientes:
        for paciente in lista_de_pacientes:
            arquivos_pacientes.write(f"{paciente.nome}, {paciente.idade}")
            print("Dados salvos com sucesso.")

print("\nExibindo lista de pacientes")
for paciente in lista_de_pacientes:
    paciente.exibir_dados()