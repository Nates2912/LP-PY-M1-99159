#Limpando terminal
import os 
os.system("cls")

idade  = int (input("Type your age: "))

if idade >= 18 and idade < 65:
    print("Obrigatory vote.")

else: 
    print("Not obligated to vote.")