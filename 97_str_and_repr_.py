"""
__str__:

Tells Python how to display an object as a string.
Used when you print the object.
Meant to be readable for end-users.


__repr__:

Tells Python how to display an object in a way that, ideally, could recreate the object if you fed the string back to Python.
Useful for developers.
If you type just the object's name in a Python shell, this is what you see.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    p: Person = Person("Ashish", 26)

    # if we print this object then we would get somehting like this <__main__.Person object at 0x7f167ed8d810>
    # it is hard to read, but basically it says - we have an Object in main at this point of memory 0x7f167ed8d810 in my machine
    print(p)

    # but we would want to make some sense for as a user, so we will create two different dunder methods 
        # __str__
        # __repr__


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    # this is going to return the string representation of whatever we want to point,
    # so with the help of this if we want to print object like we did earlier, then it will print the custom text
    def __str__(self): 
        return f"You are trying to print object name"
    
    # repr stands for representation, in this we can return which is more readable to programmer
    # so this is suppse to be a literal representation
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

if __name__ == "__main__":
    p = Person("Ashish", 26)

    # if we print this object then we would get somehting like this <__main__.Person object at 0x7f167ed8d810>
    # it is hard to read, but basically it says - we have an Object in main at this point of memory 0x7f167ed8d810 in my machine
    
    print(p) # or print(str(p))
    print(repr(p))

    '''
    When you use print(p) and both __str__ and __repr__ are present in the class, 
    the __str__ method is called. So, you will get the string representation provided by __str__.
    '''