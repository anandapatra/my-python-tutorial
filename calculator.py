'''
Created on Jun 3, 2017

@author: AP2270
'''

def add(num1, num2):
    return (num1 + num2)

def subtract(num1, num2):
    return (num1 - num2)

def multiply(num1, num2):
    return (num1 * num2)

def divide(num1, num2):
    return (num1 / num2)

def main():
    operation = input('Enter a operation to be performed')
    if (operation != '+' and operation !='-' and operation !='*' and operation != "/"):
        print('Invalid Operation Entered. Please Enter one of +,-,* or /')
    else:
        num1 = int(input('Enter a number '))
        num2 = int(input('Enter the second number'))
        if(operation == '+'):
            return add(num1, num2)
        elif(operation == '-'):
            return subtract(num1, num2)
        elif(operation == '*'):
            return multiply(num1, num2)
        elif(operation == '/'):
            return divide(num1, num2)
        else:
            print('Nothing to be done')
    
print('Welcome to the Calculator')  
result = main()
print('The result of the operation is ', result)