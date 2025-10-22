# import os

# os.system("cls")

# #lista 
# lista_notas = []

# # função sem parametros (parentesis) e sem retorno
# def limpa_tela():
#     os.system("cls")

# #funcao com parametros (parentesis) e com retorno
# def calcular_media (avr, soma):
#     soma = sum(lista_notas)
#     avr = soma / 3
#     return (avr)


# #funçao com parametros e sem retorno
# def mostrar_notas(notas):
#     print(f"Grades: {notas}")

# # chamando a funçao
# limpa_tela()
# for i in range (3):
#     nota = int(input(f"Input the {i+1}º grade: "))
#     lista_notas.append(nota)

# #funcao com parametros (parentesis) e com retorno
# notas = calcular_media(nota)
# #funçao com parametros e sem retorno
# mostrar_notas(notas)


import os

os.system("cls")

# lista 
lista_notas = []
 
def calcular_media(lista_notas):
   resultado = sum(lista_notas) / 3
   return resultado

for i in range (3):
   nota = float(input(f"Input the {i+1}º grade: "))
   lista_notas.append(nota)

media = calcular_media(lista_notas)

print (f"Média: {media:.2}")