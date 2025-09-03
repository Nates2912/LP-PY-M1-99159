import os 
os. system ("cls")

print("""
Code \t Meal           Cost
   1 \t Steak          R$25,00
   2 \t Lasagna        R$20,00
   3 \t Strogonoff     R$18,00
   4 \t Steak + Onions R$15,00
   3 \t Egg Sandwich   R$5,00
""")

codigo = input("Choose your meal: ")

match codigo:
    case "1":
        print("Picanha Steak: 25R$")
    case "2":
        print("Lasagna: 20R$")
    case "3":
        print("Strogonoff: 18R$")
    case "4":
        print("Steak with Onions: 15R$")
    case "5":
        print("Egg Sandwich: 5R$")
    case _:
        print("Invalid Answer")



