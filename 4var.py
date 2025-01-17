#variables are the name given to a memory location in a program
a = "Ashish"
b = 50000
c = 89.90
d = True # this is boolean ..it can be either true or false
d = None # this is none 
#in python program it will automatically detect if we write something in double quote then it will consider as string ..if there is normal integer then it will detect as integer and for decimal numbers it if there is decimal then it will detect flaot
# Keywords – Reserved words in Python
# Identifiers – class/function/variable name
print(a)
print(b)
print(c)
print(d)
print(d)
#and this is how we print

#if we want to know which type of variable it is then
print(type(a))
print(type(b))
print(type(c))
print(type(d))

'''Rules for defining a variable name: (Also applicable to other identifiers)

A variable name can contain alphabets, digits, and underscore.
A variable name can only start with an alphabet and underscore.
A variable can't start with a digit.
No white space is allowed to be used inside a variable name
Variable names are case sensitive too
If you want to define a variable name which contains two words then separate them with _ like this: first_name'''

_c = "Yo"
A = "Porwal"
print(_c)
print(A)

# What are constants?
'''
So, In other programming language we can define constants and these are the varibales which should not be changed.
In python there is no way to define constant but we have this convention if we want to define constant whose varibale shouldn't change
then we can do with all capital letters, like below

API_KEY = "ksmdflsmdlfgdfgasdfasdfaspogjgpm"

'''

# What is type hinting?

'In python suppose I want to define a string, then I would do this'
first_name = 'Ashish'
'I did not define explicilty as string, python interpreter will automatically understand it is a string'


'Now the concept of type hinting requires us to actually explicitly say that we are using a string here:'

first_name: str = 'Ashish'
print(first_name)

# similarly we can type hint - int, dict, set, tuple

some_list: list = ['a', 'b', 'c']
# or we can more specify it
some_list: list[str] = ['a', 'b', 'c']



# if we assign some integer value in varibale with uderscore, then in output it is going to be ignored
some_number = 1000_00 #so this practise is recommneded if dealing with high numbers
print(some_number)

# Boolean flag
'''
>>> 
>>> t = True
>>> for i in range(3):
...     t
...     if t:
...             "t is True"
...     else:
...             "t is now False"
...     t = not t
... 
True
't is True'
False
't is now False'
True
't is True'
>>>
>>>
'''

### Common practice when naming varibales

'''
The most common practices for multi-word variable names are the following:

Snake case: use when define function or variables
    Lowercase words are separated by underscores. For example: number_of_graduates.

Camel case:  this one is less common in python
    The second and subsequent words are capitalized to make word boundaries easier to see. 
    For example: numberOfGraduates.

Pascal case: used for Classes and Exceptions
    Similar to camel case, except the first word is also capitalized. 
    For example: NumberOfGraduates.

'''


### PUBLIC and NON PUBLIC VARIABLE
'''
Public Variables:
- Naming: 
    Public variables are named using standard conventions without any prefix 
    or special characters, typically in snake case for regular variables.

    Usage: Public variables are intended to be used (read and possibly written to) 
    by external code. They are part of an API's or class's public interface.
    
    Example: self.name, self.age

- Non-Public Variables (Private variables):

    Naming: Non-public (private) variables are prefixed with a single underscore (_). 
    This convention indicates that the variable is intended for internal use within 
    the module or class and should not be accessed directly from outside the class or module.

    Usage: These variables are meant to be protected and not part of the public 
    interface of the class. Accessing these variables directly from outside the class 
    is considered bad practice, as it can lead to less maintainable and less predictable code. 
    
    Example: self._secret, self._internal_state
'''


### In Python there are some names which we never used as varibale names
'''
>>> import keyword
>>> keyword.kwlist
[
    'False',
    'None',
    'True',
    'and',
    'as',
    'assert',
    'async',
    ...,
    'yield'
]
'''

### Now, there are some built-in names which we should not use
'''
>>> import builtins
>>> dir(builtins)
[
    'ArithmeticError',
    'AssertionError',
    'AttributeError',
    ...
    'tuple',
    'type',
    'vars',
    'zip'
]
'''

### Variables Hold References to Objects
'''
- Python is an object-oriented programming language.
- Every piece of data in a Python program is an object of a specific type or class.
- So, when we define a variable in python it refer to a point in memory, to know that
  memory location we can use id() function, that retruns object's identifier.

- You can create multiple variables that point to the same object. 
  In other words, variables that hold the same memory address:
    >>> m = n
    >>> id(n) == id(m)
    True

  In above example, Python doesn't create a new object. 
  It creates a new variable name or reference, m, which points to the same 
  object that n points to.
'''

### TYPE HINTING OF VARIABLES
num: int = 5
# we can also create a variable without assigning a value
num: int  # but this thing doesn't declare a variable in the memory. so, if we print num then we will get error.


'''
>>> num: int
>>> num
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'num' is not defined. Did you mean: 'sum'?
>>> 
>>> __annotations__  # Even though number isn't defined, Python has recorded the type hint
{'num': <class 'int'>}
>>> 
'''