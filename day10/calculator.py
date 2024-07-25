import math
import art


def add(n1, n2):
    return n1 + n2          

def sub(n1,n2):
    return n1 - n2

def times(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


def calculator(num1 = 0, num2 = 0):
    answer = 0
    if num1 == 0:
        num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    operations = {
        '+': add(num1,num2),
        '-': sub(num1,num2),
        '*': times(num1,num2),
        '/': div(num1,num2)
    }

    for operation in operations.keys():
        print(operation)
    operation_symbol = input("Pick an operation: ")

    answer += operations[operation_symbol]
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    choice = input(f"Type 'y' to continue calculating with {answer}; 'n' to start a new calculation; 'x' to finish running: ")
    if choice == 'y':
        calculator(answer)
    elif choice == 'n':
        calculator()
    else:
        exit()

calculator()