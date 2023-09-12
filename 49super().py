'''
In an inherited subclass, a parent class can be referred to with the use of the super() function. 

The benefits of using a super function are:-  
    Need not remember or specify the parent class name to access its methods.
    This function can be used both in single and multiple inheritances.
    This implements code reusability as there is no need to rewrite the entire function.
    Super function in Python is called dynamically because Python is a dynamic language unlike other languages.

There are 3 constraints to use the super function:-  

    The class and its methods which are referred by the super function
    The arguments of the super function and the called function should match.
    Every occurrence of the method must include super() after you use it.
'''

#Super method  is use to access the methods of a super class(parent class) in the derived class

class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers") 
    
    def takeBreath(self):
        super().takeBreath()
        print("I am a Progarmmer so I am breathing++..")

p = Person()
p.takeBreath() 

e = Employee()
e.takeBreath() 

pr = Programmer()
pr.takeBreath() 


# if we have __init__ defined in Parent class then we would want to initialize in Child class too like below

class A:
    def __init__(self, name:str = "Class A") -> None:
        self.name = name
        print("we got name in Class A: ", self.name)
    
    def get_name(self):
        print(f"My name is: {self.name}")

class B(A):
    def __init__(self, name: str = "Class B") -> None:
        super().__init__(name)
    
    def get_name(self):
        print(f"This is get name function in class B")

b: B = B("Ash")
b.get_name()