# __init__ method aka contructor in many other programming languges but in Python it is called initializer
# which is first run as the object is created 
class Employee:
    company = "Google"

    def __init__(self, name, salary, company):
        self.name = name
        self.salary = salary
        self.company = company
        print("Employee is created!") 

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The company of the employee is {self.company}")


Ash = Employee("Ashish", 5000, "Microsoft")
# Ash = Employee() --> This throws an error (missing 3 required positional arguments:)
Ash.getDetails()