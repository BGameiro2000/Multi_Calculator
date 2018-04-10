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

# creating instance
mainWin = tk.Tk()

#==========
# version
#==========
verGUI = ""
versaoAtvividadesLaboratoriais = verAtvLab
verPDF = ""

for cls in LaboratoryActivities.__subclasses__():
    print(cls)
#    cls = ttk.LabelFrame(mainWin, text=cls.discipline)

#======================
# Start GUI
#======================
mainWin.mainloop()