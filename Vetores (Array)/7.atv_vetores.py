import os 
os. system ("cls")

lista_preco = []
lista_pratos = []


while True:
    opcao = int(input(""" 
    Code \t Meal           Cost
    1 \t Steak          R$25,00
    2 \t Lasagna        R$20,00
    3 \t Strogonoff     R$18,00
    4 \t Steak + Onions R$15,00
    5 \t Egg Sandwich   R$5,00
                       
    Input in the desired meal: """))

    match opcao:
        case 1:
                prato = "Picanha Steak"
                preco = 25
        case 2:
                prato ="Lasagna"
                preco =20
        case 3:
                prato = "Strogonoff"
                preco = 18
        case 4:
                prato = "Steak with Onions"
                preco = 15
        case 5:
                prato = "Egg Sandwich"
                preco = 5
        case _:
                print ("Invalid Answer. \n Try again. \n")

    if opcao >= 1 and opcao <= 5:
        lista_pratos.append(prato)
        lista_preco.append(preco)

    resposta = input("Anything else? (Use Y or N):").upper()
    if resposta == "N":
        break
    os. system ("cls")

if sum(lista_preco) == 0:
    print("No meal was chosen.")
else: 
    print("=CHOSEN MEALS=")
    #for each
    for prato in lista_pratos:
        print(f"Prato: {prato}")

print(f"Total: R$ {sum(lista_preco):.2f}")
