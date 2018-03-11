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
"""
Menu.
"""
print("Options:\n\n\nEnter what you want to calculate (perimeter, area or volume) and the the geometric figure/solid you want.\n\n\nNote:\n\n- The geometric figures supported are ./n- The solids supported are .")
"""
Defining groups of inputs.
"""
from math import pi as pie
Perimeter_expressions = ["perimeter", "Perimeter", "p", "P"]
Area_expressions = ["area", "Area", "a", "A"]
Volume_expressions = ["volume", "Volume", "v", "V"]
Expressions_1 = ["1", "(1)"]
Expressions_2 = ["2", "(2)"]
Expressions_3 = ["3", "(3)"]
Expressions_4 = ["4", "(4)"]
Expressions_5 = ["5", "(5)"]
"""
Calculation.
"""
while True:
  print(" \n ")
#User inputs.
  user_input_operation = input("Enter an operation : ")
#Calculation
  if user_input_operation in Perimeter_expressions:
    geometric_figure = input("Choose a geometric figure./n(1) Regular geometric figures (equal sides)/n(2) Rectangle/n(3) Triangle/n(4) Circle/n(5)/nGeometric figure:")
    if geometric_figure in Expressions_1:
      Number_of_sides = input("How many sides?/n:")
      Number_of_sides_float = float(Number_of_sides)
      if Number_of_sides_float > 2 and Number_of_sides_float != 4:
        Measurement_Sides = float(input("Measurement of the sides:"))
        print(Number_of_sides_float * Measurement_Sides)
      elif Number_of_sides_float == 4:
        Calculation_option_Square = input("What do you want to use as measurement?/n(1) Side/n(2) Diagonal/nOption:")
        if Calculation_option in Expressions_1:
          Square_Side = input("Measurement:")
          print(4 * Square_Side)
        elif Calculation_option in Expressions_2:
          Square_Diagonal = input("Measurement:")
          print(2 * (2 ** (1 / 2)) * Square_Diagonal)
        else:
          print("Unknown input")
      else:
        print("Unknown input")
    elif geometric_figure in Expressions_2:
      Rectangle_Side1 = float(input("Measurement of side 1:"))
      Rectangle_Side2 = float(input("Measurement of side 2:"))
      print(2 * (Rectangle_Side1 + Rectangle_Side2))
    elif geometric_figure in Expressions_3:
      Triangle_Side1 = float(input("Measurement of side 1:"))
      Triangle_Side2 = float(input("Measurement of side 2:"))
      Triangle_Side3 = float(input("Measurement of side 3:"))
      print(Triangle_Side1 + Triangle_Side2 + Triangle_Side3)
    elif geometric_figure in Expressions_4:
      Use_Pi = input("Use Pi or define it?/n(1) Use Pi/n(2) Use custom Pi/n:")
      if Use_Pi in Expressions_1:
        pi = pie
      elif Use_Pi in Expressions_2:
        pi = float(input("Custom Pi:"))
      else:
        print("Unknown input")
      Calculation_option_Circle = input("What do you want to use as measurement?/n(1) Radius/n(2) Diameter/nOption:")
      if Calculation_option_Circle in Expressions_1:
        Diameter_Circle = 2 * float(input("Measurement of the radius:"))
      elif Calculation_option_Circle not in Expressions_1 and Calculation_option_Circle not in Expressions_2:
        print("Unknown input")
      else:
        Diameter_Circle = float(input("Measurement of the diameter:"))
      print (pi * Diameter_Circle)
    elif geometric_figure in Expressions_5:
    else:
      print("That's not a supported geometric figure.")
  elif user_input_operation in Area_expressions:
    input("Choose a geometric figure :/n(1)/n(2)/n(3)/n(4)/n(5)")
  elif user_input_operation in Volume_expressions:
    input("Choose a solid :/n(1)/n(2)/n(3)/n(4)/n(5)")
  else:
    print("Unknown input")
