#!/usr/bin/env python3
"""
This code is under Apache License 2.0
Written by B_Gameiro (Bernardo Bernardino Gameiro)
More in 
  SoloLearn: https://www.sololearn.com/Profile/8198571
  GitHub: https://github.com/BGameiro76
  Repl.it: https://repl.it/@B_Gameiro
  
Programa para realizar os calculos da atividade laboratoriais de Física do Secundário
"""
from sys import exit as end
Sim_expressions = ["Yes", "Y", "y", "yes", "Sim", "sim", "S", "s", "YES", "SIM"]
Nao_expressions = ["No", "no", "N", "n", "NO", "Não", "não", "NÃO", "Nao", "nao", "nao"]
#Welcome
run_program = input("\n\n\n\n\nBem Vindo às atividades laboratoriais de Física do secundário!\nEste programa destina-se a auxiliar-te nas atividades experimentais de 10º, 11º e 12º ano do secundário.\n\nEste programa contem informação importante relativa com as mesmas.\nNomeadamente considerações, aproximações, cálculos, esquemas e objetivos das mesmas.\n\nApenas tens de inserir a informação necessária sempre que vires um dos seguntes sinais: \"𠂭 \" ou \"=\" ou \"☢ \" ou \"⋙ \" ou \"⫸ \"\n\n\nVamos começar?\n𠂭 ")
if run_program in Sim_expressions:
    print("\nÓtimo!\nVamos começar.\n")
elif run_program in Nao_expressions:
    end()
else:
    print("O que inseriu não é válido.")

#Ativiadades
def atividade10(x, y):
    x = atividade#atividades laboratoriais (A.L.*.*)
    y = funcao#o que fazer com a atividade (resumo/explicação, considerações, cálculos, objetivos)

def atividade11(x, y):
    x = atividade#atividades laboratoriais (A.L.*.*)
    y = funcao#o que fazer com a atividade (resumo/explicação, considerações, cálculos, objetivos)

def atividade12(x, y):
    x = atividade#atividades laboratoriais (A.L.*.*)
    y = funcao#o que fazer com a atividade (resumo/explicação, considerações, cálculos, objetivos)

#Escolher ano
while True:
    ano = input("Qual é o ano da atividade experimental que quer realizar?\n𠂭 ")
    if ano == "10" or ano == "10º" or ano == "décimo"  or ano == "decimo" or ano == "dez":
        ano = "10º"
        while True:
            ano_verificar = input("É este o ano que deseja utilizar (" + ano + " ano)?\n𠂭 ")
            if ano_verificar in Sim_expressions:
                print("A iniciar 10º ano...")
            elif ano_verificar in Nao_expressions:
                break
            else:
                print("O que introduziu não é válido.")
    elif ano == "11" or ano == "11º" or ano == "décimo primeiro"  or ano == "decimo primeiro" or ano == "onze":
        ano = "11º"
        while True:
            ano_verificar = input("É este o ano que deseja utilizar (" + ano + " ano)?\n𠂭 ")
            if ano_verificar in Sim_expressions:
                print("A iniciar 11º ano...")
            elif ano_verificar in Nao_expressions:
                break
            else:
                print("O que introduziu não é válido.")
    elif ano == "12" or ano == "12º" or ano == "décimo segundo"  or ano == "decimo segundo" or ano == "doze":
        ano = "12º"
        while True:
            ano_verificar = input("É este o ano que deseja utilizar (" + ano + " ano)?\n𠂭 ")
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