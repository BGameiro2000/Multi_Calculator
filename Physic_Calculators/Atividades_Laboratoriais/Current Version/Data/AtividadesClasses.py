#!/usr/bin/env python3

"""
This code is under Apache License 2.0
Written by B_Gameiro (Bernardo Bernardino Gameiro)
More in 
    SoloLearn: https://www.sololearn.com/Profile/8198571
    GitHub: https://github.com/BGameiro76
    Repl.it: https://repl.it/@B_Gameiro

GUI para as atividades laboratoriais de Física do secundário em Python 3 e Tkinter
Este ficheiro contém a  informação relativa às diversas atividades laboratoriais.
O projrto será reaslizado apenas com as atividades laboratoriais de Física, mas terá a possibilidade de ser expandido para Química.
"""

class Disciplinas:

    def __init__(self, discipline, year, name, code, info, help, description, material, procedure, id):
        self.discipline = discipline
        self.year = year
        self.name = name
        self.code = code
        self.info = info
        self.help = help
        self.description = description
        self.material = material
        self.procedure = procedure
        self.id = "%s_%dAno_AL%s" % (discipline, year, code)

class Phisics(Disciplinas):
        
    self.discipline = "Física"

    def constants():
        g = 10 #m/(s**2)