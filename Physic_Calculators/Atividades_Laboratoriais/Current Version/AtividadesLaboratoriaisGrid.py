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

#==========
# define window
#==========
# creating instance of main window
mainWin = tk.Tk()
# Title of the window    
mainWin.title("Atividades Laboratoriais do Secundário")
# size
#mainWin.geometry('550x450')

#==========
# version
#==========
verGUI = ""
verPDF = ""
verGeral = "0.G%s.A%s.P%s" % (verGUI, verAtvLab, verPDF)

#==========
# structure
#==========
mainContainer = ttk.LabelFrame(mainWin, text="Escolha a disciplina:") # main container
mainContainer.grid(padx=5, pady=5)
tabControl0 = ttk.Notebook(mainContainer) # main notebook inside container

for cls0 in LaboratoryActivities.__subclasses__(): # create tabs for notebook 0 and a container inside each tab
    tabLabel = str(cls0.specialAttribute)
    tab = ttk.Frame(tabControl0)
    tabControl0.add(tab, text=tabLabel)
    container = ttk.LabelFrame(tab, text="Escolha o ano:")
    container.grid(padx=5, pady=5)
    tabControl1 = ttk.Notebook(container)

    for cls1 in cls0.__subclasses__(): # create tabs for notebook 1 and a container inside each tab
        tabLabel = str(cls1.specialAttribute)
        tab = ttk.Frame(tabControl1)
        tabControl1.add(tab, text=tabLabel)
        container = ttk.LabelFrame(tab, text="Escolha a atividade laboratorial:")
        container.grid(padx=5, pady=5)
        tabControl2 = ttk.Notebook(container)

        for cls2 in cls1.__subclasses__(): # create tabs for notebook 2 and a container inside each tab
            tabLabel = str(cls2.specialAttribute)
            tab = ttk.Frame(tabControl2)
            tabControl2.add(tab, text=tabLabel)
            container = ttk.LabelFrame(tab, text=(cls0.specialAttribute, cls1.specialAttribute, cls2.specialAttribute))
            container.grid(padx=5, pady=5)
            ttk.Label(container, text=cls2.name).grid(column=0, row=0, sticky="W")

            containerVal = ttk.LabelFrame(container, text="Dados")
            containerVal.grid(column=0, row=1, sticky="W", padx=5, pady=5)
            checkVal = ttk.Button(containerVal, text="Calcular")
            for val in cls2.PhysicalQuantitiesVar:
                idx = list(cls2.PhysicalQuantitiesVar).index(val)
                ttk.Label(containerVal, text=cls2.PhysicalQuantitiesExpDic[val]+":").grid(column=0, row=idx, sticky="W", padx=5, pady=5)
                cls2.PhysicalQuantitiesValuesDic[val] = tk.DoubleVar()
                valueBox = ttk.Entry(containerVal, width=10, textvariable=cls2.PhysicalQuantitiesValuesDic[val], justify="right")
                valueBox.grid(column=1, row=idx, sticky="E", padx=5, pady=5)
                valueUnit = ttk.Combobox(containerVal, width=5, text=cls2.PhysicalQuantitiesUnitsDic[val])
                valueUnit.grid(column=2, row=idx, padx=5, pady=5)
                #valueUnit.current(cls2.PhysicalQuantitiesUnitsDic[val])
            checkVal.grid(column=2, sticky="E", padx=5, pady=5)

            containerAns = ttk.LabelFrame(container, text="Resultados")
            containerAns.grid(column=1, row=1, sticky="W", padx=5, pady=5)
            for ans in cls2.doActivity():
                

        tabControl2.grid(padx=5, pady=5) # show notebook 2
    tabControl1.grid(padx=5, pady=5) # show notebook 1
tabControl0.grid(padx=5, pady=5) # show notebook 0

#======================
# menu bar
#======================
# Creating a Menu Bar
menuBar = Menu(mainWin)
mainWin.config(menu=menuBar)

# Add menu items
# File menu
file_menu = Menu(menuBar, tearoff=0)
file_menu.add_command(label="Novo")
file_menu.add_separator()
file_menu.add_command(label="Versão")
file_menu.add_separator()
file_menu.add_command(label="Sair")
menuBar.add_cascade(label="Ficheiro", menu=file_menu)
edit_menu = Menu(menuBar, tearoff=0)
edit_menu.add_command(label="Procurar atualização")
edit_menu.add_separator()
edit_menu.add_command(label="Alterar atividades laboratoriais")
menuBar.add_cascade(label="Editar", menu=edit_menu)
help_menu = Menu(menuBar, tearoff=0)
help_menu.add_command(label="Informação")
help_menu.add_separator()
help_menu.add_command(label="Ajuda")
menuBar.add_cascade(label="Ajuda", menu=help_menu)
donate_menu = Menu(menuBar, tearoff=0)
donate_menu.add_command(label="Donativos")
donate_menu.add_separator()
donate_menu.add_command(label="Sugestões")
menuBar.add_cascade(label="Contribuir", menu=donate_menu)

#======================
# Start GUI
#======================
mainWin.mainloop()