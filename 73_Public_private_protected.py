''' 
Variables are of three types:
    Public - any information which you want to see by everyone.
    Protected - any inforamtion which you want to see by some people chosen by you.
    Private - any info which only you can see.

Concept of public, private, and protected variables relate to the access control.
    - Public variables can be accessed from anywhere inside or outside of the class. 
    - Protected variables should not be accessed from outside of the class and its subclasses.In Python, this is only a convention and is not enforced by the language.
    - Private variables are meant to be hidden from anything outside the class. Python performs name mangling on these variables. In name mangling, the interpreter changes the variable name in a way that makes it harder to create subclasses that accidentally override the private attributes and methods.
'''
# Private Variables

class Employee:
    def __init__(self, name, salary):
        self.__name = name  # This is a private variable
        self.__salary = salary  # This is also a private variable

    def display_info(self):
        print(f"Employee Name: {self.__name}")
        print(f"Salary: {self.__salary}")

emp = Employee("John Doe", 50000)
emp.display_info()  # Accessible through a class method
# print(emp.__name)  # This will raise an AttributeError
print(emp._Employee__name)  # Name mangling allows access like this


'''
like in class if you want to make a: 
    public variable then directly put that in class like showed below 
    protected variables are made with single underscore before the name of the variable...so that that variable can be access by that class itself or can be access by that class object but cannot be access by outer class
    private variables can be made by putting double underscore before variable name  ...so it means that variable is saying do not use it outside the class..so even the object cannot acces it directly
    but that object can access private variable if we write it with that class name ...as showed below  

'''

class Variables:
    one = "This is public variable"
    _two = "This is protected variable"
    __three = "This is Private variable and hence should not be used outside the class"

    def fun1(self):
        pass

ashish = Variables()
print(ashish.one)
print(ashish._two)
# print(ashish.__three) #see this is a private variable and it can only be access outside the class as shown below
print(ashish._Variables__three)  