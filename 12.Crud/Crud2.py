import os
import time
from dataclasses import dataclass
os.system("cls || clear")

lista_clientes = []

@dataclass
class Cliente:
    #atributos da classe
    #atributos sao variaveis que pertecem a classe
    nome: str
    email: str
    telefone: str

    #metodo para mostrar as informações dos clientes
    #método é o nome dado a uma função que pertence a classe
    #a classe normalmente e maiusculo e o objeto minusculo

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
    print("\n=== Adicionar novo cliente ===")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone: ")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f"\nCliente {nome} adicionado com sucesso!")

#função para encontrar um cliente na lista
def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    nome_buscar = input("Digite o nome do cliente: ")
    for cliente in lista_clientes: 
        if cliente.nome.lower() == nome_buscar_lower:
            return cliente
    return None #significa retornar vazio, sem conteúdo

#funcao para mostrar todos os clientes
def mostrar_todos_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    print("\n=== Lista de clientes ===")
    for cliente in lista_clientes:
        cliente.mostrar_dados()

#função para atualizar clientes
def atualizar_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    #Mostrar lista
    mostrar_todos_clientes(lista_clientes)
    print("\n=== Atualizar dados do cliente ===")
    nome_buscar = input("\nDigite o nome do cliente: ")
    cliente_para_atualizar = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_atualizar: 
        print("\nPessoa Encontrada. ")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {cliente_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"\nE-mail atual: {cliente_para_atualizar.email}")
        novo_email = input("Novo e-mail: ")
        
        print(f"\nTelefone atual: {cliente_para_atualizar.telefone}")
        novo_telefone = input("Novo telefone: ")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email
        if novo_telefone:
            cliente_para_atualizar.telefone = novo_telefone
        
        print(f"\nDados do cliente: {nome_buscar} atualizados com sucesso!")
    else:
        print(f"\nCliente com nome: {nome_buscar} não encontrado.")

#função para excluir um cliente
def excluir_cliente(lista_cliente):
    if lista_esta_vazia(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes)

    nome_buscar = input("\nDigite o nome do cliente que deseja excluir: ")

    cliente_para_remover = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_remover:
        lista_cliente.remove(cliente_para_remover)
        print(f"\nCliente {cliente_para_remover.nome} excluído com sucesso!")
    else: print(f"\nCielnte com o nome {nome_buscar} não encontrado")


#mostrando menu.
while True:
    print("""
=== GERENCIADOR DE CLIENTES ===       
1 - Adicionar         
2 - Mostrar todos    
3 - Atualizar     
4 - Excluir 
0 - Sair
        """)
    
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_cliente(lista_clientes)
        case 2:
            mostrar_todos_clientes(lista_clientes)
        case 3:
            atualizar_clientes(lista_clientes)
        case 4: 
            excluir_cliente(lista_clientes)
        case 0: 
            print("Saindo do programa...")
            break
        case _:
            print("\nOpção inválida. \nTente novamente.")

    #pausa antes de mudar o menu
    if opcao !='' and opcao!=0:
        time.sleep(3)
    elif opcao == 1:
        time.sleep(1)
    
    #limpa a tela
    if opcao != 0:
        os.system("cls || clear")
