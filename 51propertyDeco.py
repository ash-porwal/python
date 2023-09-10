#Property decorators allow us to use class method as attributes(variables we make are called attributes)
#and the second purpose is we can replace setter and getter methods

class Employee:
    company = "Mi"
    salary = 5000
    salarybonus = 400
    # totalSalary = 5400

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.totalSalary)
e.totalSalary = int(input("Enter total value: "))
print(e.salary)
print(e.salarybonus)