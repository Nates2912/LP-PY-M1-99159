# Construa um algoritmo que calcule a média aritmética de vários valores inteiros positivos, inseridos pelo usuário. 
# O final da leitura acontecerá quando for lido um valor negativo.
# Mostre a média aritmética dos números informados pelo usuário.

import os 
os. system ("cls")

soma = 0
quantn = 0

while True:
    num = int(input("Number: "))
    if num <0:
        break
    quantn += 1
    soma += num
    
avr = soma/quantn
    
print(f"Average: {avr}")

    