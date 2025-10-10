# Limpa a tela (opcional)
import os
os.system("cls")

# Pede uma entrada ao usuário
texto = input("Digite algo: ")

# Listas para guardar o que for número e o que não for
numeros = []
letras = []
simbolos = []

# Percorre cada caractere da entrada
for caractere in texto:
    if caractere.isdigit():   # Verifica se é um número
        numeros.append(int(caractere))  # Adiciona na lista de números
    elif caractere.isalpha(): 
        letras.append(caractere)  
    else:
         simbolos.append(caractere)     # Adiciona na lista de letras

# Mostra o resultado
print("Números encontrados:", numeros)
print("Letras encontradas:", letras)
print("Símbolos encontrados:", simbolos)