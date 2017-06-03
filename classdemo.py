'''
Created on Jun 3, 2017

@author: AP2270
'''

class Student:
    __name=''
    __email =''
    
    def __init__(self, name, email):
        self.__name= name
        self.__email=email 
    
    def get_name(self):
        return self.__name


    def get_email(self):
        return self.__email


    def set_name(self, value):
        self.__name = value


    def set_email(self, value):
        self.__email = value


    def del_name(self):
        del self.__name


    def del_email(self):
        del self.__email

   
    name = property(get_name, set_name, del_name, "name's docstring")
    email = property(get_email, set_email, del_email, "email's docstring")
    
    def toString(self):
        return ('{} email address is {}'.format(self.__name, self.__email))
    
ananda = Student('Ananda', 'pat@gmail.com')
print(ananda.toString())
