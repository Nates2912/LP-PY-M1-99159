import os

os.system("cls")

# função sem parametros (parentesis) e sem retorno
def limpa_tela():
    os.system("cls")

#funcao com parametros (parentesis) e com retorno
def calcular_centimetros (n1):
    return (n1 * 100)

#funçao com parametros e sem retorno
def mostrar_resultado(centimetros):
    print(f"Centimetros: {centimetros}")

# chamando a funçao
limpa_tela()
numero1 = float(input("Metros: "))

#funcao com parametros (parentesis) e com retorno
centimetros = calcular_centimetros(numero1)
#funçao com parametros e sem retorno
mostrar_resultado(centimetros)

