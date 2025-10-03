#Cleaning the terminal

import os
os.system("cls")

#entrace

quant_maca = int(input("Cart: "))

print ("")

#process

if quant_maca >= 12: 
    print(f"You bought {quant_maca} apples.")
    valor_total = quant_maca * 1.00
else: 
    print(f"You bought {quant_maca} apples.")
    valor_total = quant_maca * 1.30

#exit

print ("")

print(f"\n Your total is: {valor_total:.2f}")