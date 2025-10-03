#Cleaning the terminal

import os
os.system("cls")


gender= input ("M for male. F for female: ") .upper()
alt = float(input("What's your height?  "))


match alt:

    case "M":
        Mpeso =  72.7 * alt - 58
    case "F":
        Fpeso =  62.1 * alt - 44.7
    case _: "Invalid"

print("Your ideal height is: {alt}")