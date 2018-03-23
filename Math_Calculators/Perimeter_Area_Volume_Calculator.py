#!/usr/bin/env python3
"""
This code is under Apache License 2.0
Written by B_Gameiro (Bernardo Bernardino Gameiro)
More in 
  SoloLearn: https://www.sololearn.com/Profile/8198571
  GitHub: https://github.com/BGameiro76
  Repl.it: https://repl.it/@B_Gameiro
  
Calculator in Python 3.
Supports perimeters, areas and volumes.
"""
#==============================================================================================================================================================================================================
#Menu
#==============================================================================================================================================================================================================
print("\n\n\n\n\n\n\n\nOptions:\nEnter what you want to calculate (perimeter, area or volume) and the the geometric figure/solid you want.\n\n\nNote:\n\n- The geometric figures supported are .\n- The solids supported are .\n")

#==============================================================================================================================================================================================================
#Defining groups of inputs, functions and imports.
#==============================================================================================================================================================================================================
from math import pi as pie
import re

Perimeter_expressions = ["perimeter", "Perimeter", "p", "P"]
Area_expressions = ["area", "Area", "a", "A"]
Volume_expressions = ["volume", "Volume", "v", "V"]
Expressions_1 = ["1", "(1)"]
Expressions_2 = ["2", "(2)"]
Expressions_3 = ["3", "(3)"]
Expressions_4 = ["4", "(4)"]
Expressions_5 = ["5", "(5)"]
notnumbers = r"[^0-9]"

def printt(operation):
  if operation == "perimeter":
    result = perimeter
  elif operation == "area":
    result = area
  elif operation == "volume":
    result = volume
  else:
    print("Something went wrong!")
  print("\nThe", operation, "is", result)

#==============================================================================================================================================================================================================
#Loop & calculation
#==============================================================================================================================================================================================================
while True:

#==============================================================================================================================================================================================================
#User inputs
#==============================================================================================================================================================================================================
  user_input_operation = input("\nEnter an operation\n: ")

#==============================================================================================================================================================================================================
#Perimeter menu
#==============================================================================================================================================================================================================
  if user_input_operation in Perimeter_expressions:#Select geometric figure
    perimeter = 0
    Number_of_sides = 0
    geometric_figure = input("\nChoose a geometric figure.\n\n(1) Regular geometric figures (equal sides)\n(2) Rectangle\n(3) Triangle\n(4) Circle\n(5) Geometric figure\n\n:")

#==============================================================================================================================================================================================================
#Perimeter of regular geometric figures (number of sides)
#==============================================================================================================================================================================================================
    if geometric_figure in Expressions_1:
      try:
        Number_of_sides = int(input("\nHow many sides?\n:"))
      except:
        print("Unknown input")
        continue

#==============================================================================================================================================================================================================
#Perimeter of regular geometric figures (if it isn't a square)
#==============================================================================================================================================================================================================
      if Number_of_sides > 2 and Number_of_sides != 4:#At least 2 sides
        try:
          Measurement_Sides = float(input("\nMeasurement of the sides\n:"))
        except:
          print("Unknown input")
          continue
        perimeter = Number_of_sides * Measurement_Sides
        printt("perimeter")

#==============================================================================================================================================================================================================
#Perimeter of regular geometric figures (if it is a square)
#==============================================================================================================================================================================================================
      elif Number_of_sides == 4:
        Calculation_option_Square = input("What do you want to use as measurement?\n\n(1) Side\n(2) Diagonal\n\n:")
        if Calculation_option_Square in Expressions_1:#If side, multiply by 4
          try:
            Square_Side = float(input("\nMeasurement\n:"))
          except:
            print("Unknown input")
            continue
          perimeter = 4 * Square_Side
          printt("perimeter")
        elif Calculation_option_Square in Expressions_2:#If diagonal, calculate the side         ### diagonal**2 = 2*(side**2) <=> side = diagonal/(sqrt 2)
          try:                                                                                   ### perimeter = no of sides * lenght of the side <=> perimeter = 4 * diagonal/(sqrt 2)
            Square_Diagonal = float(input("\nMeasurement\n:"))                                   ### perimeter = (2 ** (5/2)) * diagonal or 4 * (2 ** (1 / 2)) * diagonal
          except:
            print("Unknown input")
            continue
          perimeter = 4 * (2 ** (1 / 2)) * Square_Diagonal
          printt("perimeter")
        else:#Unknown input
          print("Unknown input")
      else:
        print("Unknown input")

