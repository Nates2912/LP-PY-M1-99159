#Terminal clean
import os
os.system("cls")

#Start

name = ("Type your name: ")
print("")
n1= float (input("Type in the first number: "))

print("")
n2= float (input("Type in the second number: "))
print("")

media= (n1+n2) /2

if media >= 9:
    conceito = "A"

elif media >= 7.5:
    conceito = "B"

elif media >= 6:
    conceito = "C"

elif media >= 4:
    conceito = "D"

else: 
    conceito = "E"

if media > 6:
    resultado = "Approved"
else: 
     resultado = "Not Approved"

print(f"\nAverage: {media}")
print(f"Grade: {conceito}")
print(f"Results: {resultado}")