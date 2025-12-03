import os
import time
from dataclasses import dataclass
os.system("cls || clear")

lista_funcionarios = []

@dataclass
class Cliente:
    #atributos da classe
    #atributos sao variaveis que pertecem a classe
    nome: str
    email: str
    cpf: str
    funcao: str

    #metodo para mostrar as informações dos funcionarios
    #método é o nome dado a uma função que pertence a classe
    #a classe normalmente e maiusculo e o objeto minusculo

    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nE-mail: {self.email} \nCPF: {self.cpf} \nFunção: {self.funcao}")


#função para verificar se a lista tá vazia
def lista_esta_vazia(lista_funcionarios):
    if not lista_funcionarios:
        print("Não há funcionarios cadastrados.")
        return True
    return False

#função para adicionar um novo cliente na lista
def adicionar_cliente(lista_funcionarios):
    print("\n=== Adicionar novo cliente ===")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    cpf = input("Digite seu CPF: ")
    funcao = input("Digite sua função: ")

    novo_cliente = Cliente(nome=nome, email=email, cpf=cpf, funcao=funcao)
    lista_funcionarios.append(novo_cliente)
    print(f"\nCliente {nome} adicionado com sucesso!")

#função para encontrar um cliente na lista
def encontrar_cliente_por_nome(lista_funcionarios, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    nome_buscar = input("Digite o nome do cliente: ")
    for cliente in lista_funcionarios: 
        if cliente.nome.lower() == nome_buscar_lower:
            return cliente
    return None #significa retornar vazio, sem conteúdo

#funcao para mostrar todos os funcionarios
def mostrar_todos_funcionarios(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return
    
    print("\n=== Lista de funcionarios ===")
    for cliente in lista_funcionarios:
        cliente.mostrar_dados()

#função para atualizar funcionarios
def atualizar_funcionarios(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return
    
    #Mostrar lista
    mostrar_todos_funcionarios(lista_funcionarios)
    print("\n=== Atualizar dados do cliente ===")
    nome_buscar = input("\nDigite o nome do cliente: ")
    cliente_para_atualizar = encontrar_cliente_por_nome(lista_funcionarios, nome_buscar)

    if cliente_para_atualizar: 
        print("\nPessoa Encontrada. ")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {cliente_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"\nE-mail atual: {cliente_para_atualizar.email}")
        novo_email = input("Novo e-mail: ")
        
        print(f"\nCPF atual: {cliente_para_atualizar.cpf}")
        novo_cpf = input("Novo CPF: ")

        print(f"\nFunção atual: {cliente_para_atualizar.funcao}")
        nova_funcao = input("Nova função: ")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email
        if novo_cpf:
            cliente_para_atualizar.cpf = novo_cpf
        if nova_funcao:
            cliente_para_atualizar.funcao = nova_funcao
        
        print(f"\nDados do cliente: {nome_buscar} atualizados com sucesso!")
    else:
        print(f"\nCliente com nome: {nome_buscar} não encontrado.")

#função para excluir um cliente
def excluir_cliente(lista_cliente):
    if lista_esta_vazia(lista_funcionarios):
        return
    
    mostrar_todos_funcionarios(lista_funcionarios)

    nome_buscar = input("\nDigite o nome do cliente que deseja excluir: ")

    cliente_para_remover = encontrar_cliente_por_nome(lista_funcionarios, nome_buscar)

    if cliente_para_remover:
        lista_cliente.remove(cliente_para_remover)
        print(f"\nCliente {cliente_para_remover.nome} excluído com sucesso!")
    else: print(f"\nCielnte com o nome {nome_buscar} não encontrado")


#mostrando menu.
while True:
    print("""
=== GERENCIADOR DE FUNCIONÁRIOS ===       
1 - Adicionar         
2 - Mostrar todos    
3 - Atualizar     
4 - Excluir 
0 - Sair
        """)
    
    #evitando erros no programa
    #caso o usuário digite letras
    try:
        opcao = int(input("Digite uma das opções acima: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número...")
        time.sleep(2)
        os.system("cls || clear")
        continue

    match opcao:
        case 1:
            adicionar_cliente(lista_funcionarios)
        case 2:
            mostrar_todos_funcionarios(lista_funcionarios)
        case 3:
            atualizar_funcionarios(lista_funcionarios)
        case 4: 
            excluir_cliente(lista_funcionarios)
        case 0: 
            print("Saindo do programa...")
            break
        case _:
            print("\nOpção inválida. \nTente novamente.")

    #pausa antes de mudar o menu
    if opcao !=1 and opcao!=0:
        time.sleep(3)
    elif opcao == 1:
        time.sleep(1)
    
    #limpa a tela
    if opcao != 0:
        os.system("cls || clear")