import os
os.system ("cls")

#como cria um vetor (lista)
lista_notas = []

#inserindo elas
for i in range (4):
    nota = int(input(f"Input the {i+1}º grade: "))
    lista_notas.append(nota)

soma = sum(lista_notas)
avr = soma / 4

for i in range (4):
     print(f"\nGrade: {lista_notas[i]}")

print(f"\nAverage: {avr}")

print("\nEND OF SIMULATION.")