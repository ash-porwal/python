# the del keyword is used to delete objects

x = 10
print(x)  # This will print 10

del x
# print(x)  # Uncommenting this will raise a NameError because x is no longer defined


# Delete an Item from a List:
fruits = ["apple", "banana", "cherry"]
del fruits[1]
print(fruits)  # This will print ['apple', 'cherry']

# Delete a Slice from a List:
numbers = [1, 2, 3, 4, 5]
del numbers[1:4]
print(numbers)  # This will print [1, 5]


# Delete a Key from a Dictionary:
person = {"name": "John", "age": 30, "city": "New York"}
del person["age"]
print(person)  # This will print {'name': 'John', 'city': 'New York'}


"""
Remember, del just removes the reference to the object. 
If that reference was the last one, the Python garbage collector will reclaim the memory. 
If there are other references to the same object, the object will stay alive.
"""

"""

In Python, when you create an object, variables that are assigned to this object don't hold the object value itself; 
instead, they hold a reference (a pointer) to the location in memory where the object is stored.

The del statement deletes the reference, not the object itself. 
The Python garbage collector will delete the object and free the memory only when there are no references left pointing to that object.
"""

# Here we create a list
original_list = [1, 2, 3]

# This does not create a new list. It creates another reference (alias) pointing to the same list.
alias_list = original_list

# At this point, both original_list and alias_list point to the same list in memory.

# Deleting one reference
del original_list

# Even though we've deleted original_list, the list [1, 2, 3] still exists in memory
# because alias_list is still referencing it.
print(alias_list)  # This will print [1, 2, 3]

# Now, let's delete alias_list as well
del alias_list

# Now that all references to the list [1, 2, 3] are gone, the Python garbage collector
# can free the memory occupied by this list.
