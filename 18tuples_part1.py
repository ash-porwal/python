# a datatype which cannot be changed in python is called tuple
# Tuples are ordered, 
# Tuples are immutable
# Tuples allow duplicate values
# Tuples can have any data types in itself
# Tuple is hashable only if all its elements are hashable

t = (2, 5, 6, 7)
print(t)
print(t[3])
#it looks lists and tuples are same but they are not..
#we cannot update the value of tuples which we could do in list
# t[0] = 23
# print(t)

#
a = () #this is an empty tuple
print(a)
a = (25,) #tuple with single element and it is required to put coma after that single element...so the complier can know it is a tuple
print(a)
a = (25)
print(a) #this will become a number not tuple...so this wrong
a = (1, 44, 56)
print(a)
print(a[:3])