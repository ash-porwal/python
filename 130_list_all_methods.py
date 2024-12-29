""" 
All list methods - Python3.11
 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

# -----------------------------------------------------------------------
# append: Adds an element to the end of the list.
lst = [1, 2, 3]
lst.append(4)
print(lst)  # Output: [1, 2, 3, 4]
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# clear: Removes all the elements from the list.
lst.clear()
print(lst)  # Output: []
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# copy: Returns a shallow copy of the list.
lst = [1, 2, 3]
lst_copy = lst.copy()
print(lst_copy)  # Output: [1, 2, 3]
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# count: Returns the number of elements with the specified value.
lst = [1, 2, 3, 2, 4, 2]
print(lst.count(2))  # Output: 3
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# extend: Add the elements of a list (or any iterable) to the end of the current list.
lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)  # Output: [1, 2, 3, 4, 5]
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# index: Returns the index of the first element with the specified value.
print(lst.index(3))  # Output: 2
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# insert: Adds an element at the specified position.
lst.insert(1, 'a')
print(lst)  # Output: [1, 'a', 2, 3, 4, 5]
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# pop: Removes the element at the specified position and returns it, so we can pass any index
#      which we want to remove, by default it takes last index and removes it and return it.
# so, if we want to remove element by index or remove certain position element then we use pop()
element = lst.pop(1)
print(element)  # Output: 'a'
print(lst)      # Output: [1, 2, 3, 4, 5]
# If you call the .pop() method on an empty list or if mention that index which don't exists then 
# the method will raise an IndexError
"""
>>> temp = []
>>> temp.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list
>>> 
"""
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# Deleting items with del statement in a List
# del is similar to pop(), it also removes items based on the position
# but it doesn't return a value
"""
>>> l = [1,2,3,4]
>>> del l[3]
>>> l
[1, 2, 3]
"""
# with del statement, we can also use negative indexing
"""
>>> l = [1,2,3,4]
>>> del l[-1]
>>> l
[1, 2, 3]
>>> 
"""
# Note: If you need to store the removed value for any reason, then use the .pop() method instead.

# Similar to the .pop() method, you’ll get an IndexError exception 
# if you attempt to use del on a list with an invalid index
"""
>>> l = [1,2,3,4]
>>> del l[50]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> 
"""

# in pop() method if we don't specify the index then it takes default index which is -1
# but in del statement we need to specify index, if we don't then SyntaxError is gonna raise.
"""
>>> l = [1,2,3,4]
>>> del l[]
  File "<input>", line 1
    del l[]
          ^
SyntaxError: invalid syntax
"""

# With del statement we can delete the portion of a list as well
# so, we need to pass slicing of list from where to where we want to remove
"""
>>> temp_list = ["D", "T", "W", "J"]
>>> del temp_list[1:3]
>>> temp_list
['D', 'J']

"""
# we can also delete using negative indexing
"""
>>> temp_list = ["D", "T", "W", "J"]
>>> del temp_list[-3:-1]
>>> temp_list
['D', 'J']
"""
# Explain of above: 
#   you delete temp_list starting from index -3("T")
#   and up to, but not including the item at index -1 ("J")
# -----------------------------------------------------------------------


# -----------------------------------------------------------------------
# remove: Removes the first item with the specified value.
# so, if we plan to remove item from a list by its value rather than by its index, we use remove()
lst.remove(3)
print(lst)  # Output: [1, 2, 4, 5]
# in case if we specify the value which doesn't exists in the list then it raise - ValueError
"""
>>> temp_list = ["D", "T", "W", "J"]
>>> temp_list.remove("z")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
"""
# Also in pop we need to specify a value, it doesn't have any default value
# -----------------------------------------------------------------------


# -----------------------------------------------------------------------
# reverse: Reverses the order of the list.
lst.reverse()
print(lst)  # Output: [5, 4, 2, 1]
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# sort: Sorts the list.
lst = [3, 1, 4, 1, 5, 9, 2]
lst.sort()
print(lst)  # Output: [1, 1, 2, 3, 4, 5, 9]
# -----------------------------------------------------------------------


# -----------------------------------------------------------------------
# Frequently Asked question
"""
- How you can remove an item from a list by its index?
    we can use pop() or del statement, 
    pop() removes and returns the item
    while del statement only removes the item without returning it.

- What is the difference between .remove() and .pop()
    remove() method removes value by its position
    pop() removes by index

- How do you delete multiple items from a list at once?
    we can use del statement with a slice specified the start and end indices
"""