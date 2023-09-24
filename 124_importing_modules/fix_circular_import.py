import importlib

def some_function():
    module_b = importlib.import_module("module_b")
    module_b.function_b()
some_function()