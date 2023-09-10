'''
When should we go for tuple data structure in python?
If we are going to define a data which is not going to change over the period,
then we should go for tuple data structure.
For example, weekdays, calendar months, years etc.

'''
#Note: parenthesis are optional, when creating tuples. So, tuples are defined by the commas and not paranthesis
employee_ids = 1, 2, 3, 4, 5
print(type(employee_ids))

# slicing
t=(10,20,30,40,50,60)
print(t[2:5])
print(t[2:100])
print(t[::2])
print(t[::-1]) #this will reverse'

'''
Tuple having immutable nature.
If we create a tuple then we cannot modify the elements of the existing tuple. 
The operations/functions/methods on tuples, which we are going to see now, 
will create and return new objects (lists, strings, tuples) depending on the operation, 
but not change the existing tuple because of its immutability.
'''

t=(10,20,30,40)
# t[1]=70 #TypeError output

'''
Concatenation operator (+):
This operator concatenates two tuples and returns a single new tuple object.
'''
t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)

'''

Multiplication operator (*):
Multiplication operator works as repetition operator, and returns a single, new, repeated tuple object.
'''
t1=(10,20,30)
t2=t1*3
print(t2)

# we can unpack tuple like this too
a, b, c, d = t
print(a)
print(b)

# or we can use *
a, *b = t
print(a)
print(b) # b will hold the rest value as a list