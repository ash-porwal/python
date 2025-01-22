'''
built in functions like - all(), any(), len(), sorted() etc.

here is quick summary:

all()	Returns True if all the items in an iterable are truthy and False otherwise.
any()	Returns True if at least one element in the iterable is truthy and False otherwise.
len()	Returns an integer representing the number of items in the input object.
max()	Returns the largest value in an iterable or series of arguments.
min()	Returns the smallest value in an iterable or series of arguments.
sorted()	Returns a new sorted list of the elements in the iterable.
sum()	Returns the sum of a start value and the values in the input iterable from left to right.
'''

# Examples:
'''
- all() and any()
------------------
>>> inventory = {"apple": 100, "orange": 80, "banana": 100, "mango": 200}

>>> all(inventory.values())
True

>>> # Update the stock
>>> inventory["mango"] = 0
>>> all(inventory.values())
False

- len()
------------------
>>> MLB_teams = {
...     "Colorado": "Rockies",
...     "Chicago": "White Sox",
...     "Boston": "Red Sox",
...     "Minnesota": "Twins",
...     "Milwaukee": "Brewers",
...     "Seattle": "Mariners",
... }

>>> len(MLB_teams)
6

- min() and max()
------------------
>>> computer_parts = {
...     "CPU": 299.99,
...     "Motherboard": 149.99,
...     "RAM": 89.99,
...     "GPU": 499.99,
...     "SSD": 129.99,
...     "Power Supply": 79.99,
...     "Case": 99.99,
...     "Cooling System": 59.99,
... }

>>> min(computer_parts.values())
59.99
>>> max(computer_parts.values())
499.99
'''

# sorting dict
# we can use the built-in sorted() function to sort a dictionary
'''
>>> students = {
...     "Alice": 89.5,
...     "Bob": 76.0,
...     "Charlie": 92.3,
...     "Diana": 84.7,
...     "Ethan": 88.9,
...     "Fiona": 95.6,
...     "George": 73.4,
...     "Hannah": 81.2,
... }

# The sorted() function returns a list of sorted values, so you wrap its call with dict() 
to build a new sorted dictionary. Below it sorted on their values
>>> dict(sorted(students.items(), key=lambda item: item[1]))
{
    'George': 73.4,
    'Bob': 76.0,
    'Hannah': 81.2,
    'Diana': 84.7,
    'Ethan': 88.9,
    'Alice': 89.5,
    'Charlie': 92.3,
    'Fiona': 95.6
}

>>> dict(sorted(students.items(), key=lambda item: item[1], reverse=True))
{
    'Fiona': 95.6,
    'Charlie': 92.3,
    'Alice': 89.5,
    'Ethan': 88.9,
    'Diana': 84.7,
    'Hannah': 81.2,
    'Bob': 76.0,
    'George': 73.4
}
'''

# we can also sort with keys of dictonary
'''
>>> dict(sorted(students.items(), key=lambda item: item[0]))
{
    'Alice': 89.5,
    'Bob': 76.0,
    'Charlie': 92.3,
    'Diana': 84.7,
    'Ethan': 88.9,
    'Fiona': 95.6,
    'George': 73.4,
    'Hannah': 81.2
}
'''


# We can use the sum() function to add the values of a dict
'''
>>> daily_sales = {
...     "Monday": 1500,
...     "Tuesday": 1750,
...     "Wednesday": 1600,
...     "Thursday": 1800,
...     "Friday": 2000,
...     "Saturday": 2200,
...     "Sunday": 2100,
... }

>>> sum(daily_sales.values()) / len(daily_sales)
1850.0
'''