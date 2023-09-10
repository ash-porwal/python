class Employee:
    company = "Visa"

class Freelancer:
    company = "Fiverr"

class Programmer(Freelancer, Employee):
    name = "Rohit"

p = Programmer()
print(p.company)