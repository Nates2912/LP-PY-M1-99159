import os
from dataclasses import dataclass

os.system("cls")

# Criando uma classe.
@dataclass
class Cliente:
    nome: str
    endereco: str

    #Função apenas dessa classse
    def mostrar_dados_cliente(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")

# Criando dois clientes com as características
# definidas na classe.
cliente1 = Cliente(nome="Marta", endereco="Rua A.")
cliente2 = Cliente(nome="João", endereco="Rua C.")

