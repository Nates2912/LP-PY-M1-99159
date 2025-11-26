import os
os.system("cls")

quantidade_livros= 2
lista_alunos = []

from dataclasses import dataclass

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

print("Solicitando dados:")
for i in range (quantidade_livros):
    livro = Livro (
        nome= input("\nDigite o nome do livro: "), 
        autor= input("Digite o(a) autor: "), 
        categoria= input("Digite sua categoria: "), 
        preco= float(input("Digite seu preço: "))
    )
    lista_alunos.append(livro)

print("Exibindo dados: ")
catalogo = "dados_livros.txt"

with open(catalogo, "a") as catalogo_livros: # O "a" adiciona e e nao apaga o antigo
    for livro in lista_alunos:
        catalogo_livros.write(f"{livro.nome}\n{livro.autor}\n{livro.categoria}\n{livro.preco}\n") 
    print("Salvo com sucesso!")
