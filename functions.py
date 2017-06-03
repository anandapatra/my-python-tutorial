'''
Created on Jun 3, 2017

@author: AP2270
'''

print('Demonstrate the concept of method in python')

def sayHello():
    print('Hello')

def sayHi(inVar):
    print('Hi ', inVar)
    
def getData(inVar):
    return ('Input Data is ',inVar)
 
sayHello()   
sayHi('Ananda')
print(getData(5))
    
