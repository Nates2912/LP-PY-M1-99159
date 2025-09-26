# Faça um algoritmo que leia uma quantidade não
# determinada de números inteiros positivos. Calcule: 
# quantidade de números pares e ímpares; 
# média de valores pares 
# média geral dos números lidos. 
# O número que encerrará a leitura será o número zero.

import os 
os. system ("cls")

par = 0
imp = 0
somap = 0
somag = 0
tot_num = 0

while True:
    num = int(input("Number: "))
    if num > 0:
        tot_num += 1
        somag += num
        if num % 2 == 0:
            par += 1
            somap +=num 
            #par
        else:
            imp += 1
            #impar
    if num == 0:
        break


if par != 0:
    mediap= somap / par
else:
    mediap = 0 

if tot_num != 0:
    mediag = somag / tot_num
else: 
    mediag = 0
    
print(f"Par: {par}")
print(f"Odd: {imp}")
print(f"With par: {mediap}")
print(f"Average: {mediag}")
