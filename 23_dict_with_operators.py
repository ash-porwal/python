'''
The membership operators in and not in allow you to determine whether a given key, value, 
or item is in a dictionary.

>>> MLB_teams = {
...     "Colorado": "Rockies",
...     "Chicago": "White Sox",
...     "Boston": "Red Sox",
...     "Minnesota": "Twins",
...     "Milwaukee": "Brewers",
...     "Seattle": "Mariners",
... }

>>> "Milwaukee" in MLB_teams
True
>>> "Indianapolis" in MLB_teams
False
>>> "Indianapolis" not in MLB_teams
True

>>> "Milwaukee" in MLB_teams.keys()
True
>>> "Indianapolis" in MLB_teams.keys()
False
>>> "Indianapolis" not in MLB_teams.keys()
True
'''

# with in/not in operator we can just know if that key is present in dict or not, if 
# directly using `in` operator on dictory, without using .keys() or .values()
'''
>>> d = {1:-1, 2:-2}
>>> 
>>> 2 in d
True
>>> -2 in d
False
>>> 
'''

# so, if we want to check if the value is present in dict or not then we should use
# .values
'''
>>> d = {1:-1, 2:-2}
>>> 
>>> -2 in d.values()
True
>>> 
'''

# so, from above we can conclude that if we want to know if some value is present in dict
# then we can use membership operator directly on dict variable, using .key() will work the 
# same but it is just redundant and slightly less efficient than using the dictionary directly.

#-------------------------------------------------------
### Equality(==) and Inequality(!=)
'''
>>> [1, 2, 3] == [3, 2, 1]
False
>>> {1: 1, 2: 2, 3: 3} == {3: 3, 2: 2, 1: 1}
True

>>> [1, 2, 3] != [3, 2, 1]
True
>>> {1: 1, 2: 2, 3: 3} != {3: 3, 2: 2, 1: 1}
False
'''

'''
These operators disregard element order when you use them with dictionaries, which is 
different from what happens with lists.

When you compare a list using the equality operator, the result depends on both the content 
and the order. In contrast, when you compare two dictionaries that contain the same series of 
key-value pairs, the order of those pairs isn’t considered. 
'''


#-------------------------------------------------------
### Union and Augmented Union: | and |=
'''
The union operator (|) creates a new dictionary by merging the keys and values of two initial 
dictionaries. The values of the dictionary to the right of the operator take precedence when 
both dictionaries share keys:

>>> default_config = {
...     "color": "green",
...     "width": 42,
...     "height": 100,
...     "font": "Courier",
... }

>>> user_config = {
...     "path": "/home",
...     "color": "red",
...     "font": "Arial",
...     "position": (200, 100),
... }

>>> config = default_config | user_config
>>> config
{
    'color': 'red',
    'width': 42,
    'height': 100,
    'font': 'Arial',
    'path': '/home',
    'position': (200, 100)
}
'''

'''
Similarly, the augmented union operator (|=) updates an existing dictionary with key-value 
pairs from another dictionary, mapping, or iterable of key-value pairs. Again, when the 
operands share keys, the values from the right-hand side operand take priorit

>>> config = {
...     "color": "green",
...     "width": 42,
...     "height": 100,
...     "font": "Courier",
... }

>>> user_config = {
...     "path": "/home",
...     "color": "red",
...     "font": "Arial",
...     "position": (200, 100),
... }

>>> config |= user_config
>>> config
{
    'color': 'red',
    'width': 42,
    'height': 100,
    'font': 'Arial',
    'path': '/home',
    'position': (200, 100)
}
'''