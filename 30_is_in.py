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