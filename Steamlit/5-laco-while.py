#crie um programa que solicite o usuario e o login, se tiver errado ele vai pedir denovo

import os
os.system("cls")

pas = "1"
log = "1"

while True:
    User = input("User: ")
    Password = input("Password:")

    if User == log and Password == pas:
        print ("Welcome back!")
        break
    else:
        print("Invalid, try again.")
