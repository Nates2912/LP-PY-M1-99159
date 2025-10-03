import os
os.system("cls")

#função com passagem de parametros (parentesis)
#criando a funçao
def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} is an even number.")
    else:
        print(f"{numero} is NOT an even number.")

numero = int(input("Type in a number: "))


par_ou_impar(numero)