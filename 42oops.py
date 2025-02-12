class RailwayForm: #class is the keyword for class
    formType = "RailwayForm"
    def printData(self): #yaha par function define hua hai...abhi ke liye  ye samjh lo ki self likhte hai
        print("Name is ", self.name) #yaha par ek fstring use kiya hai
        print(f"Train is {self.train}")

myApplication = RailwayForm() #here we did object instantiation..to yaha  ye bol raha ki ek mujhe naya form do...aur yaha par myApplication batata hai ki wo RailwayForm class ka object hai
myApplication.name = input("enter your name: ")
myApplication.train = "Rajdhani Express"
myApplication.printData()  # here we are calling the function 

'''
Just a note that method and function are not the same terms

function are not bound to any object and hence are not defined inside class
While Methods are bound to object and defined inside class

'''

# ------------------
# Concepets of OOPs:
# ------------------

# The four main pillars of Object-Oriented Programming (OOP) are
#   Encapsulation, Abstraction, Inheritance, and Polymorphism. 

"""
1.  Classes and Objects
    Classes: 
        A class is a blueprint for creating objects. 
        It defines a datatype by bundling data (attributes) and functions (methods) 
        that operate on the data into a single unit. 
        In Python, classes are defined using the class keyword.
    Objects: 
        An object is an instance of a class. 
        When a class is defined, no memory is allocated until an object of that class is created.
"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object of the class Dog
my_dog = Dog("Buddy", 4)
print(my_dog.bark())  # Output: Buddy says woof!

"""
2.  Encapsulation: 
        It is a process of wrapping data (variables) and methods into a single unit (class) and restricting direct access to some details to protect data integrity.
"""
class Car:
    def __init__(self, speed):
        self.__max_speed = speed  # Private attribute

    def drive(self):
        return f"Driving at {self.__max_speed} speed."

my_car = Car(200)
# print(my_car.__max_speed)  # This will raise an error
print(my_car.drive())  # Output: Driving at 200 speed.

"""
3.   Inheritance: 
        This allows a class to inherit attributes and methods from another class. 
        The new class is called a derived (or child) class, and the one from which it inherits 
        is called the base (or parent) class. This helps to reduce code redundancy.
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Derived classes need to implement this method.")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!


"""
4.  Polymorphism: 
        It enables a single function, method to operate in multiple ways, 
        allowing flexibility and scalability in programming.
"""
class India:
    def capital(self):
        print("New Delhi is the capital of India.")

class USA:
    def capital(self):
        print("Washington, D.C. is the capital of the USA.")

def describe_country(country):
    country.capital()

india = India()
usa = USA()

describe_country(india)  # Output: New Delhi is the capital of India.
describe_country(usa)    # Output: Washington, D.C. is the capital of the USA.


"""
5.  Abstraction: 
        This involves hiding the complex reality while exposing only the necessary parts. 
        In Python, this is generally accomplished using abstract classes and methods 
        (from the abc module), which declare methods that must be created within any child classes 
        built from the abstract class.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# shape = Shape()  # This will raise an error, cannot instantiate abstract class
rect = Rectangle(4, 5)
print(rect.area())  # Output: 20
print(rect.perimeter())  # Output: 18
