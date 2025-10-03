import os
os.system ("cls")

#como cria um vetor (lista)
lista_notas = []

pares = 0 #Para definir 0
impares = 0 #Para definir 0
#inserindo elas
for i in range (6):
    n1 = int(input(f"Input the {i+1}º number: "))
    lista_notas.append(n1)

    if n1 % 2 == 0:
        pares = pares + 1 
    else:
        impares = impares + 1

for i in range (6):
    print(f"\nGrade: {lista_notas[i]}")

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")

print("\nEND OF SIMULATION.")
