# Class and Object :

class Student:
    def show(self):
        print(" This is a student class...")
s=Student()
s.show()        


# Constructer:

class Student:
    def init (self,name):
        self.name = name
    def display(self):
        print("SHIKHAR")
s=Student()        
s.display()        

#Inheritence:

class Father:
    def house(self):
        print("Fathers house")
class Son(Father):
    pass
s=Son()
s.house() 