import os
os.system("cls")

#função com passagem de parametros (parentesis)
#criando a funçao
def par_ou_impar(numero):
    if numero > 0:
        print(f"{numero} is a positive number")
    elif numero == 0:
        print(f"{numero} is 0")
    else:
        print(f"{numero} is a negative number")
numero = int(input("Type in a number: "))


par_ou_impar(numero)