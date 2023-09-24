# importing a function from a different file in the same path

from some_fun import first_func

print(first_func())


# ------------------------------------------------------------
# or we can just import the file name
print()

import some_fun
print(some_fun.first_func())

"""
######### Conditions and Caveats for Importing #########

1. Python Path (sys.path): 
    - Python has a list of directories it looks in, to find modules to import. 
    By default, this list includes the current directory, the site-packages directory, and some other standard directories. 
    If your module is not in one of these directories, 
    Python won't find it unless you modify sys.path or set the PYTHONPATH environment variable.

2. Cyclic Imports: 
    - If module A imports module B and module B imports module A, you have cyclic imports. 
    It can sometimes lead to problems if not handled properly.

3. __name__ and __main__: 
    - When a Python file is run, its __name__ attribute is set to '__main__'. 
    When the same module is imported elsewhere, its __name__ attribute is set to the module's name. 
    This distinction can be useful, for example, to write code that can both be executed directly and imported elsewhere:

4. Reloading Modules: 
    - If you make changes to a module after importing it, you'll need to either restart your Python session 
    or use the reload() function from the importlib module to reflect the changes.

5. Directory as a Module: 
    - If you have a directory with an __init__.py file, Python treats it as a package, 
    and you can import modules from this directory. 
    The __init__.py file can be empty or can contain initialization code for your package.
    Whenever import is done, Pyhton runs init file

6. Local vs. Global Import: 
    - While it's common to import modules at the top of a file, you can also import inside functions. 
    This might make the function's performance faster if the import is heavy and the function is not always called. 
    However, typically, imports are placed at the top for clarity and style reasons.
"""

# ------------------------------------------------------------
# importing a class
print()

from some_class import SomeClassName

s = SomeClassName
s.func1()

"""
In Python, module names should not contain hyphens because they cannot be imported directly 
using the regular import statement with hyphens. 
Instead, use underscores (_). 
So, importing_from_parent_dir.py is fine, but if you had something like importing-from-parent-dir.py, that would be problematic.
"""