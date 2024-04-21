# Overloading is - when we define the same function multiple times
# but each time we define the same function with different parameters
# this is function overloading and python will call that function accoridng to
# the arguments passed in that function.

# In Python, if you define a function more than once with the same name but different parameters, 
# the last definition will overwrite the previous ones

# so we can achieve this functionality similar to function overloading in Python

def greet(*args):
    if len(args) == 1:
        print(f"Hello, {args[0]}")
    elif len(args) == 2:
        print(f"{args[1]}, {args[0]}")
    else:
        print("Incorrect number of arguments")

# Function calls
greet("Alice")                      # Outputs: Hello, Alice
greet("Alice", "Good morning")      # Outputs: Good morning, Alice
greet()                             # Outputs: Incorrect number of arguments