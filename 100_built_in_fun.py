# Please refer below for all built-in functions
# https://docs.python.org/3/library/functions.html
print('-------print function--------')

# print with sep
# using sepeartor we can seperate the commans 
print("THIS", "THAT", sep=':')
print("THIS", "THAT", sep=' ') # leaving empty it will give the usual output, otherwise we can pass anything
print("THIS", "THAT", sep='askdnasd') # seperating with random text

# print with end - 
# when there is written a priint statnemen
print("Ashish") # actually it is written like -> print("Ashish", end='\n')
print("print statement1", end='') # this will turncate the new line character, and we can pass any value in quote of end.
print("print statement2")

# to go on documentation of any function
# On MacOS - press Command key and click on function which doc you want to see
# for windows/unix press Ctrl and click on that function
print()
# ------------------------------------------------------------------------------------------
print('--------enumerate---------')

# enumerate function
# Enumerate function returns index and items of the iterable 

sample_list: list[str] = ['Ash', 'Rahul', 'Abhishek']

for k, v in enumerate(sample_list):
    print(f'{k} : {v}')

# if we loop it to single value like below
print()

# below will return a tuple of index and value
for k in enumerate(sample_list):
    print(k)

print()
# we can even specify the start value in enumerate, by default it starts with 0
# I want it should start with 101 this time
for k, v in enumerate(sample_list, start=101):
    print(f'{k} : {v}')
print()

# ------------------------------------------------------------------------------------------
# round function
print('-------round--------')

some_float: float = 1.666677788
# we can round the above number
print(round(some_float))

# what if we want that round should be performed after 3 decimal then we would do this
print()
print(round(some_float, 3)) # I simply added 3

# ------------------------------------------------------------------------------------------
# range
print()
print('--------range--------')

# when it is just one number defined then it starts with 0 and ends at n-1. 
# (where n is that number which you defined in range function)
num: range = range(10) 
print(num)

# we can convert that range into a list
print(list(num))

# range syntax: range(start_value, end_value, step)

# to get negative number we want to define -1 at step
print(list(range(0, - 11, -1)))

# so above we converted range to a list but the size of range is pretty low as compare to list

# let's see the size of this number
import sys

print(sys.getsizeof(num)) # just 48bytes

#same number but as a list
print(sys.getsizeof(list(num))) # now it is around 136bytes, the same range as above but it is a list.

num2: range = range(10**2) # we can see this is a pretty big number, if we print it as a list, then computer is going to crash
print(sys.getsizeof(num2)) # just 48bytes again
print(sys.getsizeof(list(num2))) # 856 bytes just on converting from range to list

# ------------------------------------------------------------------------------------------
# globals
# returns a dictionary representing the current global symbol table
print()
print('---------globals---------')
print(globals())

# ------------------------------------------------------------------------------------------
# locals
# returns a dictionary representing the current local symbol table.
print()
print('---------locals---------')
# if we print this in a funtion then it just return local varibales of that function

def some_fun():
    x1 = "this is local x1"
    x2 = "this is local x2"

    print(locals())
some_fun()

# ------------------------------------------------------------------------------------------
# all()
# all() function returns True if all items in an iterable are true. Otherwise, it returns False.
print()
print('---------all()---------')

print(all([True, True, True]))
print(all([True, False, True]))

print(all([0, 1, 2, 3]))  # 0 is considered False in a boolean context
print(all([]))  # Empty iterable, so it's considered True by convention

# ------------------------------------------------------------------------------------------
# any()
# any() function returns True if at least one item in an iterable is true. Otherwise, it returns False.


print()
print('---------any()---------')
print(any([False, False, True]))

print(any([False, 0, ''])) #False

print(any([])) # Empty iterable, so it's considered False by convention

# ------------------------------------------------------------------------------------------
print()
print('---------isinstance()---------')
# Syntax: isinstance(object, classinfo)

# object: The object whose type you want to check.
# classinfo: A class, type, or a tuple of classes/types.
x = 10
print(isinstance(x, int))  # True

# Checking with multiple classes (using a tuple):
x = "Hello"
print(isinstance(x, (int, str, list)))  # True, because x is a str

# Using with user-defined classes:

class MyClass:
    pass

obj = MyClass()
print(isinstance(obj, MyClass))  # True

class Parent:
    ...

class Child(Parent):
    ...

