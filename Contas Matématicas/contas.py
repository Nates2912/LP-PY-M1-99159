
#Faça um programa que peça dois números e imprima as 4 contas
  

#Para limpar o terminal
import os
os.system("cls")

#imput do usuario
numero1 = float (input("Digite um numero: "))
print("")
numero2 = float (input("Digite um numero: "))
print("")

#como as contas funcionam
soma = numero1+numero2
subtracao = numero1-numero2
multiplicacao = numero1*numero2
divisao = numero1/numero2

#resultados
print(f"Soma: {soma}")
print("")
print(f"Subtração: {subtracao}")
print("")
print(f"Multiplicação: {multiplicacao}")
print("")
print(f"Divisão: {divisao}")