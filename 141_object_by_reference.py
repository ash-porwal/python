"""
Question is - Is Python Object by reference or Object by value?

Ans - Python programming uses "pass by reference object" concept while passing values to the functions.

Understanding Object References in Python

    Variable Assignment:
        When you assign a value to a variable, you are essentially creating a reference to an object in memory.
"""

# For example -
a = [1, 2, 3]
b = a
# Here, both a and b reference the same list object in memory.

"""
    Mutability:
        If the object is mutable (e.g., lists, dictionaries), 
        changes made through one reference will affect the object itself and be visible through all other references.

    Immutability:
        If the object is immutable (e.g., integers, strings, tuples), 
        assigning a new value to a variable creates a new object in memory, 
        and the variable reference is updated to this new object.

        # For Example-
        x = 10
        y = x
        x = 20
        print(y)  # Output: 10
"""

"""
    Function Arguments:
        When you pass an argument to a function, Python passes a reference to the object, not the object itself:

        Mutable Objects: Changes to a mutable object within a function will affect the original object.

        # Example
        def modify_list(lst):
            lst.append(4)

        my_list = [1, 2, 3]
        modify_list(my_list)
        print(my_list)  # Output: [1, 2, 3, 4]



    Immutable Objects:
        Assigning a new value to an immutable object within a function does not affect the original object.

        # Example
        def modify_value(val):
            val = 20

        x = 10
        modify_value(x)
        print(x)  # Output: 10
"""
