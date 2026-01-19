"""
Dict methods - Python 3.11
==========================

This module documents commonly used Python dictionary (`dict`) methods.

General Notes
-------------
• Dictionaries store key-value pairs.
• Keys must be immutable and unique.
• Dictionaries are mutable.
• Since Python 3.7, dictionaries preserve insertion order.
• Some methods modify the dictionary in place; others return views or values.

# ---------------------------------------------------------------------
# ORDER NOTE (Python 3.7+)
# ---------------------------------------------------------------------
# Dictionaries preserve insertion order.
# The "last inserted item" is well-defined for popitem().

General Syntax
--------------
result = dict_object.method(param1, param2, ...)
"""

# ---------------------------------------------------------------------
# SAMPLE DICTIONARY
# ---------------------------------------------------------------------

dictionary = {1: 'a', 2: 'b', 3: 'c'}

# ---------------------------------------------------------------------
# DICT METHODS
# ---------------------------------------------------------------------

# clear()
# Syntax: dict.clear()
# Removes all items from the dictionary
# Returns: None
dictionary.clear()
print("After clear:", dictionary)  # {}

# copy()
# Syntax: dict.copy()
# Returns: dict (shallow copy)
dictionary = {1: 'a', 2: 'b', 3: 'c'}
copy_dict = dictionary.copy()
print("Copy of dictionary:", copy_dict)  # {1: 'a', 2: 'b', 3: 'c'}

# fromkeys()
# Syntax: dict.fromkeys(iterable, value=None)
# iterable: required (keys)
# value: optional (default = None)
# Returns: new dict
new_dict = dict.fromkeys([1, 2, 3], 'value')
print("New dictionary from keys:", new_dict)  # {1: 'value', 2: 'value', 3: 'value'}

# get()
# Syntax: dict.get(key, default=None)
# Returns: value if key exists, else default
print("Get value for key 2:", dictionary.get(2))  # b
print("Get missing key:", dictionary.get(99))  # None

# items()
# Syntax: dict.items()
# Returns: view object of (key, value) tuples
print("Dictionary items:", list(dictionary.items()))
# [(1, 'a'), (2, 'b'), (3, 'c')]

# keys()
# Syntax: dict.keys()
# Returns: view object of keys
print("Dictionary keys:", list(dictionary.keys()))  # [1, 2, 3]

# popitem()
# Syntax: dict.popitem()
# Removes and returns the last inserted key-value pair
# Returns: tuple (key, value)
dictionary = {1: 'a', 2: 'b', 3: 'c'}
popped_item = dictionary.popitem()
print("Popped item:", popped_item)  # (3, 'c')
print("After popitem:", dictionary)  # {1: 'a', 2: 'b'}

# pop()
# Syntax: dict.pop(key[, default])
# Removes specified key and returns its value
dictionary = {1: 'a', 2: 'b', 3: 'c'}
popped_value = dictionary.pop(2)
print("Popped value:", popped_value)  # b
print("After pop:", dictionary)  # {1: 'a', 3: 'c'}

# pop() with default (avoids KeyError)
print("Pop missing key:", dictionary.pop(99, "not found"))  # not found

# setdefault()
# Syntax: dict.setdefault(key, default=None)
# If key exists: returns its value
# If key missing: inserts key with default value
dictionary = {1: 'a', 2: 'b'}
default_value = dictionary.setdefault(3, 'c')
print("Set default value:", default_value)  # c
print("After setdefault:", dictionary)  # {1: 'a', 2: 'b', 3: 'c'}

# update()
# Syntax: dict.update(other_dict or iterable)
# Updates dictionary with new key-value pairs
dictionary.update({4: 'd', 5: 'e'})
print("After update:", dictionary)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# values()
# Syntax: dict.values()
# Returns: view object of values
print("Dictionary values:", list(dictionary.values()))
# ['a', 'b', 'c', 'd', 'e']
