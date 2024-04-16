# "dunder methods" (short for "double underscore methods") are special methods that begin 
# and end with double underscores. 
# They are also known as "magic methods.

# Dunder methods are used to provide specific functionalities to Python classes and 
# are automatically invoked by certain actions or operations on those classes.

"""
Common Dunder methods - 
__init__(self, ...): This method is used to initialize a new object. It's called when an object is created from a class and allows the class to initialize the attributes of the object.

__str__(self): Returns a human-readable string representation of the object. This method is called by the str() built-in function and by the print() function.

__repr__(self): Returns an official string representation of the object that should, ideally, be a valid Python expression that could be used to recreate the object. This is called by the repr() built-in function.

__add__(self, other): Allows for the definition of a custom behavior for the addition operator +. If an instance of the class appears on the left side of +, Python calls this method.

__eq__(self, other): Defines behavior for the equality operator ==. This method should return True if the objects should be considered equal, or False otherwise.

__getitem__(self, key): Allows an object to use index-based access like lists or dictionaries. Implementing this method enables you to use obj[key] to access items.

__setitem__(self, key, value): Similar to __getitem__, but this method allows you to set the value of an item within your object using an index or key, like obj[key] = value.

__delitem__(self, key): Enables an object to use syntax similar to deleting items from a list or dictionary, such as del obj[key].

__iter__(self): Returns an iterator for the object. This method is called when an iterator is required, such as in loops or the iter() built-in function.

__call__(self, *args, **kwargs): Allows the instances of the class to be called as if they were functions.

"""

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