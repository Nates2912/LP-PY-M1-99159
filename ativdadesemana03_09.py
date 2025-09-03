import os 
os. system ("cls")

dia = input("What day is it?")

match dia:
    case "1":
        "Sunday"
    case "2":
        "Monday "
    case "3":
        "Tuesday"
    case "4":
        "Wednesday"
    case "5":
        "Thursday"
    case "6":
        "Friday"
    case"7":
        "Saturday"
    case _:
        "Invalid Answer"

print (dia)
