"""
Dict methods - Python3.11
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
"""
dictionary = {1: 'a', 2: 'b', 3: 'c'}

# clear() - Removes all items from the dictionary
dictionary.clear()
print("After clear:", dictionary)  # After clear: {}

# copy() - Returns a shallow copy of the dictionary
dictionary = {1: 'a', 2: 'b', 3: 'c'} # creating new dictionary as we cleared above
copy_dict = dictionary.copy()
print("Copy of dictionary:", copy_dict)  # Copy of dictionary: {1: 'a', 2: 'b', 3: 'c'}

# fromkeys() - Creates a new dictionary from the given sequence of keys with a value provided by the user
new_dict = dict.fromkeys([1, 2, 3], 'value') # we need to provide keys as a list
print("New dictionary from keys:", new_dict)  # New dictionary from keys: {1: 'value', 2: 'value', 3: 'value'}

# get() - Returns the value for the specified key if the key is in the dictionary
# and if key is not present then get will return None
print("Get value for key 2:", dictionary.get(2))  # Get value for key 2: b

# items() - Returns a view object that displays a list of dictionary's key-value tuple pairs
print("Dictionary items:", list(dictionary.items()))  # Dictionary items: [(1, 'a'), (2, 'b'), (3, 'c')]

# keys() - Returns a view object that displays a list of all the keys in the dictionary
print("Dictionary keys:", list(dictionary.keys()))  # Dictionary keys: [1, 2, 3]

# popitem() - Removes the last inserted key-value pair
# We cannot use popitem() to remove a specific item by key in a dictionary. 
# The popitem() method is designed to remove and return the last inserted item from the dictionary, 
# and it does not allow you to specify which item to remove.
dictionary = {1: 'a', 2: 'b', 3: 'c'}
popped_item = dictionary.popitem()
print("Popped item:", popped_item)  # Popped item: (3, 'c')
print("Dictionary after popitem:", dictionary)  # Dictionary after popitem: {1: 'a', 2: 'b'}
# If you want to remove the first added item instead
# 
# popped_item = dictionary.popitem(last=False)

# pop() - Removes the element with the specified key
# we can also remove last index using pop even if we dont know last key
"""
dictionary = {1: 'a', 2: 'b', 3: 'c'}

# Identify the last key
last_key = list(dictionary.keys())[-1] # Since Python 3.7, dictionaries are guaranteed to maintain insertion order. This means that when you iterate over the dictionary keys, items, or values, they will be returned in the order in which they were added to the dictionary. 

# Use pop to remove the last item
removed_value = dictionary.pop(last_key)
print(f"Removed ({last_key}: '{removed_value}')")
print(f"Remaining dictionary: {dictionary}")

"""
popped_value = dictionary.pop(2)
print("Popped value:", popped_value)  # Popped value: b
print("Dictionary after pop:", dictionary)  # Dictionary after pop: {1: 'a', 3: 'c'}

"""
However, in versions of Python before 3.6, dictionaries do not maintain any specific order. 
For Python 3.6 or earlier, we cannot rely on the order of elements in a standard dictionary. 
For these versions, to maintain order, we would need to use collections.OrderedDict, 
which explicitly preserves the order in which items are added.


from collections import OrderedDict

# Creating an OrderedDict
ordered_dict = OrderedDict()
ordered_dict['one'] = 1
ordered_dict['two'] = 2
ordered_dict['three'] = 3

print("Original OrderedDict:")
for key, value in ordered_dict.items():
    print(key, value)

# Removing the last item
ordered_dict.popitem(last=True)  # By default last=True, which removes the last added item

print("\nOrderedDict after removing the last item:")
for key, value in ordered_dict.items():
    print(key, value)

# Adding a new item
ordered_dict['four'] = 4

print("\nOrderedDict after adding a new item:")
for key, value in ordered_dict.items():
    print(key, value)

# If you want to remove the first added item instead
# ordered_dict.popitem(last=False)

"""

# setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
default_value = dictionary.setdefault(4, 'd')
print("Set default value:", default_value)  # Set default value: d
print("Dictionary after setdefault:", dictionary)  # Dictionary after setdefault: {1: 'a', 2: 'b', 4: 'd'}

# update() - Updates the dictionary with the specified key-value pairs
dictionary.update({5: 'e'})
print("Dictionary after update:", dictionary)  # Dictionary after update: {1: 'a', 2: 'b', 4: 'd', 5: 'e'}

# values() - Returns a view object that displays a list of all the values in the dictionary
print("Dictionary values:", list(dictionary.values()))  # Dictionary values: ['a', 'b', 'd', 'e']
