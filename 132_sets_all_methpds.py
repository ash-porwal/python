"""
Sets all methods - Python 3.11
==============================

This module documents commonly used Python set (`set`) methods.

General Notes
-------------
• Sets store unordered, unique elements.
• Sets are mutable.
• Many methods modify the set in place.
• Some methods return new sets, others return None.

General Syntax
--------------
result = set_object.method(param1, param2, ...)
"""

# ---------------------------------------------------------------------
# SAMPLE SETS
# ---------------------------------------------------------------------

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# ---------------------------------------------------------------------
# SET METHODS
# ---------------------------------------------------------------------

# add()
# Syntax: set.add(element)
# element: required
# Returns: None
set1.add(5)
print("After add:", set1)  # {1, 2, 3, 4, 5}

# clear()
# Syntax: set.clear()
# Returns: None
set1.clear()
print("After clear:", set1)  # set()

# copy()
# Syntax: set.copy()
# Returns: set (shallow copy)
set1 = {1, 2, 3, 4}
set_copy = set1.copy()
print("Copy:", set_copy)  # {1, 2, 3, 4}

# difference()
# Syntax: set.difference(*others)
# Returns: set
print("Difference:", set1.difference(set2))  # {1, 2}

# difference_update()
# Syntax: set.difference_update(*others)
# Returns: None
set1.difference_update(set2)
print("After difference_update:", set1)  # {1, 2}

# discard()
# Syntax: set.discard(element)
# Returns: None (no error if element missing)
set1 = {1, 2, 3, 4}
set1.discard(4)
print("After discard:", set1)  # {1, 2, 3}

# intersection()
# Syntax: set.intersection(*others)
# Returns: set
print("Intersection:", set1.intersection(set2))  # {3}

# intersection_update()
# Syntax: set.intersection_update(*others)
# Returns: None
set1.intersection_update(set2)
print("After intersection_update:", set1)  # {3}

# isdisjoint()
# Syntax: set.isdisjoint(other)
# Returns: bool
print("Isdisjoint:", set1.isdisjoint(set2))  # False

# issubset()
# Syntax: set.issubset(other)
# Returns: bool
print("Issubset:", set1.issubset(set2))  # True

# issuperset()
# Syntax: set.issuperset(other)
# Returns: bool
print("Issuperset:", set2.issuperset(set1))  # True

# pop()
# Syntax: set.pop()
# Returns: element (arbitrary)
set1 = {1, 2, 3, 4}
print("Pop:", set1.pop())  # Removes and returns an arbitrary element

# remove()
# Syntax: set.remove(element)
# Returns: None (raises KeyError if missing)
set1.remove(3)
print("After remove:", set1)  # {1, 2, 4} (order may vary)

# symmetric_difference()
# Syntax: set.symmetric_difference(other)
# Returns: set
print("Symmetric difference:", set1.symmetric_difference(set2))  # {1, 2, 5, 6}

# symmetric_difference_update()
# Syntax: set.symmetric_difference_update(other)
# Returns: None
set1.symmetric_difference_update(set2)
print("After symmetric_difference_update:", set1)  # {1, 2, 5, 6}

# union()
# Syntax: set.union(*others)
# Returns: set
print("Union:", set1.union(set2))  # {1, 2, 3, 4, 5, 6}

# update()
# Syntax: set.update(*others)
# Returns: None
set1.update({7, 8})
print("After update:", set1)  # {1, 2, 5, 6, 7, 8}
