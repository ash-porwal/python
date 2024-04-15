'''
A classmethod in Python is a method that belongs to the class and not any specific instance. 
It takes a reference to the class itself as its first argument. 
This means it can modify class-level attributes.
'''

class MyClass:
    class_attribute = "I'm a class attribute!"

    def __init__(self, name:str = "INIT") -> None:
        self.name = name

    @classmethod
    def my_class_method(cls): # as we it is taking class itself as a  first arguments so we can access class attributes.
        print("This is a class method!")
        print("Accessing class attribute:", cls.class_attribute)

        # We can now use cls to access or modify class-level attributes or other class methods.
        cls.class_attribute = "I've changed attribute value"
        print(cls.class_attribute)


# Calling the class method directly on the class, without creating an instance
MyClass.my_class_method()
print("Line 25: ", MyClass.class_attribute)


'''
The difference between a static method and a class method is:
------------------------------------------------------------

classmethod: 
Works with the class itself (i.e., with class-level attributes). 
Often used when you need to deal with attributes shared across instances.
Class method works with the class since its parameter is always the class itself.


staticmethod: 
Doesn't care about class-specific or instance-specific details. 
It behaves like a regular function but is, for some logical reason, 
bundled with a class (e.g., for organization).
------------------------------------------------------------

classmethod: 
Always takes a reference to the class itself as its first parameter, 
which is conventionally named cls.

staticmethod: 
Doesn't take any special first parameter. 
It doesn't automatically pass the class or instance reference.
------------------------------------------------------------

Both can be called on a class or on an instance, but...

classmethod: 
Has access to the class, so it can access and modify class-level attributes.

staticmethod: 
Cannot access or modify class-level or instance-level attributes unless they're explicitly passed into the method.
------------------------------------------------------------
'''