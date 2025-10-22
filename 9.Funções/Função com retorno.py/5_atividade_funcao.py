import os
import time
os.system ("cls")

lista_notas = []

def calcular_media(lista_notas):
   resultado = sum(lista_notas) / 2
   return resultado

def resultado_final(media):
    if media <= 7:
        print("Approved")
    else:
        print("Failed") 

for i in range (2):
    while True:
        notas = int(input(f"Type the {i+1}º grade: "))
        if notas >= 0 and notas <= 10:
            lista_notas.append(notas)
            break
        else:
            print("Wrong. Try again...")
            time.sleep(2)
           
       
media = calcular_media(lista_notas)

print(f"Average: {media}")
resultado_final(media)

