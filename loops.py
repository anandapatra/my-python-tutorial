'''
Created on Jun 3, 2017

@author: AP2270
'''

var = 'Hello World'
for v in var:
    print(v)
    

myList = [1,2,'Ananda', 'Python']
for i in myList:
    print('The current element in the list', i)

# iterate by seq index
for i in range(len(myList)):
    print(i)
    
for i in range(0,10):
    print(i)
    
# loop by while
count = 0;
while count != 10:
    print('The count is not yet 10')
    count= count + 1
    if count == 3:
       continue
    if count == 5:
        break
   