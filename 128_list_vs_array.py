# list and array both are different dataypes
# if we want to store big value then prefer array otherwise prefer list

# to use Array in Python we want to import array
from array import array
from sys import getsizeof

# making array
arr = array('i', range(10_00))
l = list(range(10_00))

print("Array bytes: ", getsizeof(arr))
print("l bytes: ", getsizeof(l))

