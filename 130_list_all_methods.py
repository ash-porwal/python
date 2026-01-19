"""
All list methods – Python 3.11
==============================

This module documents commonly used Python list (`list`) methods.

General Notes
-------------
• Lists are ordered, mutable collections.
• Lists can contain mixed data types.
• Some methods modify the list in place.
• Some methods return values (e.g., pop, index).

General Syntax
--------------
result = list_object.method(param1, param2, ...)
"""

# ---------------------------------------------------------------------
# SAMPLE LIST
# ---------------------------------------------------------------------

lst = [1, 2, 3]

# ---------------------------------------------------------------------
# LIST METHODS
# ---------------------------------------------------------------------

# append()
# Syntax: list.append(element)
# Adds an element to the end of the list
# Returns: None
lst.append(4)
print("After append:", lst)  # [1, 2, 3, 4]

# clear()
# Syntax: list.clear()
# Removes all elements from the list
# Returns: None
lst.clear()
print("After clear:", lst)  # []

# copy()
# Syntax: list.copy()
# Returns: list (shallow copy)
lst = [1, 2, 3]
lst_copy = lst.copy()
print("Copy:", lst_copy)  # [1, 2, 3]

# count()
# Syntax: list.count(value)
# Returns: int (number of occurrences)
lst = [1, 2, 3, 2, 4, 2]
print("Count of 2:", lst.count(2))  # 3

# extend()
# Syntax: list.extend(iterable)
# Adds elements from iterable to the list
# Returns: None
lst = [1, 2, 3]
lst.extend([4, 5])
print("After extend:", lst)  # [1, 2, 3, 4, 5]

# index()
# Syntax: list.index(value[, start[, end]])
# Returns: int (first matching index)
print("Index of 3:", lst.index(3))  # 2

# insert()
# Syntax: list.insert(index, element)
# Inserts element at specified index
# Returns: None
lst.insert(1, 'a')
print("After insert:", lst)  # [1, 'a', 2, 3, 4, 5]

# pop()
# Syntax: list.pop([index])
# Removes and returns element at index (default = last)
# Raises IndexError if list is empty or index invalid
element = lst.pop(1)
print("Popped element:", element)  # 'a'
print("After pop:", lst)  # [1, 2, 3, 4, 5]

# remove()
# Syntax: list.remove(value)
# Removes first occurrence of value
# Raises ValueError if value not found
lst.remove(3)
print("After remove:", lst)  # [1, 2, 4, 5]

# reverse()
# Syntax: list.reverse()
# Reverses list in place
# Returns: None
lst.reverse()
print("After reverse:", lst)  # [5, 4, 2, 1]

# sort()
# Syntax: list.sort(*, key=None, reverse=False)
# Sorts list in ascending order by default
# Returns: None
lst = [3, 1, 4, 1, 5, 9, 2]
lst.sort()
print("After sort:", lst)  # [1, 1, 2, 3, 4, 5, 9]

# ---------------------------------------------------------------------
# DEL STATEMENT (not a method, but commonly used with lists)
# ---------------------------------------------------------------------

# del removes items by index or slice (does NOT return a value)

lst = [1, 2, 3, 4]
del lst[3]
print("After del index:", lst)  # [1, 2, 3]

lst = [1, 2, 3, 4]
del lst[-1]
print("After del negative index:", lst)  # [1, 2, 3]

lst = ["D", "T", "W", "J"]
del lst[1:3]
print("After del slice:", lst)  # ['D', 'J']

# ---------------------------------------------------------------------
# COMMON ERRORS
# ---------------------------------------------------------------------
"""
>>> [].pop()
IndexError: pop from empty list

>>> [1, 2].remove(99)
ValueError: list.remove(x): x not in list

>>> l = [1, 2, 3]
>>> del l[10]
IndexError: list assignment index out of range
"""

# ---------------------------------------------------------------------
# FAQ
# ---------------------------------------------------------------------
"""
Q: How do you remove an item by index?
A: Use pop() (returns value) or del (no return)

Q: Difference between remove() and pop()?
A: remove() deletes by value, pop() deletes by index

Q: How do you delete multiple items at once?
A: Use del with slicing
"""
