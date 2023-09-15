# dataclasses is a module introduced in Python 3.7 as part of the standard library.

# It provides a decorator and functions to create classes that are primarily used to store 
# data with little boilerplate. 
# These classes, often referred to as "data classes", automatically generate special methods 
# like __init__(), __repr__(), and __eq__().


#To define a data class, you use the @dataclass decorator:

from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

"""
With just this code, you get an automatically generated constructor, 
so you can instantiate Point as Point(1.0, 2.0). 
You also get a nice __repr__ method and an __eq__ method for free.
"""

p1: Point = Point(1.0,2.0)
p2: Point = Point(1.0,2.0)
print(p1==p2) # we didnt define __eq__ in class but still able to check it
print(p1) # we get __repr__
print(p2) # we get __repr__

# Immutability
# You can make instances of your data class immutable:

@dataclass(frozen=True)
class Point:
    x: float
    y: float

# Now, once an instance of Point is created, you cannot modify its attributes.