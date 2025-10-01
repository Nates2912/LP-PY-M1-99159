import os
os.system ("cls")

soma = 0

for i in range (3):
    nota = int(input(f"Input the {i+1}º grade: "))
    soma += nota


print(f"\nGrade: {nota}")
print(f"\nSum: {soma}")

print("\nEND OF SIMULATION.")