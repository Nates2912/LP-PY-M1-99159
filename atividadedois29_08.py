#Cleaning the terminal

#USANDO OR (OU)

import os 
os.system("cls")

nota= int (input("Type in the first number: "))
print("")

#Se nota menor que zero ou maior que dez
if nota < 0 or nota > 10:
    print("Invalid input.")
else:
    print (f"Grade: {nota}")