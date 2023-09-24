# first make sure from whatever directory you are importing from, there should be __init__.py file

# from <dir_name>.<file_name> import <class name>
from helper.helper_py_file import HelperClass

h = HelperClass
h.helper_fun()

# ---------------------------------------------------------------
from helper import importing_from_parent_dir

obj = importing_from_parent_dir.some_helper_function()
obj.func1