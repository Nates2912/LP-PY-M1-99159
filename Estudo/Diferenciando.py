
import os
os.system("cls")


texto = input("Digite algo: ")


numeros = []
letras = []
simbolos = []


for caractere in texto:
    if caractere.isdigit():   
        numeros.append(int(caractere))
    elif caractere.isalpha(): 
        letras.append(caractere)  
    else:
         simbolos.append(caractere)  

print("\nNúmeros encontrados:", numeros)
print("Letras encontradas:", letras)
print("Símbolos encontrados:", simbolos)