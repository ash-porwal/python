'''
decorators
are the function which takes another function as an argument and returns a a wrapped version of that function
decorator takes the result of a function, modifies the result and returns it.
we use @function_name  to specify a decorator to be applied on another function
'''



def decor(fun):
    def inner():
        print("Inner function before enhancing function")
        fun()
        print("Inner function after enhancing function")
    return inner
    
@decor
def fun1():
    print("this is function 1")
    print("using decorator we will enhance this function")
    # after above line now decorator will take this function as a parameter and adds some functionality and return this function

# save_fun = decor(fun1)
## save_fun = inner
# save_fun()

fun1()

# But we dont include wrapper then we will see something unusual.
# Suppose below is the some function which has a doc string, and function name is some_fun

# so, if we do print(some_fun.__doc__) then it should actually return a doc string but it will return None.
# and on doing print(some_fun.__name__) then it should return name of the function which is some_fun but as we are using @decorator name
# without wrapper then it will return the name of the returned function name which decorator is retuning.
# that is why when we make custom decorators we should use wraps class from functools.

@decor
def some_fun():
    """
    This is Doc String
    # https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
    """
    ...

print(some_fun.__name__)
print(some_fun.__doc__)

# Let's use wrap module
from functools import wraps
from typing import Callable # I've imported Callable because 
# I wanted to type hint like this def some_deco_fun(some_arg: function)-> function: # since that argument should be function and it should return function, 
# but type hinting as function is invalid syntax, so I imported Callable (which will help me doing type hinting that some_arg should be some Callable type)


def some_deco_fun(some_arg: Callable)-> Callable:
    """
    This is Custom Decorator.

    Args: one argument which will be a function
    
    Return value: it returns a function which is defined inside it.
    """
    
    @wraps(some_arg)
    def wrapper(*args, **kwargs): # This *args and **kwargs will the postional arguments defined in that function where we are attaching deco
        print(f"This is a wrapper function \nAnd this is argument you passed: {args}")
        #now we want to call the that function which is passing in some_deco_fun, but with argument and keyword argument just in case if that function need it.
        some_arg(*args, **kwargs)
    
    # now we want to return wrapper function which we defined
    return wrapper

@some_deco_fun
def wrapper_test_fun(param):
    """This is a function which is using custom decorator"""
    ...

if __name__ == '__main__':
    wrapper_test_fun('Ashish')

    # so now we can get the name and doc string from the actual function
    print(wrapper_test_fun.__name__)
    print(wrapper_test_fun.__doc__)