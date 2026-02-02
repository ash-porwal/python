"""
Sets all methods - Python 3.11
==============================

This module documents commonly used Python set (`set`) methods.

General Notes
-------------
• Sets are mutable.
• Sets are unordered
• Does not support indexing
• Set contains unique elements.
• Many methods modify the set in place.
• Some methods return new sets, others return None.

General Notes on Frozen set
-------------
• Frozen set Unordered and immutable
• Frozen set Stores unique elements
• Frozen set Can be used as dictionary keys or elements of another set
• Frozen sets are hashable
    (An object is hashable if it has a hash value that never changes during its lifetime
        and it can be compared for equality.
        Mutable objects cannot be hashable, because their content can change)
we create fs = frozenset([1, 2, 3])


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

# -------------------------------
# add()
# Syntax: set.add(element)
# Adds a single element to the set
# If element already exists → no change
# Modifies the set
# Returns: None
# -------------------------------
set1 = {1, 2, 3, 4}
set1.add(5)
print("After add:", set1)   # {1, 2, 3, 4, 5}


# -------------------------------
# clear()
# Syntax: set.clear()
# Removes ALL elements from the set
# Modifies the set
# Returns: None
# -------------------------------
set1.clear()
print("After clear:", set1)   # set()


# -------------------------------
# copy()
# Syntax: set.copy()
# Creates a shallow copy of the set
# Original set remains unchanged
# Returns: new set
# -------------------------------
set1 = {1, 2, 3, 4}
set_copy = set1.copy()
print("Copy:", set_copy)      # {1, 2, 3, 4}
print("Original:", set1)      # {1, 2, 3, 4}


# -------------------------------
# difference()
# Syntax: set.difference(other)
# Returns elements present in set1 BUT NOT in set2
# Does NOT modify original sets
# Returns: new set
# -------------------------------
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Difference:", set1.difference(set2))   # {1, 2}
print("set1 unchanged:", set1)                 # {1, 2, 3, 4}


# -------------------------------
# difference_update()
# Syntax: set.difference_update(other)
# Removes elements found in set2 FROM set1
# Modifies set1 in place
# Returns: None
# -------------------------------
set1.difference_update(set2)
print("After difference_update:", set1)   # {1, 2}


# -------------------------------
# discard()
# Removes element if present
# No error if element is missing
# Modifies set
# Returns: None
# -------------------------------
set1 = {1, 2, 3, 4}
set1.discard(4)
set1.discard(10)          # no error
print("discard:", set1)   # {1, 2, 3}


# -------------------------------
# intersection()
# Returns common elements
# Does NOT modify original sets
# Returns: new set
# -------------------------------
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("intersection:", set1.intersection(set2))   # {3, 4}


# -------------------------------
# intersection_update()
# Keeps only common elements in set1
# Modifies set1
# Returns: None
# -------------------------------
set1 = {1, 2, 3, 4}
set1.intersection_update(set2)
print("intersection_update:", set1)   # {3, 4}


# -------------------------------
# isdisjoint()
# True if NO common elements
# Returns: bool
# -------------------------------
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("isdisjoint:", set1.isdisjoint(set2))   # False


# -------------------------------
# issubset()
# True if all elements of set1 are in set2
# Returns: bool
# -------------------------------
set1 = {3, 4}
set2 = {1, 2, 3, 4, 5}
print("issubset:", set1.issubset(set2))   # True


# -------------------------------
# issuperset()
# True if set2 contains all elements of set1
# Returns: bool
# -------------------------------
print("issuperset:", set2.issuperset(set1))   # True


# -------------------------------
# pop()
# Removes and returns an arbitrary element(any element chosen by Python)
# Modifies set
# -------------------------------
set1 = {1, 2, 3, 4}
print("pop:", set1.pop())
print("after pop:", set1)


# -------------------------------
# remove()
# Removes specified element
# Raises KeyError if missing
# Modifies set
# Returns: None
# -------------------------------
set1 = {1, 2, 3, 4}
set1.remove(3)
print("remove:", set1)   # {1, 2, 4}


# -------------------------------
# symmetric_difference()
# Elements in either set but NOT both
# Does NOT modify original sets
# Returns: new set
# -------------------------------
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("symmetric_difference:", set1.symmetric_difference(set2))   # {1, 2, 5, 6}


# -------------------------------
# symmetric_difference_update()
# Keeps only non-common elements in set1
# Modifies set1
# Returns: None
# -------------------------------
set1 = {1, 2, 3, 4}
set1.symmetric_difference_update(set2)
print("symmetric_difference_update:", set1)   # {1, 2, 5, 6}


# -------------------------------
# union()
# Combines all elements (no duplicates)
# Does NOT modify original sets
# Returns: new set
# -------------------------------
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("union:", set1.union(set2))   # {1, 2, 3, 4, 5}


# -------------------------------
# update()
# Adds elements to set1
# Modifies set1
# Returns: None
# -------------------------------
set1 = {1, 2}
set1.update({3, 4, 5})
print("update:", set1)   # {1, 2, 3, 4, 5}
