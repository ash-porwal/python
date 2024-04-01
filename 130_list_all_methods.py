""" 
All list methods - Python3.11
 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""


# append: Adds an element to the end of the list.
lst = [1, 2, 3]
lst.append(4)
print(lst)  # Output: [1, 2, 3, 4]

# clear: Removes all the elements from the list.
lst.clear()
print(lst)  # Output: []

# copy: Returns a shallow copy of the list.
lst = [1, 2, 3]
lst_copy = lst.copy()
print(lst_copy)  # Output: [1, 2, 3]

# count: Returns the number of elements with the specified value.
lst = [1, 2, 3, 2, 4, 2]
print(lst.count(2))  # Output: 3

# extend: Add the elements of a list (or any iterable) to the end of the current list.
lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)  # Output: [1, 2, 3, 4, 5]

# index: Returns the index of the first element with the specified value.
print(lst.index(3))  # Output: 2

# insert: Adds an element at the specified position.
lst.insert(1, 'a')
print(lst)  # Output: [1, 'a', 2, 3, 4, 5]

# pop: Removes the element at the specified position and returns it.
element = lst.pop(1)
print(element)  # Output: 'a'
print(lst)      # Output: [1, 2, 3, 4, 5]

# remove: Removes the first item with the specified value.
lst.remove(3)
print(lst)  # Output: [1, 2, 4, 5]

# reverse: Reverses the order of the list.
lst.reverse()
print(lst)  # Output: [5, 4, 2, 1]

# sort: Sorts the list.
lst = [3, 1, 4, 1, 5, 9, 2]
lst.sort()
print(lst)  # Output: [1, 1, 2, 3, 4, 5, 9]
