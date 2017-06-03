'''
Created on Jun 3, 2017

@author: AP2270
'''

fo = open('text.txt', 'w')
fo.write('I am writing to the file')
fo.close()

fo=open('text.txt', 'a')
fo.write('\nI am writing the next line to the file')
fo.close()

fo=open('text.txt', 'r')
text = fo.read()
print(text)
fo.close()

