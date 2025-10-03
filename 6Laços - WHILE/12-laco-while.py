# Foi feita uma pesquisa entre os habitantes de uma região.  Foram coletados os dados de idade, sexo (M/F) e salário. 
# Faça um algoritmo que informe:  
# a) a média de salário do grupo;
# b) maior e menor idade do grupo
# c) quantidade de mulheres com salário a partir de R$ 5.000,00.
# Crie um menu com três opções.
# Código |   Descrição
#        1        |   Adicionar pessoa

#        2       |   Exibir resultados

#        3       |   Sair
# O final da leitura de dados se dará com quando o usuário digitar o número código 3. 

import os 
os. system ("cls")

menida = 9999
marida =0
somasal = 0
quantsal = 0
mulher5k = 0


while True:
    os.system ("cls")
    print("""
Code \t Description           
   1 \t Add someone          
   2 \t Show results    
   3 \t Exit    
   
""")

    opt =  int(input("Type the chosen option: "))
    match opt:
        case 1:
            ida = int(input("Type in your age: "))
            gen = input ("Type in your gender, M or F: ").upper()
            sal = float(input("Type in your salary: "))

            #media d salario
            quantsal += 1
            somasal += sal

            #idade
            if ida < menida :
                menida = ida
            if ida > menida:
                marida = ida

            #quant de mulheres com salario >= 5k
            if sal >= 5000 and gen == "F":
                mulher5k += 1

        case 2:
            mediasal = somasal /quantsal if quantsal != 0 else 0
            if menida ==  9999:
                menida = 0    
            print("\n=Showing results=")
            print(f"Average group salary: {mediasal}")
            print(f"Youngest: {menida}")
            print(f"Oldest: {marida}")
            print(f"Women that get paid more than 5k: {mulher5k}")
            input("Press enter to continue...")
                
        case 3:
            print ("Logging out...")
            break
        case _:
            print ("Invalid. try again")
            input("Press enter to continue...")










