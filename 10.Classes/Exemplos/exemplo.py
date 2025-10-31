import os
os.system("cls")

#exemplo - texto que desejo salvar
texto = input("Nome: ")


#definir nome do arquivo para salvar
nome_arquivo = "exemplo.txt"

#comandos para salvar
# with open(nome_arquivo, "w") as meu_arquivo: # apaga o que foi salvo anteriormente e troca pelo texto atual
with open(nome_arquivo, "a") as meu_arquivo: # O "a" adiciona e e nao apaga o antigo
    meu_arquivo.write(f"{texto}\n") 
    print("Salvo com sucesso!")
