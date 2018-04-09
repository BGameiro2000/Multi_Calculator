#!/usr/bin/env python3

"""
This code is under Apache License 2.0
Written by B_Gameiro (Bernardo Bernardino Gameiro)
More in 
    SoloLearn: https://www.sololearn.com/Profile/8198571
    GitHub: https://github.com/BGameiro76
    Repl.it: https://repl.it/@B_Gameiro

GUI para as atividades laboratoriais de Física do secundário em Python 3 e Tkinter.
Este ficheiro contém a  informação relativa às diversas atividades laboratoriais.
O projeto será reaslizado apenas com as atividades laboratoriais de Física, mas terá a possibilidade de ser expandido para Química.
"""

verAtvLab = ""

class Disciplinas:
    #def __init__(self, discipline, year, name, code, pdfInfo, help, id):
    def __init__(self, discipline, year, name, code, info, help, description, material, procedure, id):
        self.discipline = discipline
        self.year = year
        self.name = name
        self.code = code
        self.Info = info
        self.help = help
        self.description = description
        self.material = material
        self.procedure = procedure
        self.id = "%s_%sAno_AL%s" % (discipline, year, code)
"""
class Physics(Disciplinas):
    
    def __init_subclass__(self, discipline):
        self.discipline = "Física"

    def constants(self):
        g = 10 #m/(s**2)
"""

class Physics(Disciplinas):
    self.discipline = "Física"

class Tenth(Physics):
    self.year = "10"

class Eleventh(Physics):
    self.year = "11"

class Twelfth(Physics):
    self.year = "12"

Física_10Ano_AL1_1 = Tenth("name", "code", "info", "help", "description", "material", "procedure", "id")

print(Física_10Ano_AL1_1.discipline)

#check if variable == object.id