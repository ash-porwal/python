# A class method is a method that is bound to a class rather than its object.
# It doesn't require creation of a class instance, much like staticmethod. 

'''
The difference between a static method and a class method is:

Static method knows nothing about the class and just deals with the parameters
Class method works with the class since its parameter is always the class itself.

'''

class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(self, sal):
        self.salary = sal

e = Employee()
print(Employee.salary)
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)