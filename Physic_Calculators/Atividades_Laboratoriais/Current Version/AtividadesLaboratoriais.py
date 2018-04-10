#!/usr/bin/env python3

"""
This code is under Apache License 2.0
Written by B_Gameiro (Bernardo Bernardino Gameiro)
More in 
    SoloLearn: https://www.sololearn.com/Profile/8198571
    GitHub: https://github.com/BGameiro76
    Repl.it: https://repl.it/@B_Gameiro

GUI para as atividades laboratoriais de Física do secundário em Python 3 e Tkinter
"""

#==========
# imports
#==========
import tkinter as tk
from tkinter import ttk, Menu
from tkinter import messagebox as msg
from Data.AtividadesClasses import *

# creating instance of main window
mainWin = tk.Tk()

#==========
# version
#==========
verGUI = ""
versaoAtvividadesLaboratoriais = verAtvLab
verPDF = ""

for cls in LaboratoryActivities.__subclasses__():
    containerLabel = str(cls.discipline)
    print(containerLabel)
    containerName = '%sContainer' % (cls.discipline)
    print(containerName)
    createContainers = '%s = ttk.LabelFrame(mainWin, text="%s")\n%s.grid()' % (containerName, containerLabel, containerName)
    print(createContainers)
    
    exec(createContainers)
    
    dg = ttk.Button(FísicaContainer, text="asd")

#======================
# Start GUI
#======================
mainWin.mainloop()