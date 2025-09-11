#Terminal clean
import os
os.system("cls")

#Stuff so the client is able to type lol

n1= int (input("Type in the first number: "))
print("")
n2=int (input("Type in the second number: "))
print("")

soma = n1 + n2

produto = n1 * n2

media= soma/2

if soma > produto:
    maior = n1
    menor = n2
else:
    maior = n1
    menor = n2

    print (f"Sum: {soma}")
    print (f"Product: {produto}")
    print (f"Bigger number: {maior}")
    print (f"Smaller number: {menor}")
    print("")

if n1 == n2:
    print ("The user typed the same numbers, how humorous.")

    
    
    



    