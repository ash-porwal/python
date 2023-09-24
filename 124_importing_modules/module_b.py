# These files file create circular import error

from module_a import function_a

def function_b():
    print("Function B")
    function_a()
