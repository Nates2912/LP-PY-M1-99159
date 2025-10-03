# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados
# sobre o salário e número de filhos das famílias da cidade. A prefeitura deseja saber:  
# a) total de famílias que responderam a pesquisa;
# b) média do salário da população;
# c) média do número de filhos;
# d) maior salário;
# e) menor salário.
# Crie um menu com duas opções.
# Código |   Descrição
#      1         |   Adicionar família
#      2        |   Sair e exibir resultados
# O final da leitura de dados se dará com quando o usuário digitar o número código 2. 

import os 
os. system ("cls")

menosal = 0
maiosal = 0
quantsal = 0
quantkid = 0

while True:
    os.system ("cls")
    print("""
Code \t Description           
   1 \t Add Family          
   2 \t Show results and exit    
""")

    opt =  int(input("Type the chosen option: "))
    match opt:
        case 1:

            kid = input ("Type in your gender, M or F: ").upper()
            sal = float(input("Type in your salary: "))

        #media quantidade d filhos

            quantkid += 1
            somakid += kid

        #media d salario
            quantsal += 1
            somasal += sal

        #calculo menor ou maior salario
            if sal < menosal :
                menosal = sal
            if sal > maiosal:
                maiosal = sal

        

        

