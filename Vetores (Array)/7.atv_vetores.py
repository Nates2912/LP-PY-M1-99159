import os 
os. system ("cls")

lista_preco = []
lista_pratos = []
totalprice = 0

while True:
    print(""" 
    Code \t Meal           Cost
    1 \t Steak          R$25,00
    2 \t Lasagna        R$20,00
    3 \t Strogonoff     R$18,00
    4 \t Steak + Onions R$15,00
    5 \t Egg Sandwich   R$5,00
    """)

    codigo = input("Choose your meal: ")
    
    match codigo:
        case "1":
                prato = "Picanha Steak"
                preco = 25
        case "2":
                prato ="Lasagna"
                preco =20
        case "3":
                prato = "Strogonoff"
                preco = 18
        case "4":
                prato = "Steak with Onions"
                preco = 15
        case "5":
                prato = "Egg Sandwich"
                preco = 5
        case _:
                print ("Invalid Answer")
                print ("Try again...")

    totalprice = totalprice + preco

    lista_pratos.append(prato)
    lista_preco.append(preco)

    moreord = input("Anything else? (Use Y or N):").upper()

    if moreord == "N":
           break
    
    os.system("cls")

for prato in lista_pratos:
    print(f"Order: {prato}")

for preco in lista_preco:
    print(f"Price:{preco}")
    
print(f"Total: {totalprice}")
