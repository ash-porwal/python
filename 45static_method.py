# A normal method of classes are called instance method.

'''
Decorators - Any callable python object that is used to modify a function in a class
Pyhton has three built in decorators 
    - Static Method
    - Class Method
    - Property Decorator
we use decorators because we can change class methods or attributes without affecting the client side code   

'''

# Static methods can be called from both a class instance as well as from a Class

# we do not need to pass the class instance as the first argument via self, unlike other class functions.
# Which we can see in below @staticmethod as we did not define any self keyword

class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    # we have defined staticmethod decorator
    # in this we dont use any self keyword, so it can be used inside and outside of the class, with the class object
    @staticmethod 
    def greet():
        print("Good Morning, this is Static Method greet")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

Ashish = Employee()
Ashish.salary = 100000
Ashish.getSalary("Thanks") # Employee.getSalary(Ashish)
Ashish.greet() # Employee.greet()
Ashish.time()

'''
Staticmethod - It is a decorator
staticmethod in Python lets you create methods inside a class that don't need the class 
or its instances to work. 
It's like a regular function but belongs to a class. 
You can call it using the class itself, without having to create an object of the class.
'''