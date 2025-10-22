import os

os.system("cls")

def calcular_imc(pes,alt):
   return pes / (alt** 2)

def resultado(imc):
   print(f"Seu IMC é: {imc:.2f}")

peso = float(input("Seu peso (Kg): "))
altura = float(input("Sua altura (M): "))

resultado(calcular_imc(peso,altura))
