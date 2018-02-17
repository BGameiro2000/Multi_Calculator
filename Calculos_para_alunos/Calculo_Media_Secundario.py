"""
Calculadora da média do secundário para alunos do ensino oficial em Portugal.
Mais opções serão disponibilizadas.
More in 
  SoloLearn: https://www.sololearn.com/Profile/8198571
  GitHub: https://github.com/BGameiro76
  Repl.it: https://repl.it/@B_Gameiro
"""
"""
Importar
"""
from sys import exit as tchau
nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia = print
"""
Definir grupos
"""
Sim_expressions = ("Yes", "Y", "y", "yes", "Sim", "sim", "S", "s", "YES", "SIM")
Nao_expressions = ("No", "no", "N", "n", "NO", "Não", "não", "NÃO", "Nao", "nao", "nao")
Expressions_1 = ("1", "(1)")
Expressions_2 = ("2", "(2)")
Expressions_3 = ("3", "(3)")
"""
Menu
"""
nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("Bem vindo à calculadora de médias!\n\n")
ter_curso = input("É aluno do ensino oficial em Portugal?\n:")
while True:
    if ter_curso in Nao_expressions:
        tchau("Desculpe, mas o seu curso não está disponível atualmente.\nPor favor tente noutra altura.")
    elif ter_curso in Sim_expressions:
        nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("\n")
        break
    else:
        print("O que intruduziu não é válido.\n")
        ter_curso = input("É aluno do ensino oficial em Portugal?\n:")
"""
Curso:
"""
nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("Curso:\n(1) Ciências e tecnologias\n(2) Ciências Socioeconómicas\n(3) Outro")
input_curso = input(":")
while True:
    if input_curso in Expressions_1:
        escolha_curso = "Ciências e tecnologias"
        break
    elif input_curso in Expressions_2:
        escolha_curso = "Ciências socioeconómicas"
        break
    elif input_curso in Expressions_3:
        print("O calculo da média para o seu curso não é possível de momento.\n")
        input_curso = input(":")
    else:
        print("O que intruduziu não é válido.\n")
        input_curso = input(":")
"""
Disciplinas:
"""

"""
Escolha as suas disciplinas.\n\n\n10ª e 11º\n\nPortuguês\n\nFilosofia\n\nMatemática A\n\n
nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("Escolha bianual:\n(1) Matemática A\n(2) História A\n(3) Geografia A")
input_bianual
"""