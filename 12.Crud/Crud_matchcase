import os
os.system("cls || clear")

#Criando uma lista
lista_clientes = []

#Create
print("CREATE - Adicionar / Inserir")
nome = input("Digite seu nome: ")
lista_clientes.append(nome)

print(f"O nome: {nome} foi inserido com sucesso.")

#Read
print("\nRead - Ler / Mostrar")
print(lista_clientes)

#Update
print("\nUpdate - Atualizar / Alterar")
nome_para_atualizar = input("Digite o nome a ser atualizado: ")
if nome_para_atualizar in lista_clientes:
    novo_nome = input("Digite o novo nome: ")
    indice = lista_clientes.index(nome_para_atualizar)
    lista_clientes[indice] = novo_nome
    print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}")
else:
    print(f"O nome {nome_para_atualizar} não foi encontrado.")

print(lista_clientes)

#Delete
print("\nDelete - Excluir / Remover")
nome_para_excluir = input("Digite o nome a ser excluido: ")
if nome_para_excluir in lista_clientes:
    lista_clientes.remove(nome_para_excluir)
    print(f"{nome_para_excluir} foi excluído com sucesso.")
else:
    print(f"O nome {nome_para_excluir} não foi encontrado.")

print(lista_clientes)
