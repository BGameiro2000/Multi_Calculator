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

#==========
# Version
#==========
verAtvLab = ""

#==========
# Classes
#==========
class LaboratoryActivities: #main class
    #==========
    # Attributes
    #==========
    def __init__(self, discipline, year, code, name, pdfInfo, help):
        self.discipline = discipline
        self.year = year
        self.code = code
        self.name = name
        self.pdfInfo = pdfInfo
        self.help = help
        self.id = "%s %sºAno AL%s" % (discipline, year, code)

#==========
# Disciplines
#==========
class Physics(LaboratoryActivities): #child of main class, defines the discipline
    discipline = "Física"
    #==========
    # Attributes (discipline --> Física)
    #==========
    def __init__(self, year, code, name, pdfInfo, help):
        LaboratoryActivities.__init__(self, Physics.discipline, year, code, name, pdfInfo, help)

    #==========
    # Constants SI
    #==========
    g = 10 #m/(s**2)

"""
class Chemistry(LaboratoryActivities): #child of main class, defines the discipline
    #==========
    # Attributes (discipline --> Química)
    #==========
    def __init__(self, year, code, name, pdfInfo, help):
        LaboratoryActivities.__init__(self, "Química", year, code, name, pdfInfo, help)

    #==========
    # Constants SI
    #==========
    NA = 6.022*10**23 #1/mol
"""

#==========
# Years
#==========
class PhysicsTenth(Physics): #child of Physics subclass, defines the year
    year = "10"
    #==========
    # Attributes (year --> 10)
    #==========
    def __init__(self, code, name, pdfInfo, help):
        Physics.__init__(self, PhysicsTenth.year, code, name, pdfInfo, help)

class PhysicsEleventh(Physics): #child of Physics subclass, defines the year
    year = "11"
    #==========
    # Attributes (year --> 11)
    #==========
    def __init__(self, code, name, pdfInfo, help):
        Physics.__init__(self, PhysicsEleventh.year, code, name, pdfInfo, help)

class PhysicsTwelfth(Physics): #child of Physics subclass, defines the year
    year = "12"
    #==========
    # Attributes (year --> 12)
    #==========
    def __init__(self, code, name, pdfInfo, help):
        Physics.__init__(self, PhysicsTwelfth.year, code, name, pdfInfo, help)

#==========
# Laboratory Activities
#==========
class F10AL1_1(PhysicsTenth): #child of PhysicsTenth subclass, defines the code and the activity
    #==========
    # Attributes
    #==========
    def __init__(self, name, pdfInfo, help):
        PhysicsTenth.__init__(self, "1.1", name, pdfInfo, help)
        self.name = ""
        self.pdfInfo = r""
        self.help = ""
        def userInputs(x):
            x = input()

"""
#==========
# Tests
#==========
ex0 = Physics("11", "1.1", "name", "pdfinfo", "help")
ex1 = F10AL1_1("name", "pdfinfo", "help")

print("dis", Physics.__init__.discipline)
print("y", Physics.year)
print("code", Physics.code)
print("name", Physics.name)
print("info", Physics.pdfInfo)
print("help", Physics.help)
print("id", Physics.id)


print("dis", ex0.discipline)
print("y", ex0.year)
print("code", ex0.code)
print("name", ex0.name)
print("info", ex0.pdfInfo)
print("help", ex0.help)
print("id", ex0.id)


print("dis", ex1.discipline)
print("y", ex1.year)
print("code", ex1.code)
print("name", ex1.name)
print("info", ex1.pdfInfo)
print("help", ex1.help)
print("id", ex1.id)
"""