#==============================================================================================================================================================================================================
#Perimeter of an rectangle
#==============================================================================================================================================================================================================
    elif geometric_figure in Expressions_2:
      try:
        Rectangle_Side1 = float(input("Measurement of side 1\n:"))
        Rectangle_Side2 = float(input("Measurement of side 2\n:"))
      except:
        print("Unknown input")
        continue
      perimeter = 2 * (Rectangle_Side1 + Rectangle_Side2)
      printt("perimeter")

#==============================================================================================================================================================================================================
#Perimeter of an triangle
#==============================================================================================================================================================================================================
    elif geometric_figure in Expressions_3:
      Triangle_Side1 = float(input("Measurement of side 1\n:"))
      Triangle_Side2 = float(input("Measurement of side 2\n:"))
      Triangle_Side3 = float(input("Measurement of side 3\n:"))
      perimeter = Triangle_Side1 + Triangle_Side2 + Triangle_Side3
      printt("perimeter")

#==============================================================================================================================================================================================================
#Perimeter of an circle (pi)
#==============================================================================================================================================================================================================
    elif geometric_figure in Expressions_4:
      Use_Pi = input("Use Pi or define it?\n\n(1) Use Pi\n(2) Use custom Pi\n\n:")#Define pi
      if Use_Pi in Expressions_1:#default pi
        pi = pie
      elif Use_Pi in Expressions_2:#user aproximation
      	while True:
          pi_ = input("\nCustom Pi\n:")
          try: #try to use float
            pi = float(pi_)
          except:
            continue
          if pi == 3 or pi == 3.1 or 3.15 <= pi <= 3.14:#if float and reasonable
            break
          elif pi_ == "pi" or pi_ == "real pi" or pi_ == "π":#if not float and reasonable, use the real pi
            pi = pie
            break
          else:
            print("Thats definitely not pi.")
      else:
        print("Unknown input")

#==============================================================================================================================================================================================================
#Perimeter of an circle (diameter or radius)
#==============================================================================================================================================================================================================
      Calculation_option_Circle = input("\nWhat do you want to use as measurement?\n(1) Radius\n(2) Diameter\n\n:")
      if Calculation_option_Circle in Expressions_1:#diameter
        try:
          Diameter_Circle = 2 * float(input("Measurement of the radius\n:"))#diameter to radius
        except:
          print("Unknown input")
          continue
      elif Calculation_option_Circle not in Expressions_1 and Calculation_option_Circle not in Expressions_2:
        print("Unknown input")
      else:#radius
        try:
          Diameter_Circle = float(input("Measurement of the diameter\n:"))
        except:
          print("Unknown input")
          continue

#==============================================================================================================================================================================================================
#Perimeter of an circle (answer)
#==============================================================================================================================================================================================================
      perimeter = pi * Diameter_Circle
      printt("perimeter")

#==============================================================================================================================================================================================================
#Perimeter of any given figure
#==============================================================================================================================================================================================================
    elif geometric_figure in Expressions_5:
      try:
        Number_of_sides = int(input("\nHow many sides?\n:"))#number of sides
      except:
        print("Unknown input")
        continue
      print()
      for i in range(Number_of_sides):#sum of every side
        try:
          side = float(input("Side " + str(i+1) + ": "))
          perimeter += side
        except:
          print("Unknown input")
          while True:
            side = input("Side " + str(i+1) + ": ")
            if re.search(notnumbers, side):
              print("Unknown input")
            else:
              perimeter += float(side)
              break
      printt("perimeter")#answer

#==============================================================================================================================================================================================================
#Unsupported figures
#==============================================================================================================================================================================================================
    else:
      print("That's not a supported geometric figure.")

#==============================================================================================================================================================================================================
#Area
#==============================================================================================================================================================================================================
  elif user_input_operation in Area_expressions:
    input("Choose a geometric figure :\n(1)\n(2)\n(3)\n(4)\n(5)")

#==============================================================================================================================================================================================================
#Volume
#==============================================================================================================================================================================================================
  elif user_input_operation in Volume_expressions:
    input("Choose a solid :\n(1)\n(2)\n(3)\n(4)\n(5)")

#==============================================================================================================================================================================================================
#Unknown inputs
#==============================================================================================================================================================================================================
  else:
    print("Unknown input")