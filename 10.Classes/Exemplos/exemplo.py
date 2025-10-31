import os
os.system("cls")

#exemplo - texto que desejo salvar
texto = "Senai"


#definir nome do arquivo para salvar
nome_arquivo = "exemplo.txt"

#comandos para salvar
with open(nome_arquivo, "w") as meu_arquivo:
    meu_arquivo.write(texto) 
    print("Salvo com sucesso!")
