import os
import time
from dataclasses import dataclass
os.system("cls || clear")

lista_alunos = []

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str
    estado: str
@dataclass
class Aluno:
    #atributos da classe
    #atributos sao variaveis que pertecem a classe
    nome: str
    email: str
    ra: str
    curso: str
    endereco = Endereco

    #metodo para mostrar as informações dos alunos
    #método é o nome dado a uma função que pertence a classe
    #a classe normalmente e maiusculo e o objeto minusculo

    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nE-mail: {self.email} \nR.A: {self.ra} \n ==ENDEREÇO==\n Logadouro:: {self.endereco.logradouro}\n Número: {self.endereco.numero}\n Cidade: {self.endereco.cidade}"")


#função para verificar se a lista tá vazia
def lista_esta_vazia(lista_alunos):
    if not lista_alunos:
        print("Não há alunos cadastrados.")
        return True
    return False

#função para adicionar um novo aluno na lista
def adicionar_aluno(lista_alunos):
    print("\n=== Adicionar novo aluno ===")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    ra = input("Digite seu ra: ")

    novo_aluno = Aluno(nome=nome, email=email, ra=ra)
    lista_alunos.append(novo_aluno)
    print(f"\naluno {nome} adicionado com sucesso!")

#função para encontrar um aluno na lista
def encontrar_aluno_por_email(lista_alunos, email_buscar):
    email_buscar_lower = email_buscar.lower()
    email_buscar = input("Digite o e-mail do aluno: ")
    for aluno in lista_alunos: 
        if aluno.email.lower() == email_buscar_lower:
            return aluno
    return None #significa retornar vazio, sem conteúdo

#funcao para mostrar todos os alunos
def mostrar_todos_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    
    print("\n=== Lista de alunos ===")
    for aluno in lista_alunos:
        aluno.mostrar_dados()

#função para atualizar alunos
def atualizar_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    
    #Mostrar lista
    mostrar_todos_alunos(lista_alunos)
    print("\n=== Atualizar dados do aluno ===")
    email_buscar = input("\nDigite o e-mail do aluno: ")
    aluno_para_atualizar = encontrar_aluno_por_email(lista_alunos, email_buscar)

    if aluno_para_atualizar: 
        print("\nPessoa Encontrada. ")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {aluno_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"\nE-mail atual: {aluno_para_atualizar.email}")
        novo_email = input("Novo e-mail: ")
        
        print(f"\nra atual: {aluno_para_atualizar.ra}")
        novo_ra = input("Novo ra: ")

        if novo_nome:
            aluno_para_atualizar.nome = novo_nome
        if novo_email:
            aluno_para_atualizar.email = novo_email
        if novo_ra:
            aluno_para_atualizar.ra = novo_ra
        
        print(f"\nDados do aluno: {email_buscar} atualizados com sucesso!")
    else:
        print(f"\naluno com e-mail: {email_buscar} não encontrado.")

#função para excluir um aluno
def excluir_aluno(lista_aluno):
    if lista_esta_vazia(lista_alunos):
        return
    
    mostrar_todos_alunos(lista_alunos)

    email_buscar = input("\nDigite o e-mail do aluno que deseja excluir: ")

    aluno_para_remover = encontrar_aluno_por_email(lista_alunos, email_buscar)

    if aluno_para_remover:
        lista_aluno.remove(aluno_para_remover)
        print(f"\naluno {aluno_para_remover.email} excluído com sucesso!")
    else: print(f"\nCielnte com o nome {email_buscar} não encontrado")


#mostrando menu.
while True:
    print("""
=== GERENCIADOR DE alunoS ===       
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
            adicionar_aluno(lista_alunos)
        case 2:
            mostrar_todos_alunos(lista_alunos)
        case 3:
            atualizar_alunos(lista_alunos)
        case 4: 
            excluir_aluno(lista_alunos)
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
