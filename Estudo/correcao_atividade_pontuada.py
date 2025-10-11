#slr = salario
import os
os.system("cls")

#contas e entradas de informacao eu acho
def limpa_tela():
    os.system("cls")        

def calcular_inss (slr):
        if slr > 1.518:
            desconto_inss = slr * 0.075
        elif  slr >= 1.518 and slr <= 2.792:
            desconto_inss = slr * 0.09
        elif  slr >= 2.793 and slr <= 4.189:
            desconto_inss = slr * 0.012
        elif  slr >= 4.190 and slr <= 8.157:
            desconto_inss = slr * 0.014
        return  desconto_inss


def calcular_irrf(slr):
    if slr <= 2428:
        desconto_irrf = 0
    elif slr <= 2825:
        desconto_irrf = slr * 0.075
    elif slr <= 3750:
        desconto_irrf = slr * 0.15
    elif slr >= 3751.06:
        desconto_irrf = slr * 0.225
    elif slr >= 4664.68:
        desconto_irrf = slr * 0.275
    return desconto_irrf


    

def calcular_refeicao (refeicao):
    desconto2 = refeicao * 0.20
    return desconto2

def calcular_transporte (transporte, slr):
    if  transporte == "S":
            transporte = slr * 0.06
    else:
        transporte = 0
    return transporte

def calcular_plano_saude (dependentes):
    if dependentes == "S":
        plano_saude = qtd_dependente * 150.00
    else:
        plano_saude = 0
    return plano_saude


def soma_desconto(calcular_inss, calcular_irrf , calcular_transporte, calcular_refeicao, calcular_plano_saude):
    desconto_final = calcular_inss + calcular_irrf + calcular_transporte + calcular_refeicao + calcular_plano_saude
    return desconto_final


def resultados(salario_bruto, desconto_final):
    salario_real = salario_bruto - desconto_final
    print(f"Salário: {salario:.2f}")
    print(f"Dependentes: {dependentes}")
    print(f"Vale transporte: {vale_transporte}")
    print(f"Vale refeição: {vale_refeicao}")
    print(f"O salário liquido após os descontos e acréscimos será: {salario_real:.2f}")

#perguntas

user_resposta = "0604"
senha_resposta = "1234"


while True:
    user = input("user: ")
    senha = input("Senha:")

    if user == user_resposta and senha == senha_resposta:
        limpa_tela()
        print ("Seja bem vindo(a)!")
        salario = float(input("Seu salário: "))
        vale_refeicao = float(input("Quanto custa o vale refeição?: "))
        vale_transporte = input("Usa vale transporte? (Use S ou N):").upper()
        dependentes = input("Tem dependentes?: ").upper()
        if dependentes == "S":
            qtd_dependente = int(input("Quantos?: "))
        break
    else:
        print("Inválido, tente denovo.")
        

limpa_tela()

#chamano a funcao

a = calcular_inss(salario)
b = calcular_irrf(salario)
c = calcular_transporte(salario, vale_transporte)
d = calcular_refeicao(vale_refeicao)
e = calcular_plano_saude(dependentes)
f = soma_desconto(a,b,c,d,e)
resultados(salario,f)