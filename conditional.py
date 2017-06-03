'''
Created on Jun 3, 2017

@author: AP2270
'''

x = 5 
var = 'Ananda'

if x < 5 and var.startswith('A'):
    print('The value of the number is less than 5')
    print('The variable starts with alphabet A')
elif x==5 and var.startswith('A'):
    print('The value of the variable is 5 and the var starts with A')
else:
    print('The value of the number is not less than 5')
    print('The variable does not start with A')