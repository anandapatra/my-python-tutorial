'''
Created on Jun 3, 2017

@author: AP2270
'''

var = 'I am a string variable'

print(len(var)) # gives the length of the string
print(var.capitalize()) # capitalize the starting alphabet of the string
print(var.count('a')) # counts the occurance of the alphabet in the sentence
print(var.find('a')) # returns the first index of the alphabet found
print(var[0:4]) # cuts the string till 4th index
print(var.swapcase()) # swaps the case of the string
print(var.endswith('variable')) # checks if ends with a given suffix
print(var.startswith('I')) # checks if starts with a given prefix
print(var.isalpha()) # checks if alphabets
