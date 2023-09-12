'''
both __new__ and __init__ are methods related to the creation and initialization of objects.

--------------------------------------------------------------------------------------------
__new__: 
It is responsible for creating (and returning) a new instance of a class. 
It's a static method of the class and gets called before __init__.

__init__: 
It is responsible for initializing the attributes of the created instance. 
It doesn't return anything (implicitly returns None), 
and its main job is to set up the object's initial state.
--------------------------------------------------------------------------------------------
Arguments:

__new__: 
The first argument is the class (cls), 
followed by any additional arguments that were passed to create the instance. 
Typically, it looks like def __new__(cls, *args, **kwargs):.


__init__: 
The first argument is the instance being initialized (self), 
followed by any additional arguments. 
Typically, it looks like def __init__(self, *args, **kwargs):.
--------------------------------------------------------------------------------------------

Return Value:

__new__: 
Should return an instance, which could be an instance of the class or another class altogether.

__init__: 
Doesn't return anything. It only initializes the attributes of an existing instance.
--------------------------------------------------------------------------------------------
'''

class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance")
        instance = super(MyClass, cls).__new__(cls)
        return instance #this is returning to wherever object was created of this Class

    def __init__(self, value):
        print("Initializing the instance")
        self.value = value

obj = MyClass(5)

'''
Code explaination - this line: instance = super(MyClass, cls).__new__(cls)

super(MyClass, cls): 
This gets a temporary object of the superclass, 
which is typically the base object class in Python (unless MyClass has other parents).

.__new__(cls): 
This is calling the __new__ method of the superclass. 
In most cases, this will be the __new__ method of the base object class,
which is responsible for actually creating and returning the new instance of the class. 
The resulting instance is stored in the instance variable.

then with this statements: return instance
The instance that was just created is returned. 
Any further operations on this instance (like initialization) would take place afterward.

-----------------------------------------------------------------------------------------
Keep in mind

In Python, the term "object" can refer to two things:

Any instance of a class: 
In this context, obj is an object (or instance) of the class MyClass.

The base object class: 
All classes in Python implicitly inherit from a built-in class named object 
if no other superclass is specified. 
This built-in object class is the most base type in Python's inheritance chain.
'''