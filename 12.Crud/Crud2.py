import os
import time
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Cliente:
    #atributos da classe
    #atributos sao variaveis que pertecem a classe
    nome: str
    email: str
    telefone: str

    #metodo para mostrar as informações dos clientes
    #método é o nome dado a uma função que pertence a classe

    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nE-mail: {self.email} \nTelefone: {self.telefone}")


#função para verificar se a lista tá vazia
def lista_esta_vazia(lista_clientes):
    if not lista_clientes:
        print("Não há clientes cadastrados.")
        return True
    return False

#função para adicionar um novo cliente na lista
def adicionar_cliente(lista_clientes):
    print("\n ===Adicionar novo cliente===")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone: ")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f"\nCliente {nome} adicionado com sucesso!")

#função para 