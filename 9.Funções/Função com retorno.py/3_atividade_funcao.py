import os

os.system("cls")

# função sem parametros (parentesis) e sem retorno
def limpa_tela():
    os.system("cls")

#funcao com parametros (parentesis) e com retorno
def calcular_precos (n1, total):
    if inflacao > 100:
        inflacao = n1 * 0.10
    elif inflacao < 100:
        inflacao = n1 * 0.20
    return (n1 + inflacao)

#funçao com parametros e sem retorno
def mostrar_resultado(precofinal):
    print(f"Preço final: {precofinal}")

# chamando a funçao
limpa_tela()
numero1 = int(input("Preço: "))

#funcao com parametros (parentesis) e com retorno
precofinal = calcular_precos(numero1)
#funçao com parametros e sem retorno
mostrar_resultado(precofinal)


