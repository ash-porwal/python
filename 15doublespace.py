#to detect if there is doubespace in program
d = "This is test of double space  ok"
ds = d.find("  ") #this will return index number
print(ds) #if there is double space in program then it will give some value otherwise return -1

"""
Method Usage:

The find method is used with strings to locate the position of a substring. It returns the index of the first occurrence of the substring if it is found.
The index method is also used with strings, lists, and other iterable objects to find the position of an element or a substring.
Return Values:

When the substring is not found, find returns -1.
index, on the other hand, raises a ValueError exception if the substring or element is not found.
Syntax:

The syntax for find is: string.find(substring, start, end) where start and end are optional parameters that define the search boundaries within the string.
The syntax for index is similar: string.index(substring, start, end) or list.index(element, start, end), with start and end being optional.
Use Cases:

Use find when you need to check the presence of a substring and want to avoid handling an exception if the substring is not found. 
It's a more suitable choice when you're okay with a negative index indicating absence.
Use index when you expect the substring or element to exist and prefer to handle an exception for the unexpected absence.

"""

s = "Hello, world!"

# Using find
print(s.find("world"))  # Output: 7
print(s.find("Python"))  # Output: -1

# Using index
print(s.index("world"))  # Output: 7
try:
    print(s.index("Python"))
except ValueError:
    print("Substring not found using index method.")
