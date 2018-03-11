"""
Programa para realizar os calculos da atividade laboratoriais de Física do Secundário
"""
from sys import exit as end
Sim_expressions = ["Yes", "Y", "y", "yes", "Sim", "sim", "S", "s", "YES", "SIM"]
Nao_expressions = ["No", "no", "N", "n", "NO", "Não", "não", "NÃO", "Nao", "nao", "nao"]
#Welcome
run_program = input("Bem Vindo às atividades laboratoriais de Física do secundário!\nEste programa destina-se a auxiliar-te nas atividades experimentais de 10º, 11º e 12º, contendo informação importante relativa às mesmas, nomeadamente considerações, aproximações e cálculos das mesmas.\n\nVamos começar?\n:")
if run_program in Sim_expressions:
    print("Ótimo!\nVamos começar.")
elif run_program in Nao_expressions:
    end()
else:
    print("O que inseriu não é válido.")

#Escolher ano
while True:
    ano = input("Qual é o ano da atividade experimental que quer realizar?\n:")
    if ano == "10" or ano == "10º" or ano == "décimo"  or ano == "decimo" or ano == "dez":
        while True:
            ano_verificar = input("É este o ano que deseja utilizar (" + ano + ")?\n:")
            if ano_verificar in Sim_expressions:
                print("A iniciar 10º ano...")
            elif ano_verificar in Nao_expressions:
                break
            else:
                print("O que introduziu não é válido.")
    elif ano == "11" or ano == "11º" or ano == "décimo primeiro"  or ano == "decimo primeiro" or ano == "onze":
        while True:
            ano_verificar = input("É este o ano que deseja utilizar (" + ano + ")?\n:")
            if ano_verificar in Sim_expressions:
                print("A iniciar 11º ano...")
            elif ano_verificar in Nao_expressions:
                break
            else:
                print("O que introduziu não é válido.")
    elif ano == "12" or ano == "12º" or ano == "décimo segundo"  or ano == "decimo segundo" or ano == "doze":
        while True:
            ano_verificar = input("É este o ano que deseja utilizar (" + ano + ")?\n:")
            if ano_verificar in Sim_expressions:
                print("A iniciar 12º ano...")
            elif ano_verificar in Nao_expressions:
                break
            else:
                print("O que introduziu não é válido.")
    elif ano == "exit" or ano == "sair" or ano == "break" or ano == "end" or ano == "fim":
        end()
    else:
        print("O que inseriu não é válido.")