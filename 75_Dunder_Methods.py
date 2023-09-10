#those methods which starts and ends with double underscore are called dunder methods
class A:
    var1 = "This is var 1"

    def __init__(self, name, salary, work):
        self.name = name
        self.salary = salary
        self.work = work

    def __add__(self, other):
        return self.salary + other.salary
 
emp1 = A("rohan", 90, "Cleaner")
emp2 = A("mohan", 10, "Litterer")
print(emp1 + emp2)