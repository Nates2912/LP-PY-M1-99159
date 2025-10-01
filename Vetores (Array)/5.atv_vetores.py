import os
os.system ("cls")

#como cria um vetor (lista)
lista_notas = []

#inserindo elas
for i in range (6):
    n1 = int(input(f"Input the {i+1}º grade: "))
    lista_notas.append(n1)

for i in range (6):
     print(f"\nGrade: {lista_notas[i]}")

print(f"\nBigger Number: {max(lista_notas)}")
print(f"\nSmaller Number: {min(lista_notas)}")


print("\nEND OF SIMULATION.")
