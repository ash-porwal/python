#self refers to the instance of the class
#Self variable always refers to the object instance of a class
#self is a parameter which pass automatically when we call an object

#it is not neccessary that we can only use self with function inside class only...we can use self with function without class too.
#but insdide class we have to make function with self as argument ...and only @staticmethod can be used with function if do not want to put self as argument in function
class Employee:
    company = "Google"
    salary = 78000
    def getSalary(self):
        print("Salary is", self.salary)
        print("Number of days worked", self.days)


Ashish = Employee()
# Ashish.salary = 100000
Ashish.days = int(input("Number of days worked: "))
Ashish.getSalary()
# Employee.getSalary(Ashish)