'''Data Types:
1. String # text
2. Integer # numbers
3. Float # decimal type
4. List # this is sequence type
5. Dict # mapping type -> key: value pair
6. Set # unique numbers but no order, there is frozen set too
7. Tuples #
8. Boolean # True | False
'''

# Crazy float question
a = 0.3
b = 0.2 + 0.1

print(a == b) # by look it suppose to be True, but why is it False?

# we will get to know when we print it
print(a, b)

# so to make above true we can do these things 

# use of round function
print("Value of b in round:",round(b, 2))

# we can use format or f string but that will convert int to str
print()
print("Getting 0.3 with f string method")
print(f"{b:.1f}")

# Or use of math module and we are gonna use floor method
print()
print("Getting 0.3 with math floor method")
import math
print(math.floor(b*100)/100)