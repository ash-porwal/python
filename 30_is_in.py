# == : Value Equality / Comparison Operator

# Compares the values of the two objects.
# Used to check if the values on either side of the operator are equal or not.
# For example: 3 == 3 returns True because both values are 3.
# is : Identity Operator

# Compares the memory locations (or ids) of the two objects.
# Used to check if two variables refer to the same object in memory.
# For instance, a is b will be True only if a and b are referring to the same object in memory.

# Lists are mutable objects in Python.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)  # True, because the values in both lists are the same.
print(list1 is list2)  # False, because they are two different objects in memory.

print(list1 == list3)  # True, because the values are the same.
print(list1 is list3)  # True, because list3 refers to the same object as list1.



# is
#The "is" keyword is used to test if two variables refer to the same object. Means it checks for id of that varibale
# Use the == operator to test if two variables are equal.

a = 100.0
b = 1.0 * a
print(id(a))
print(id(b))
print(a is b)
print(a == b)


a = 67
if (a == 67):
    print("yes")
else:
    print("No")

# in
'''
The in keyword has two purposes:

The in keyword is used to check if a value is present in a sequence (list, range, string etc.).

The in keyword is also used to iterate through a sequence in a for loop:
'''
b = [2, 89, 90.09]
print(2 in b)
print(22 in b)