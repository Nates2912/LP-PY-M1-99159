import os
os.system ("cls")

#criando a funçao
def logo_senai():
    os.system ("cls")
    print("=========")
    print("==SENAI==")
    print("=========")

logo_senai()
name = input("Type in your name: ")

logo_senai()
age = int(input("Type in your age: "))

logo_senai()
weight = float(input("Type in your weight: "))

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Weight: {weight}")
