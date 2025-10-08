import os
import time 

os.system("cls")

# função sem parametros (parentesis) e sem retorno
def limpa_tela():
    os.system("cls")
    time.sleep(3) # espera 3 segundos

#funcao com parametros (parentesis) e com retorno
def somar (n1, n2):
    return n1 + n2

#funçao com parametros e sem retorno
def mostrar_resultado(soma):
    print(f"Results: {soma}")

# chamando a funçao
limpa_tela()
numero1 = int(input("Type in a number: "))
numero2 = int(input("Type in a number: "))

#funcao com parametros (parentesis) e com retorno
soma = somar(numero1, numero2)
#funçao com parametros e sem retorno
mostrar_resultado(soma)

