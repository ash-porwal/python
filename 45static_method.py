'''
Decorators - Any callable python object that is used to modify a function in a class
Pyhton has three built in decorators 
    - Static Method
    - Class Method
    - Property Decorator
we use decorators because we can change class methods or attributes without affecting the client side code   

'''

#Static methods can be called from both a class instance as well as from a Class
#we do not need to pass the class instance as the first argument via self, unlike other class functions.

class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

Ashish = Employee()
Ashish.salary = 100000
Ashish.getSalary("Thanks") # Employee.getSalary(Ashish)
Ashish.greet() # Employee.greet()
Ashish.time()