# Please refer below for all built-in functions
# https://docs.python.org/3/library/functions.html
print('-------print function--------')

# print with sep
# using sepeartor we can seperate the commans 
print("THIS", "THAT", sep=':')
print("THIS", "THAT", sep=' ') # leaving empty it will give the usual output, otherwise we can pass anything
print("THIS", "THAT", sep='askdnasd') # seperating with random text

# print with end - 
# when there is written a priint statnemen
print("Ashish") # actually it is written like -> print("Ashish", end='\n')
print("print statement1", end='') # this will turncate the new line character, and we can pass any value in quote of end.
print("print statement2")

# to go on documentation of any function
# On MacOS - press Command key and click on function which doc you want to see
# for windows/unix press Ctrl and click on that function
print()
# ------------------------------------------------------------------------------------------
print('--------enumerate---------')

# enumerate function
# Enumerate function returns index and items of the iterable 

sample_list: list[str] = ['Ash', 'Rahul', 'Abhishek']

for k, v in enumerate(sample_list):
    print(f'{k} : {v}')

# if we loop it to single value like below
print()

# below will return a tuple of index and value
for k in enumerate(sample_list):
    print(k)

print()
# we can even specify the start value in enumerate, by default it starts with 0
# I want it should start with 101 this time
for k, v in enumerate(sample_list, start=101):
    print(f'{k} : {v}')
print()

# ------------------------------------------------------------------------------------------
# round function
print('-------round--------')

some_float: float = 1.666677788
# we can round the above number
print(round(some_float))

# what if we want that round should be performed after 3 decimal then we would do this
print()
print(round(some_float, 3)) # I simply added 3

# ------------------------------------------------------------------------------------------
# range
print()
print('--------range--------')

# when it is just one number defined then it starts with 0 and ends at n-1. 
# (where n is that number which you defined in range function)
num: range = range(10) 
print(num)

# we can convert that range into a list
print(list(num))

# range syntax: range(start_value, end_value, step)

# to get negative number we want to define -1 at step
print(list(range(0, - 11, -1)))

# so above we converted range to a list but the size of range is pretty low as compare to list

# let's see the size of this number
import sys

print(sys.getsizeof(num)) # just 48bytes

#same number but as a list
print(sys.getsizeof(list(num))) # now it is around 136bytes, the same range as above but it is a list.

num2: range = range(10**2) # we can see this is a pretty big number, if we print it as a list, then computer is going to crash
print(sys.getsizeof(num2)) # just 48bytes again
print(sys.getsizeof(list(num2))) # 856 bytes just on converting from range to list

# ------------------------------------------------------------------------------------------
# globals
print()
print('---------globals---------')
