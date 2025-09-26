# Escreva um algoritmo que pergunte ao usuário se deseja inserir
# mais uma nota, 
# se a resposta do usuário for “N”, 
# o programa fará a média aritmética das notas informadas 
# e mostrará a média aritmética para o usuário.
# Obs.: Use um contador dentro do laço de repetição para contar a
# quantidade de iterações (loops).

import os 
os. system ("cls")

soma = 0
quantn = 0

while True:
    nota = float(input("Grade: "))
    quantn += 1
    soma += nota
    morenota = input("Anymore grades? (Use Y or N):").upper()
    if morenota == "N":
           break
    
avr = soma/quantn
    
print(f"Average: {avr}")

    