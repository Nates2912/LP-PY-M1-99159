#crie um programa que solicite o usuario e o login, se tiver errado ele vai pedir denovo, se passar de 3, ele para

import os
os.system("cls")

pas = "1"
log = "1"

while True:
    for i in range(3):
            User = input("User: ")
            Password = input("Password:")

            if User == log and Password == pas:
                print ("Welcome back!")
                break
            else:           
                print("Invalid, try again.")
    break
            
    
        