obj = Child()
print(isinstance(obj, Parent))  # True, because Child inherits from Parent

# ------------------------------------------------------------------------------------------
print()
print('---------callable()---------')

# it is used to determine if an object can be called. An object is considered callable if it can be invoked like a function or method, 
# i.e., if you can put parentheses () after it and call it.

# Syntax: callable(object)

def my_function():
    pass

print(callable(my_function))  # True

# Checking built-in functions: len()
print(callable(len))  # True

# Checking classes:
class MyClass:
    ...

print(callable(MyClass))  # True

# Checking class instances:
# Class instances themselves are usually not callable unless the class defines a __call__ method.

class CallableClass:
    def __call__(self):
        return "I'm callable!"

obj = CallableClass()
print(callable(obj))  # True

class NonCallableClass:
    ...

obj2 = NonCallableClass()
print(callable(obj2))  # False

# ------------------------------------------------------------------------------------------
print()
print('---------filter()---------')
# used to filter elements from an iterable based on a function
# It tests each element in the iterable to see if it satisfies a certain condition and returns an iterator for the elements that return True.

# Syntax: filter(function, iterable)

# function: A function that tests each element in the iterable. 
#           If the function returns True, the element is included in the result. 
#           If the function is None, the identity function is assumed, 
#           meaning all elements that evaluate to False in a boolean context (like 0, '', None) will be removed.

#  iterable: The iterable whose elements you want to filter.

# You can achieve similar filtering with list comprehensions, which might be more readable in some scenarios:

numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [2, 4, 6]

# using list comprehension
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]

# ------------------------------------------------------------------------------------------
print()
print('---------map()---------')
# map() is used to apply function to all items in an input iterable

# Syntax: map(function, iterable)

numbers = [1, 2, 3, 4, 5, 6]
return_value = map(lambda x: x**2, numbers)
print(list(return_value))

# ------------------------------------------------------------------------------------------
print()
print('---------sorted()---------')

# it is used to sort element of an iterable and return a new list, 
# and sort() is different method - it is a method of list

# Syntax: sorted(iterable, *, key=None, reverse=False)

# iterable: whose items you want to sort
# key (optional): here we pass pre built function, like if we pass key=len, and list it like numbers = ['asdasd', 'asdff', 'sdfgdsdsfgsadf'], then it will sort the list according to lenght of those string
# reverse: if this set to True then all items will be sorted in descending order

print(sorted(numbers, reverse=True))

# ------------------------------------------------------------------------------------------
print()
print('---------eval()---------')

# Syntax: eval(expression, globals=None, locals=None)

#   expression: The string parsed and executed as a Python expression.
#   globals: (Optional) A dictionary containing global variables.
#   locals: (Optional) A dictionary containing local variables.

result = eval("10 + 20")
print(result)

# Difference between expression and statement
# anyhting that returns a value in python is a expression and statement does not return a value.

# print() is statement because that does not retunr a value.
# x = 10*10 here 10*10 is an expression because it returns a value and assigns to x

# so eval takes only those things which are going to return us something

global_var = 10

def test_eval():
    local_var = 5
    return eval("global_var + local_var", globals(), locals())
    
print(test_eval())  # 15


# ------------------------------------------------------------------------------------------
print()
print('---------exec()---------')

# execute function is just like eval but there's a key difference. 
# While eval() is designed to evaluate a single expression and return its value, 
# exec() is meant for executing dynamically created Python code which can be a single or multiple lines. 
# exec() doesn't return a value (it returns None), but it can modify variables in place or define new ones, among other actions.

# Syntax: exec(source, globals=None, locals=None)

user_input = input("Please enter something: ")
exec(user_input)

code = """
def say_hello(name):
    return "Hello, " + name
"""
exec(code)
print(say_hello("Ashish"))  # This will print "Hello, Ashish

# ------------------------------------------------------------------------------------------
print()
print('---------zip()---------')

# Syntax: zip(*iterables)
# *iterables: Two or more iterable objects, like lists, tuples, etc.

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


# Zipping lists of different lengths:
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30]
zipped = zip(names, ages)
print(list(zipped))  # [('Alice', 25), ('Bob', 30)]

# Unzipping a zipped list:
zipped_data = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
names, ages = zip(*zipped_data)
print(names)  # ('Alice', 'Bob', 'Charlie')
print(ages)  # (25, 30, 35)

