"""
Sets all methods - Python3.11

'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
'symmetric_difference', 'symmetric_difference_update', 'union', 'update'
"""


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# add
set1.add(5)
print("After add:", set1)  # {1, 2, 3, 4, 5}

# clear
set1.clear()
print("After clear:", set1)  # set()

# copy
set1 = {1, 2, 3, 4}
set_copy = set1.copy()
print("Copy:", set_copy)  # {1, 2, 3, 4}

# difference
print("Difference:", set1.difference(set2))  # {1, 2}

# difference_update
set1.difference_update(set2)
print("After difference_update:", set1)  # {1, 2}

# discard
set1 = {1, 2, 3, 4}
set1.discard(4)
print("After discard:", set1)  # {1, 2, 3}

# intersection
print("Intersection:", set1.intersection(set2))  # {3}

# intersection_update
set1.intersection_update(set2)
print("After intersection_update:", set1)  # {3}

# isdisjoint
print("Isdisjoint:", set1.isdisjoint(set2))  # False

# issubset
print("Issubset:", set1.issubset(set2))  # True

# issuperset
print("Issuperset:", set2.issuperset(set1))  # True

# pop
set1 = {1, 2, 3, 4}
print("Pop:", set1.pop())  # Removes and returns an arbitrary element

# remove
set1.remove(3)
print("After remove:", set1)  # {1, 2, 4} (or similar depending on pop result)

# symmetric_difference
print("Symmetric difference:", set1.symmetric_difference(set2))  # {1, 2, 5, 6}

# symmetric_difference_update
set1.symmetric_difference_update(set2)
print("After symmetric_difference_update:", set1)  # {1, 2, 5, 6}

# union
print("Union:", set1.union(set2))  # {1, 2, 3, 4, 5, 6}

# update
set1.update({7, 8})
print("After update:", set1)  # {1, 2, 5, 6, 7, 8}
