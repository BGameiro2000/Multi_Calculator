"""
Calculator in Python 3.
6 supported math functions.
Allows to use previous result.
More in 
  SoloLearn: https://www.sololearn.com/Profile/8198571
  GitHub: https://github.com/BGameiro76
  Repl.it: https://repl.it/@B_Gameiro
"""
"""
Menu.
"""
print("Options:\n\n\nEnter 'add', '+' or 'plus' to add two numbers.\n\nEnter 'subtract', '-' or 'minus' to subtract two numbers.\n\nEnter 'multiply', 'x' or 'times' to multiply two numbers.\n\nEnter 'divide', '/' or '÷' to divide two numbers.\n\nEnter 'exp' or '^' to elevate the first number to the power of the second number.\n\nEnter 'root' to find the nth root of the first number, being n equal to the second number.\n\nEnter 'quit' to stop the program.\n\nEnter 'ans' or press enter to use the previous result in a operation.\n\n\nNote:\n\n- The inputs above may not work at all times depending on what is the needed input.\n- Notice that, when using the root function, the program will use exponent's properties in order to achieve the result [x^y=x^(1/y)] and as the program can´t use an infinte number of decimals, it will provide an approximation.\n")
"""
Functions supported.
"""
def addition(input1, input2):
  return input1 + input2

def subtraction(input1, input2):
  return input1 - input2

def multiplication(input1, input2):
  return input1 * input2

def division(input1, input2):
  return input1 / input2

def exponentiation(input1, input2):
  return input1 ** input2

def root(input1, input2):
  return exponentiation(input1, division(1, input2))

def result(function, input1, input2):
  return function(input1, input2)
"""
Defining operations inputs.
"""
add_expressions = ("add", "+", "plus")
subtract_expressions = ("subtract", "-", "minus")
multiply_expressions = ("multiply", "x", "X", "times", '*')
divide_expressions = ("divide", "/", "÷")
exp_expressions = ("exp", "^", "to the power of")
root_expressions = ("root")
ans_expressions = ("continue", "ans", "previous result", "")
"""
Continuous calculation.
"""
while True:
  print(" \n ")
#User inputs.
  user_input_num1 = input("Enter a number : ")
  user_input_operation = input("Enter an operation : ")
  user_input_num2 = input("Enter another number : ")
#Inputs -> Floats
  if user_input_num1 in ans_expressions and user_input_num2 in ans_expressions:
    user_input_num1 = float(c)
    user_input_num2 = float(c)
  elif user_input_num1 in ans_expressions:
    user_input_num1 = float(c)
    user_input_num2 = float(user_input_num2)
  elif user_input_num2 in ans_expressions:
    user_input_num1 = float(user_input_num1)
    user_input_num2 = float(c)
  else:
    user_input_num1 = float(user_input_num1)
    user_input_num2 = float(user_input_num2)
#Use the inputs in the functions defined.
  #break
  if user_input_operation == "quit":
    break
  #addition
  elif user_input_operation in add_expressions:
    c = result(addition, user_input_num1, user_input_num2)
    print(c)
    print("\nContinue?\n")
  #subtraction
  elif user_input_operation in subtract_expressions:
    c = result(subtraction, user_input_num1, user_input_num2)
    print(c)
    print("\nContinue?\n")
  #multiplication
  elif user_input_operation in multiply_expressions:
    c = result(multiplication, user_input_num1, user_input_num2)
    print(c)
    print("\nContinue?\n")
  #division
  elif user_input_operation in divide_expressions:
    c = result(division, user_input_num1, user_input_num2)
    print(c)
    print("\nContinue?\n")
  #exponentiation
  elif user_input_operation in exp_expressions:
    c = result(exponentiation, user_input_num1, user_input_num2)
    print(c)
    print("\nContinue?\n")
  #nth root
  elif user_input_operation in root_expressions:
    c = result(root, user_input_num1, user_input_num2)
    print(c)
    print("\nContinue?\n")
  #Unknown input
  else:
    print("Unknown input")