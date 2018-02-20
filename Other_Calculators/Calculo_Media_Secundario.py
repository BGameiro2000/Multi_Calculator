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
Sim_expressions = ["Yes", "Y", "y", "yes", "Sim", "sim", "S", "s", "YES", "SIM"]
Nao_expressions = ["No", "no", "N", "n", "NO", "Não", "não", "NÃO", "Nao", "nao", "nao"]
Expressions_1 = ["1", "(1)", "1)"]
Expressions_2 = ["2", "(2)", "2)"]
Expressions_3 = ["3", "(3)", "3)"]
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
        nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("O que intruduziu não é válido.\n")
        ter_curso = input("É aluno do ensino oficial em Portugal?\n:")
"""
Curso:
"""
nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("Curso:\n\n(1) Ciências e tecnologias\n(2) Ciências Socioeconómicas\n(3) Outro")
input_curso = input(":")
while True:
    if input_curso in Expressions_1:
        escolha_curso = "Ciências e tecnologias"
        break
    elif input_curso in Expressions_2:
        escolha_curso = "Ciências socioeconómicas"
        break
    elif input_curso in Expressions_3:
        nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("\nO calculo da média para o seu curso não é possível de momento.\n\nCurso:\n\n(1) Ciências e tecnologias\n(2) Ciências Socioeconómicas\n(3) Outro")
        input_curso = input(":")
    else:
        nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("O que intruduziu não é válido.\n")
        input_curso = input(":")
"""
Disciplinas:
"""
nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("\n\nEscolha das disciplinas:\n")
escolha_disc_lingua_estrangeira = input("Língua Estrangeira\n:")
if input_curso in Expressions_1:
    escolha_disc_bianual_1_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(1) Biologia e Geologia\n(2) Física e Química A\n(3) Geometria Descritiva A\n:")
    if escolha_disc_bianual_1_input in Expressions_1:
        escolha_disc_bianual_1 = "Biologia e Geologia"
        escolha_disc_bianual_2_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(2) Física e Química A\n(3) Geometria Descritiva A\n:")
        if escolha_disc_bianual_2_input in Expressions_2:
            escolha_disc_bianual_2 = "Física e Química A"
        elif escolha_disc_bianual_2_input in Expressions_3:
            escolha_disc_bianual_2 = "Geometria Descritiva A"
        else:
            nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("O que intruduziu não é válido.")
            escolha_disc_bianual_2_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(2) Física e Química A\n(3) Geometria Descritiva A\n:")
    elif  escolha_disc_bianual_1_input in Expressions_2:
        escolha_disc_bianual_1 = "Física e Química A"
        escolha_disc_bianual_2_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(1) Biologia e Geologia\n(3) Geometria Descritiva A\n:")
        if escolha_disc_bianual_2_input in Expressions_1:
            escolha_disc_bianual_2 = "Biologia e Geologia"
        elif escolha_disc_bianual_2_input in Expressions_3:
            escolha_disc_bianual_2 = "Geometria Descritiva A"
        else:
            nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("O que intruduziu não é válido.")
            escolha_disc_bianual_2_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(1) Biologia e Geologia\n(3) Geometria Descritiva A\n:")
    elif  escolha_disc_bianual_1_input in Expressions_3:
        escolha_disc_bianual_1 = "Física e Química A"
        escolha_disc_bianual_2_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(1) Biologia e Geologia\n(2) Física e Química A\n:")
        if escolha_disc_bianual_2_input in Expressions_1:
            escolha_disc_bianual_2 = "Biologia e Geologia"
        elif escolha_disc_bianual_2_input in Expressions_2:
            escolha_disc_bianual_2 = "Geometria Descritiva A"
        else:
            nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("O que intruduziu não é válido.")
            escolha_disc_bianual_2_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(1) Biologia e Geologia\n(2) Física e Química A\n:")
    else:
        nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("O que intruduziu não é válido.")
        escolha_disc_bianual_1_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(1) Biologia e Geologia\n(2) Física e Química A\n(3) Geometria Descritiva A\n:")
elif input_curso in Expressions_2:
    escolha_disc_bianual_1_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(1) Economia A\n(2) História A\n(3) Geografia A\n:")
    if escolha_disc_bianual_1_input in Expressions_1:
        escolha_disc_bianual_1 = "Economia A"
        escolha_disc_bianual_2_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(2) História A\n(3) Geografia A\n:")
        if escolha_disc_bianual_2_input in Expressions_2:
            escolha_disc_bianual_2 = "História A"
        elif escolha_disc_bianual_2_input in Expressions_3:
            escolha_disc_bianual_2 = "Geografia A"
        else:
            nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("O que intruduziu não é válido.")
            escolha_disc_bianual_2_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(2) História A\n(3) Geografia A\n:")
    elif  escolha_disc_bianual_1_input in Expressions_2:
        escolha_disc_bianual_1 = "História A"
        escolha_disc_bianual_2_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(1) Economia A\n(3) Geografia A\n:")
        if escolha_disc_bianual_2_input in Expressions_1:
            escolha_disc_bianual_2 = "Economia A"
        elif escolha_disc_bianual_2_input in Expressions_3:
            escolha_disc_bianual_2 = "Geografia A"
        else:
            nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("O que intruduziu não é válido.")
            escolha_disc_bianual_2_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(1) Economia A\n(3) Geografia A\n:")
    elif  escolha_disc_bianual_1_input in Expressions_3:
        escolha_disc_bianual_1 = "História A"
        escolha_disc_bianual_2_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(1) Economia A\n(2) História A\n:")
        if escolha_disc_bianual_2_input in Expressions_1:
            escolha_disc_bianual_2 = "Economia A"
        elif escolha_disc_bianual_2_input in Expressions_2:
            escolha_disc_bianual_2 = "Geografia A"
        else:
            nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("O que intruduziu não é válido.")
            escolha_disc_bianual_2_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(1) Economia A\n(2) História A\n:")
    else:
        nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("O que intruduziu não é válido.")
        escolha_disc_bianual_1_input = input("Escolha a sua disciplina bianual (10º e 11º Ano)\n(1) Economia A\n(2) História A\n(3) Geografia A\n:")
else:
    nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("Erro desconhecido.")