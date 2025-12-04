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
    data_de_nascimento: str
    ra: str
    curso: str
    endereco = Endereco

    #metodo para mostrar as informações dos alunos
    #método é o nome dado a uma função que pertence a classe
    #a classe normalmente e maiusculo e o objeto minusculo

    def mostrar_dados(self):
        print(f"\n===ALUNO===\nNome: {self.nome} \nAniversário: {self.data_de_nascimento} \nR.A: {self.ra} \nCurso{self.curso}")
        print(f"\n===ENDEREÇO===\nLogadouro: {self.endereco.logradouro} \nNúmero: {self.endereco.numero} \nCidade: {self.endereco.cidade} Estado: {self.estado}")


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
    data_de_nascimento = input("Digite seu aniversário: ")
    ra = input("Digite seu ra: ")
    curso = input("Digite seu curso: ")
    endereco= Endereco(input("Digite seu endereço: ")),
    logradouro = input("Digite seu logradouro"),
    numero=input("Digite o número da sua casa: "),
    cidade= input("Digite sua cidade: ")
    estado= input("Digite seu estado: ")


    novo_aluno = Aluno(nome=nome, data_de_nascimento=data_de_nascimento, ra=ra, curso=curso, endereco=endereco, logradouro=logradouro, numero=numero, cidade=cidade, estado =estado)
    lista_alunos.append(novo_aluno)
    print(f"\nAluno {nome} adicionado com sucesso!")

#função para encontrar um aluno na lista
def encontrar_aluno_por_nome(lista_alunos, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    nome_buscar = input("Digite o aniversário do aluno: ")
    for aluno in lista_alunos: 
        if aluno.nome.lower() == nome_buscar_lower:
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
    nome_buscar = input("\nDigite o aniversário do aluno: ")
    aluno_para_atualizar = encontrar_aluno_por_nome(lista_alunos, nome_buscar)

    if aluno_para_atualizar: 
        print("\nPessoa Encontrada. ")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {aluno_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"\nAniversário atual: {aluno_para_atualizar.nome}")
        novo_data_de_nascimento = input("Novo aniversário: ")
        
        print(f"\nR.A atual: {aluno_para_atualizar.ra}")
        novo_ra = input("Novo R.A: ")

        print(f"\nCurso atual: {aluno_para_atualizar.curso}")
        novo_curso = input("Novo curso: ")

        print(f"\nEndereço atual: {aluno_para_atualizar.endereco}")
        novo_endereco = input("Novo endereço: ")

        print(f"\nLogradouro atual: {aluno_para_atualizar.logradouro}")
        novo_logradouro = input("Novo logradouro: ")

        print(f"\nNúmero atual: {aluno_para_atualizar.numero}")
        novo_numero = input("Novo número: ")
        
        print(f"\nCidade atual: {aluno_para_atualizar.cidade}")
        novo_cidade = input("Nova cidade: ")

        print(f"\nEstado atual: {aluno_para_atualizar.estado}")
        novo_estado = input("Novo estado: ")

        if novo_nome:
            aluno_para_atualizar.nome = novo_nome
        if novo_data_de_nascimento:
            aluno_para_atualizar.nome = novo_data_de_nascimento
        if novo_ra:
            aluno_para_atualizar.ra = novo_ra
        if novo_curso:
            aluno_para_atualizar.curso = novo_curso
        if novo_endereco:
            aluno_para_atualizar.endereco = novo_endereco
        if novo_logradouro:
            aluno_para_atualizar.logradouro = novo_logradouro
        if novo_numero:
            aluno_para_atualizar.numero = novo_numero
        if novo_cidade:
            aluno_para_atualizar.cidade = novo_cidade
        if novo_estado:
            aluno_para_atualizar.estado = novo_estado
        
        print(f"\nDados do aluno: {nome_buscar} atualizados com sucesso!")
    else:
        print(f"\nAluno com nome: {nome_buscar} não encontrado.")

#função para excluir um aluno
def excluir_aluno(lista_aluno):
    if lista_esta_vazia(lista_alunos):
        return
    
    mostrar_todos_alunos(lista_alunos)

    nome_buscar = input("\nDigite o nome do aluno que deseja excluir: ")

    aluno_para_remover = encontrar_aluno_por_nome(lista_alunos, nome_buscar)

    if aluno_para_remover:
        lista_aluno.remove(aluno_para_remover)
        print(f"\nAluno {aluno_para_remover.nome} excluído com sucesso!")
    else: print(f"\nAluno com o nome {nome_buscar} não encontrado")


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
