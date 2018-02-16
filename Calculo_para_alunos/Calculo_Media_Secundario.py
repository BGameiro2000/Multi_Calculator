"""
Calculadora da média do secundário para alunos de ciências e tecnologias do ensino oficial em Portugal.
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
"""
Menu
"""
nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("Bem vindo à calculadora de médias!\n\n")
curso = input("É aluno de ciências e tecnologias do ensino oficial em Portugal?\n:")
if curso in Nao_expressions:
    tchau("Desculpe, mas o seu curso não está disponível atualmente.\nPor favor tente noutra altura.")
elif curso in Sim_expressions:
    nao_tenho_impressora_mas_se_tivesse_era_isto_que_fazia("por editar")
else:
    tchau("O que intruduziu não é válido.")