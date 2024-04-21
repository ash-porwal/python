"""
With monkey patching we can modify class, function, varibale without actually modifying actual code.
"""


# Suppose we have a class defined in some module
class MyClass:
    def method(self):
        print("Original Method")

# Now in our application elsewhere, we decide to change the 'method' of MyClass
def new_method(self):
    print("Modified Method")

# Apply monkey patch
MyClass.method = new_method

# All instances of MyClass now use the new method
obj = MyClass()
obj.method()  # Outputs: "Modified Method"
