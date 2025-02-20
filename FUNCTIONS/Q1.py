# 1. Simple Calculator
# Problem: Write a program that implements a simple calculator using functions to
# perform basic arithmetic operations (addition, subtraction, multiplication, and
# division). The program should prompt the user for two numbers and an operation,
# and then return the result.
# Input: Two numbers and an operator (+, -, *, /)
# Output: The result of the operation

# Jainam Shah

def input_number(n):
    while True:
        try:
            value = float(input(f"Enter Number {n} : "))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

def calculate(number1,number2,operator):
    if operator == '+':
        result=number1+number2
        return result
    elif operator == '-':
        result=number1-number2
        return result
    elif operator == '*':
        result=number1*number2
        return result
    else:
        result=number1/number2
        return result
    
try:
    number1=input_number(1)
    number2=input_number(2)
    operator=input("Enter an Arithmetic Operator[+,-,*,/] : ")
except ValueError:
    print("Invalid input! Please enter a valid numerical score.")
else:
    if (len(operator) == 1) and (operator in ['+','-','*','/']):
        print(f"Answer is {calculate(number1,number2,operator)}")
    else:
        print("Invalid input! Please enter a valid Arithmetic Operator.")