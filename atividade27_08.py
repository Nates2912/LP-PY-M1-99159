#Cleaning the terminal

import os 
os.system("cls")

age=int(input("Type your age: "))

if age < 16: 
    print("You can't vote!")

elif age > 16 and age < 17:
    print ("Optional vote.")

elif age >= 18 and age < 65:
    print ("Obrigatory vote.")

else:
    print("Not obligated to vote.")