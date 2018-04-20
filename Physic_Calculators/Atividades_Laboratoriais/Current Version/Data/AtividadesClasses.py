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
    def __init__(self, discipline, year, code, name, pdfInfo):
        self.discipline = discipline
        self.year = year
        self.code = code
        self.name = name
        self.pdfInfo = pdfInfo
        self.id = "%s %sAno AL%s" % (discipline, year, code)

#==========
# Disciplines
#==========
class Physics(LaboratoryActivities): #child of main class, defines the discipline
    specialAttribute = "Física"
    #==========
    # Attributes (discipline --> Física)
    #==========
    def __init__(self, year, code, name, pdfInfo):
        LaboratoryActivities.__init__(self, self.specialAttribute, year, code, name, pdfInfo)

    #==========
    # Constants SI
    #==========
    g = 10 #m/(s**2)

class Chemistry(LaboratoryActivities): #child of main class, defines the discipline
    specialAttribute = "Química"
    #==========
    # Attributes (discipline --> Química)
    #==========
    def __init__(self, year, code, name, pdfInfo):
        LaboratoryActivities.__init__(self, self.specialAttribute, year, code, name, pdfInfo)

    #==========
    # Constants SI
    #==========
    NA = 6.022*10**23 #1/mol

#==========
# Years
#==========
class PhysicsTenth(Physics): #child of Physics subclass, defines the year
    specialAttribute = "10º"
    #==========
    # Attributes (year --> 10)
    #==========
    def __init__(self, code, name, pdfInfo):
        Physics.__init__(self, self.specialAttribute, code, name, pdfInfo)

class PhysicsEleventh(Physics): #child of Physics subclass, defines the year
    specialAttribute = "11º"
    #==========
    # Attributes (year --> 11)
    #==========
    def __init__(self, code, name, pdfInfo):
        Physics.__init__(self, self.specialAttribute, code, name, pdfInfo)

class PhysicsTwelfth(Physics): #child of Physics subclass, defines the year
    specialAttribute = "12º"
    #==========
    # Attributes (year --> 12)
    #==========
    def __init__(self, code, name, pdfInfo):
        Physics.__init__(self, self.specialAttribute, code, name, pdfInfo)

class ChemistryTenth(Chemistry): #child of Chemistry subclass, defines the year
    specialAttribute = "10º"
    #==========
    # Attributes (year --> 10)
    #==========
    def __init__(self, code, name, pdfInfo):
        Chemistry.__init__(self, self.specialAttribute, code, name, pdfInfo)

class ChemistryEleventh(Chemistry): #child of Chemistry subclass, defines the year
    specialAttribute = "11º"
    #==========
    # Attributes (year --> 11)
    #==========
    def __init__(self, code, name, pdfInfo):
        Chemistry.__init__(self, self.specialAttribute, code, name, pdfInfo)

class ChemistryTwelfth(Chemistry): #child of Chemistry subclass, defines the year
    specialAttribute = "12º"
    #==========
    # Attributes (year --> 12)
    #==========
    def __init__(self, code, name, pdfInfo):
        Chemistry.__init__(self, self.specialAttribute, code, name, pdfInfo)

#==========
# Laboratory Activities
#==========
class F10AL1_1(PhysicsTenth): #child of PhysicsTenth subclass, defines the code and the activity
    specialAttribute = "1.1"
    name = "Movimento num plano inclinado:\nvariação da energia cinética e distância percorrida"
    pdfInfo = r""
    #==========
    # Attributes (code --> 1.1)
    #==========
    def __init__(self, name, pdfInfo):
        PhysicsTenth.__init__(self, self.specialAttribute, self.name, self.pdfInfo)
    
    PhysicalQuantitiesVar = ["m", "d", "l", "Δt"]
    PhysicalQuantitiesValues = ["Massa do carrinho", "Distância dp carrinho à célula fotovoltaica", "Largura da faixa do carrinho", "Intervao de tempo que a célula foi interrompida"]
    PhysicalQuantitiesExp = []

    PhysicalQuantitiesValuesDic = [dict([(var, val)]) for var, val in zip(PhysicalQuantitiesVar, PhysicalQuantitiesValues)]
    PhysicalQuantitiesExpDic = [dict([(var, exp)]) for var, exp in zip(PhysicalQuantitiesVar, PhysicalQuantitiesExp)]

    def doActivity(self, m=None, d=None, l=None, Δt=None):
        v = l / Δt
        Ec = (0.5) * m * (v**2)