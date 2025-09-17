# Escrever um programa de computador que solicite do usuário 3 notas 
# ao final, apresente a média e mostre para o usuário se o aluno está aprovado, em recuperação ou reprovado. 

import os
os.system("cls")

soma = 0
avr = 0 #para soma  defaultar como 0 no começo

n1 = input(f"Type in the 1º grade: ", min_value= 0, max_value= 10)
n2 = input(f"Type in the 2º grade: ", min_value= 0, max_value= 10)
n3 = input(f"Type in the 3º grade: ", min_value= 0, max_value= 10)

soma = n1 + n2 + n3

avr = soma/3


while True:
        if n1 <0 and n1 >10:
            print("invalid")
                if avr >=7:
                        print (f"The average is: {avr:.1f}")
                        print ("Good job! approved!")
                elif avr >=5 and avr <6.9 :
                        print (f"The average is: {avr:.1f}")
                        print ("Caution, you might not get approved...")
                elif avr <5:
                        print(f"The average is: {avr:.1f}")
                        print ("Not approved. Will have to repeat the year.")
                
                else:
                        print("Input a number.")