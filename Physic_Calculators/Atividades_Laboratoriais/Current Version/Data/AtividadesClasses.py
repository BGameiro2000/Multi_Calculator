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
# Units
#==========
massDic = {"Gg": 10**6, "Mg": 10**3, "Kg": 1, "hg": 0.1, "dag": 0.1**2, "g": 0.1**3, "dg": 0.1**4, "cg": 0.1**5, "mg": 0.1**6}
disDic = {"Gm": 10**9, "Mm": 10**6, "km": 10**3, "hm": 10**2, "dam": 10, "m":1, "dm": 0.1, "cm": 0.1**2, "mm": 0.1**3, "µm":0.1**6, "nm":0.1**6}
timeDic = {"Gs": 10**9, "Ms": 10**6, "ks": 10**3, "hs": 10**2, "das": 10, "s":1, "ds": 0.1, "cs": 0.1**2, "ms": 0.1**3, "µs":0.1**6, "ns":0.1**6}
velDic = {"Gm/s": 10**9, "Mm/s": 10**6, "km/s": 10**3, "hm/s": 10**2, "dam/s": 10, "m/s":1, "dm/s": 0.1, "cm/s": 0.1**2, "mm/s": 0.1**3, "µm/s":0.1**6, "nm/s":0.1**6}
enerDic = {"GJ": 10**9, "MJ": 10**6, "kJ": 10**3, "hJ": 10**2, "daJ": 10, "J":1, "dJ": 0.1, "cJ": 0.1**2, "mJ": 0.1**3, "µJ":0.1**6, "nJ":0.1**6}

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
    #            (name & pdfInfo)
    #==========
    def __init__(self):
        PhysicsTenth.__init__(self, self.specialAttribute, self.name, self.pdfInfo)
    
    #==========
    # Variables
    #==========
    # Data lists
    PhysicalQuantitiesVar = ["m", "d", "l", "Δt"]
    PhysicalQuantitiesExp = ["Massa do carrinho", "Distância do carrinho à célula fotovoltaica", "Largura da faixa do carrinho", "Intervalo de tempo que a célula foi interrompida"]
    PhysicalQuantitiesUnits = [massDic, disDic, disDic, timeDic]
    PhysicalQuantitiesValues = []
    # Data dictionairies
    PhysicalQuantitiesExpDic = {var: exp for var, exp in zip(PhysicalQuantitiesVar, PhysicalQuantitiesExp)}
    PhysicalQuantitiesUnitsDic = {var: un for var, un in zip(PhysicalQuantitiesVar, PhysicalQuantitiesUnits)}
    PhysicalQuantitiesValuesDic = {var: val for var, val in zip(PhysicalQuantitiesVar, PhysicalQuantitiesValues)}
    # Results lists
    AnsVar = ["v", "Ec"]
    AnsExp = ["Velocidade", "Energia cinética"]
    AnsUnits = [velDic, enerDic]
    # Results dictionairies
    AnsExpDic = {var: exp for var, exp in zip(AnsVar, AnsExp)}
    AnsUnitsDic = {var: un for var, un in zip(AnsVar, AnsUnits)}

    def doActivity(self, m=None, d=None, l=None, Δt=None):
        v = l / Δt
        Ec = (0.5) * m * (v**2)