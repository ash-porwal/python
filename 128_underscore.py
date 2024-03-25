# 1. Single Underscore as a Name:
#    Throwaway Variable: Often used to indicate a variable that we don't intend to use.
for _ in range(5):
    print("Hello, World!")

# 2. Interpreter Variable: 
# In the Python REPL (opens up when you run python3 in terminal), 
# the single underscore is used to store the result of the last executed expression.
"""
>>> 5 + 6
11
>>> _ #This underscore will take the result we got from above
11
"""

# 3. Single Leading Underscore in Names:
# Suggests a "private" or "protected" variable, method, or attribute.
class MyClass:
    def __init__(self):
        self._private_var = 10

# 4. Underscores in Numbers (Python 3.6+):
#    Used for "digit grouping" to make large numbers more readable. 
#    These underscores have no effect on the value of the number
one_million = 1_000_000
hex_value = 0xDEAD_BEEF

# 5.    Double Underscore in Magic Variables:
#       Variables like __name__ and __file__ have specific meanings in Python.
#
#       __name__: If a Python file is run, this variable will be "__main__". 
#                 If the file is imported, it will contain the name of the file/module.
#       __file__: Contains the path of the script that's currently being executed.

# Unpacking iterable
t = (1, 2, 3, 4, 5) #could be list too
a, *b, c = t
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5
