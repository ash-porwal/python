# Inheritance is a way to create a new class from existing class
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")
    
    def showDetails(self):
        print("This is an programmer")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)



class SomeClassA:
    age = 26

    def __init__(self) -> None:
        self.name = 'Ashish'

class SomeClassB(SomeClassA):
    print("with help of class name: ", SomeClassA.age)

b = SomeClassB()
print("with help of object: ", b.age)
