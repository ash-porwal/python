#Property decorators allow us to use class method as attributes(variables we make are called attributes)
#and the second purpose is we can replace setter and getter methods.
#Setter is use to set the attributes value

#Using Property decorator we can call class methods as attributes

'''
https://youtu.be/5-S_B6nAzO8
'''


class Student:
    def __init__(self, name, grade): 
        self.name = name
        self.grade = grade
        print("Grade inside class: ", self.grade)
    @property
    def result(self):       
        print("Grade inside result function: ", self.grade)
        return f"{self.name} got {self.grade}"

Ashish = Student("ashish", "A+")
Ashish.grade = "c"
print(Ashish.grade)
print(Ashish.name)
print(Ashish.result) # result is the function, getting called without parentheses