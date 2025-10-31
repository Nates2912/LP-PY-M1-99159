import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro: 
    titulo: str
    ano: int
    autor: Autor

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}\nAno de publicação: {self.ano}\nNome do autor: {self.autor.nome}")

livro = Livro (titulo= input("Título do livro: "),
                ano= input("Ano de publicação: "),
                autor= Autor( 
                    nome= input("Nome do Autor: "),
                    biografia= input("Biografia: ")))

livro.exibir_detalhes()

