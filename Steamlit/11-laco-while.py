# Faça um algoritmo que leia uma quantidade não
# determinada de números inteiros positivos. Calcule: 
# quantidade de números pares e ímpares; 
# média de valores pares 
# média geral dos números lidos. 
# O número que encerrará a leitura será o número zero.

import os 
os. system ("cls")

contim = 0
contp = 0
somap = 0
somag = 0
tot_num = 0

while True:
    num = int(input("Number: "))
    if num % 2 == 0:
        #par
    else:
        #impar


    quantn += 1
    soma += num
    
avr = soma/quantn
    
print(f"Average: {avr}")
