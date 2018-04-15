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

#======================
# title
#======================
# Title of the window    
mainWin.title("Atividades Laboratoriais Secundário")

#==========
# version
#==========
verGUI = ""
verPDF = ""
verGeral = "0.G%s.A%s.P%s" % (verGUI, verAtvLab, verPDF)

#==========
# functions
#==========
def xNotebook(container, parentClass, childAttribute):
    tabControl = ttk.Notebook(container)
    for cls in parentClass.__subclasses__():
        tabLabel = str(cls.childAttribute)
        tab = ttk.Frame(tabControl)
        tabControl.add(tab, text=tabLabel)
        containerName = '%sContainer' % (tabLabel)
        createContainers = '%s = ttk.LabelFrame(tab, text="%s")\n%s.grid()' % (containerName, tabLabel, containerName)
        exec(createContainers)
    tabControl.grid()

#==========
#
#==========
mainContainer = ttk.LabelFrame(mainWin, text="")
mainContainer.grid()

xNotebook(mainContainer, LaboratoryActivities, "discipline")

#======================
# Start GUI
#======================
mainWin.mainloop()