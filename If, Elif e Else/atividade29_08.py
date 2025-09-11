#Cleaning the terminal

#USANDO AND (E)

import os 
os.system("cls")

nota= int (input("Type in the first number: "))
print("")

#Se nota maior que zero ou menor que dez
#AND -> Dentro do intervalo definido
if nota > 0 or nota < 10:
    print("Invalid input.")
else:
    print (f"Grade: {nota} Grade: {nota}")
