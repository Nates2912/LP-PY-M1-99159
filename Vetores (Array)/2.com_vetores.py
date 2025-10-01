import os
os.system ("cls")

#como cria um vetor (lista)
lista_notas = []

#inserindo elas
for i in range (3):
    nota = int(input(f"Input the {i+1}º grade: "))
    lista_notas.append(nota)

soma = sum(lista_notas)

for i in range (3):
     print(f"\nGrade: {lista_notas[i]}")

print(f"\nSum: {soma}")

print("\nEND OF SIMULATION.")