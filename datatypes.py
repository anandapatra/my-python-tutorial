'''
Created on Jun 3, 2017

@author: AP2270
'''
# number integer
from test.pickletester import MyTuple
num = 12345
print(type(num), num)

#string type
var = 'This is a variable'
print(type(var), var)

#float type
varD = 1.5
print(type(varD), varD)


#list type of data
myList = [1, 2,3,4,5]
print(type(myList), myList)
print('The fourth element in the list ', myList[3])

#dictionary data type
myDictionary = {'a':1, 'b':2, 'c':3}
print(type(myDictionary), myDictionary)
print('a contains', myDictionary['a'])

#tuple 
myTuple = (1,2,3,4,5)
print(type(myTuple), myTuple)
print('2nd element in the tuple is', myTuple[1])



