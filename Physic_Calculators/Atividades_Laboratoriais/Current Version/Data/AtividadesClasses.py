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

class LaboratoryActivities:
    #def __init__(self, discipline, year, name, code, pdfInfo, help, id):
    def __init__(self, discipline, year, name, code, info, help, description, material, procedure):
        self.discipline = discipline
        self.year = year
        self.name = name
        self.code = code
        self.info = info
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

class Physics(LaboratoryActivities):
    def __init__(self, year, name, code, info, help, description, material, procedure):
        LaboratoryActivities.__init__(self, "Fisica", year, name, code, info, help, description, material, procedure)


class Tenth(Physics):
    def __init__(self, name, code, info, help, description, material, procedure):
        Physics.__init__(self, "10", name, code, info, help, description, material, procedure)

class Eleventh(Physics):
    def __init__(self, name, code, info, help, description, material, procedure):
        Physics.__init__(self, "11", name, code, info, help, description, material, procedure)

class Twelfth(Physics):
    def __init__(self, name, code, info, help, description, material, procedure):
        Physics.__init__(self, "12", name, code, info, help, description, material, procedure)

ex = Tenth("name", "code", "info", "help", "des", "mater", "proc")

print("dis", ex.discipline)
print("y", ex.year)
print("name", ex.name)
print("code", ex.code)
print("info", ex.info)
print("help", ex.help)
print("des", ex.description)
print("mater", ex.material)
print("proc", ex.procedure)
print("id", ex.id)


#check if variable == object.id