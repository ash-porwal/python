'''
__eq__ is a special method (also known as a dunder method because of its double underscores) 
that's used to define the behavior of the equality operator (==) for custom classes.

When you compare two objects of a custom class using the == operator, 
Python internally calls the __eq__ method of the class to determine whether the two objects 
are considered equal.
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)  # True
print(p1 == p3)  # False

# So, where this __eq__ is getting called?

# When you use the equality operator (==) to compare two objects, like I did above p1 == p2
# the __eq__ method is automatically called

# so actually p1 == p2 get converted into p1.__eq__(p2)
# p1 is the object invoking the __eq__ method.
# p2 is the argument being passed to the __eq__ method.