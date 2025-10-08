import os
import time 

os.system("cls")

# função sem parametros (parentesis) e sem retorno
def limpa_tela():
    os.system("cls")
    time.sleep(3) # espera 3 segundos

#funcao com parametros (parentesis) e com retorno
def calcular_media (n1, n2):
    calcular = (n1 + n2) / 2
    return calcular

#funçao com parametros e sem retorno
def mostrar_resultado(media):
    print(f"Results: {media}")
    if media >= 7:
        print("Approved")
    else:
        print("Declined.")

# chamando a funçao
limpa_tela()
numero1 = int(input("Type in a number: "))
numero2 = int(input("Type in a number: "))

#funcao com parametros (parentesis) e com retorno
media = calcular_media(numero1, numero2)
#funçao com parametros e sem retorno
mostrar_resultado(media)

