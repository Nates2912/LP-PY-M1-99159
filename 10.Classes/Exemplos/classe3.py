import os
from dataclasses import dataclass

os.system("cls")

# Criando uma classe.
#Cliente e uma pessoa?
#Pode ter CPF? Endereço? Nome completo? Título de eleitor? E-mail? Telefone?
#Seu sistema precisa de algumas informaçoes para realizar uma venda.
#Para uma venda(entrega, nesse caso) são usados endereço, nome, telefone. Basicamente, um mini-mundo.
#O proposito da classe e delimitar as caracteristicas de uma pessoa somente para o que o sistema ´precisa

@dataclass
class Cliente:
    nome: str
    endereco: str
    telefone: str

    #Função apenas dessa classse
    def mostrar_dados_cliente(self):
        print(f"Nome: {self.nome}\n Endereço: {self.endereco}\nTelefone: {self.telefone}")

# Criando dois clientes com as características
# definidas na classe.
cliente1 = Cliente(nome="Marta", endereco="Rua A.", telefone= "71-98876-2334" )

cliente1.mostrar_dados_cliente


