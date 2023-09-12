"""
-------------------------------------------------------------------
An abstract class can't be instantiated (i.e., you can't create an object of it). 
The primary purpose of an abstract class is to act as a base for other classes. 
An abstract method, on the other hand, is a method that's declared but doesn't have an implementation in the abstract class.
-------------------------------------------------------------------

-------------------------------------------------------------------
If a class contains any method decorated with @abstractmethod, 
it becomes an abstract class. 
You cannot create an instance (or object) of an abstract class. 
If you try to instantiate it, Python will raise a TypeError.
-------------------------------------------------------------------
"""
from abc import ABC, abstractmethod

class AbstractClass(ABC):

    @abstractmethod
    def abstract_method(self):
        pass

# This will raise an error, as we can't instantiate an abstract class
# obj = AbstractClass()

# Abstract Method with Implementation

'''
-------------------------------------------------------------------
In Python, unlike some other languages, 
an abstract method can have an implementation in the abstract class. 
However, any child class must still provide its own implementation.
-------------------------------------------------------------------
'''
class AbstractClassWithImplementation(ABC):

    @abstractmethod
    def abstract_method(self):
        print("Implementation in the abstract class!")

class ChildClass(AbstractClassWithImplementation):

    def abstract_method(self):
        print("Child's implementation of the abstract method!")

        
obj = ChildClass()
obj.abstract_method()  # This will print "Child's implementation of the abstract method!"
