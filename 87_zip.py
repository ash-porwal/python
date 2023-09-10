a = [2,4,6,8]
b = [3,6,9,12]

#zip simply pack the values one by one in tuple out of two lists.
for item in zip(a,b):
    print(item)
    print()


#we can even unpack the two lists.
for item_a, item_b in zip(a,b):
    print(item_a)
    print(item_b)


'''

In linear algebra it is called dot product - when we are going to perform element wise multiplication and then add them.

so, the above can be done in 1 line by using numpy... it provides dot() function
 
'''