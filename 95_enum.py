# Enum allows us to define constant values
'''
What is an Enum?

An Enum is short for "enumeration." 
It's a way to represent a set of named values or items. 

Imagine you have a set of unique items, and instead of remembering them as numbers or strings, 
you give each one a name so it's easier to understand and work with.

How is it used in Python?
Python introduced the Enum class in the enum module to support enumerations.


'''

from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
'''
Here, Day is an Enum that represents days of the week. 
Now instead of using numbers to represent days, you can use Day.MONDAY, Day.TUESDAY, etc.
'''

'''
Why use an Enum?

Readability: 
It's clearer to use Day.MONDAY than just the number 1. 
Someone reading your code can immediately understand what you're referring to.

Organization: It groups related constants together.

Safety: 
Enums can help prevent errors. 
For example, if a function expects a day of the week, 
you can't accidentally pass it a number that's not in the range 1-7 if you're using the Day enum.
'''

class Color(Enum):

    # Keep in mind as they are constant varibales to make them in uppercase
    RED="red"
    BLUE="blue"
    YELOW="yellow"

# Keep in mind, we only define these contant values under Class only, not even under function defined in class

# So, we have told users that we have these only constant values we can access them

c = Color

# and this is how we get the value
print(c.RED.value)
print(c.BLUE.value)
print(c.YELOW.value)

if c.RED.value == "red":
    print("Color is RED")

# to get the name of the constant
print(c.RED.name)