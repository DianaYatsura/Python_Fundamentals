"""Create a Python program that emulates a simple calculator. It takes params:
number1, number2 and operator (+, -, *, /). Then, based on the operator, perform
the corresponding calculation and display the result. If the provided operator
doesnt exist provide the message "Wrong operator". *Use only if elif else structure"""

def calculator(number1, number2, operator):
    if operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "*":
        print(number1 * number2)
    elif operator == "/":
        print(number1 / number2)
    else: print("Wrong operator")

# enter values for number1, number2, operator for checking
calculator(number1=, number2=,operator='')
