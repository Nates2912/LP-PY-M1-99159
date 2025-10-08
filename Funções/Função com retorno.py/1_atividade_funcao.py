import os

os.system("cls")

# função sem parametros (parentesis) e sem retorno
def limpa_tela():
    os.system("cls")
#funcao com parametros (parentesis) e com retorno
def adicao (n1, n2): 
    return (n1 + n2)
def subtracao (n1, n2):
    return (n1 - n2)
def multiplicacao (n1, n2):
    return (n1 * n2)
def divisao (n1, n2):
    return (n1 / n2)
    
#funçao com parametros e sem retorno
def mostrar_resultado(resultados):
    print(f"Results: {resultados}")


# chamando a funçao
limpa_tela()
numero1 = int(input("Type in a number: "))
numero2 = int(input("Type in a number: "))

#funcao com parametros (parentesis) e com retorno
resultados = adicao(numero1, numero2)
resultados2 = subtracao(numero1, numero2)
resultados3 = multiplicacao(numero1, numero2)
resultados4 = divisao(numero1, numero2)
#funçao com parametros e sem retorno
mostrar_resultado(resultados)
mostrar_resultado(resultados2)
mostrar_resultado(resultados3)
mostrar_resultado(resultados4)
   

