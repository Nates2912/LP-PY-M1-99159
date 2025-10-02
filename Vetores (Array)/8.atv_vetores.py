import os
os.system ("cls")

#como cria um vetor (lista)
lista_num = []
soma_positivo = 0
quant_negativo = 0
soma = 0
#inserindo elas
for i in range (3):
    num1 = int(input(f"Type the {i+1}º number: "))
    lista_num.append(num1)

    if num1 > 0:
        soma_positivo += num1
    elif num1 < 0:
        quant_negativo += 1

for num1 in lista_num:
    print(f"Number: {num1}")

print(f"Sum of the positive numbers: {soma_positivo}")
print(f"Quantity of negative numbers: {quant_negativo}")


        

