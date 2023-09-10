'''
Iterable - iterable ek aisa python object hota hai jisme ya to ye wala __iter__ or __getitem__ define hota hai
            so if we run these methods then it will give iterator...iterable objects are list, string, tuples etc

Iterator - ek aisa python object hota hai jisme __next__() define hota hai
Iteration - iterate karne ki process ko iteration kehte hai

so now what is generators?
they are a type of iterators...and we can only traverse(travel through an area) them one time just like range() function
We use generators because we want to save RAM because they creates value on the fly
'''

#creating our own generator..
def gen(n):
    for i in range(n):
        yield i #yield is the generator which generates the value on the fly(when in motion)

one = gen(3)
print(one) #so this is not a function ..this is a generator object ...but if we write return instead of yield in gen() function then it will give some value
#and in generator we have __next__ method
print(one.__next__()) #NOW WE ARE GETTING VALUE
print(one.__next__()) #AND WE RUN THIS AGAIN AND GOT THE NEXT VALUE
print(one.__next__())
# print(one.__next__()) #NOW if the value of n is 3 ..i.e it is capable of creating 0,1,2 value just like range...so it gives an error... but in case of for loop we do not see any error because they handle stop iteration


#try to create program Making fibonacci series and factorial using generators

'''
From geeksforgeeks
Return sends a specified value back to its caller 
whereas Yield can produce a sequence of values. 
We should use yield when we want to iterate over a sequence, but don't want to store the entire seq`    uence in memory.
'''