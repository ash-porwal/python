# These files file create circular import error

# To fix it I wrote a new file where I used importlib: fix_module_a and fix_module_b

from module_b import function_b

def function_a():
    print("Function A")
    function_b()
