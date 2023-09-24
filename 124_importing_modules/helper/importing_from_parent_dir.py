# in this I will import module from parent directory

# this is called Relative Import Statement:
"""
To use relative imports, the directory you're importing from and the directory 
you're importing into both need to be Python packages. 
This means they both need to contain an __init__.py file (which can be empty).

# But relative path never works for me

# so I am gonna use sys.path.append
"""

# adding that path to Python path
import sys
sys.path.append("/home/ashporwal/hdd/lab/programmes/Python/python/124_importing_modules/")
# from .. import some_class # this never works for me
import some_class

def some_helper_function():
    s = some_class.SomeClassName()
    s.func1()

if __name__ == "__main__":
    some_helper_function()