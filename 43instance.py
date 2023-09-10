class Employee:
    company = "Google"
    salary = 100
    

ashish = Employee()
rahul = Employee()

# Creating instance attribute salary for both the objects
# ashish.salary = 400
# rahul.salary = 300
ashish.salary = 45
print(ashish.salary)
print(rahul.salary)

# Below line throws an error as address is not present in instance/class 
# print(rahul.address)