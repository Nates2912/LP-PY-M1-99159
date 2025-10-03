#Limpeza de terminal
import os
os.system("cls")

number=int(input("Type a number: "))

if number < 10:
    print("Smaller than 10!")

elif number == 10:
    print("It's 10!")

elif number > 10:
    print("Bigger than 10!")


