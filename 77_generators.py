'''
Iterable - iterable ek aisa python object hota hai jisme ya to ye wala __iter__ or __getitem__ define hota hai
            so if we run these methods then it will give iterator...iterable objects are list, string, tuples etc

Iterator - ek aisa python object hota hai jisme __next__() define hota hai
Iteration - iterate karne ki process ko iteration kehte hai

---------------------------------------------------------------
------ If someone ask what is iterator and iterable then ------
---------------------------------------------------------------

Iterable -  iterable is any Python object capable of returning its members one at a time
            Common examples of iterables include all the sequence types like lists, strings, and tuples, as well as non-sequence types like dictionaries and files.

            You can define an object as an iterable by implementing the __iter__() method in its class definition. The __iter__() method should return an iterator object, which then uses the __next__() method to get the next item.

Iterator -  An iterator is an object that actually performs the iteration
            It does this by implementing two methods:
                1. __iter__() 
                    which should return the iterator object itself. 
                    This allows iterators to be used where iterables are expected, such as in loops.

                2. __next__() 
                    which returns the next item of the sequence. 
                    On reaching the end, and in subsequent calls, 
                    it should raise StopIteration.

Iteration - 
            Iteration refers to the process itself of taking an iterable and going through its 
            elements one by one. 
'''

my_list = [1, 2, 3]  # This is an iterable

# Obtaining an iterator from the iterable
my_iterator = iter(my_list)  # The iter() function calls my_list.__iter__()

# Iterating through using the iterator
try:
    while True:  # Iteration process
        item = next(my_iterator)  # The next() function calls my_iterator.__next__()
        print(item)
except StopIteration:
    pass  # End of iteration

'''
so now what is generators?

a generator is a special type of iterable, similar to a list or a tuple. 
But, instead of storing all of its items in memory like a list or tuple, 
a generator produces items on-the-fly and yields them one by one using the yield keyword.
Because of this, generators are more memory-efficient for large datasets.

they are a type of iterators...and we can only traverse(travel through an area) them one time just like range() function
We use generators because we want to save RAM because they creates value on the fly
'''

#creating our own generator..
def gen(n):
    for i in range(n):
        yield i #yield is the generator which generates the value on the fly(when in motion)
# so as soon as you use yield in function that function is a generator then

one = gen(10**100)
print(one) #so this is not a function ..this is a generator object ...but if we write return instead of yield in gen() function then it will give some value
#and in generator we have __next__ method
print(one.__next__()) #NOW WE ARE GETTING VALUE
print(one.__next__()) #AND WE RUN THIS AGAIN AND GOT THE NEXT VALUE
print(one.__next__())
# print(one.__next__()) #NOW if the value of n is 3 ..i.e it is capable of creating 0,1,2 value just like range...so it gives an error... but in case of for loop we do not see any error because they handle stop iteration


# Creating generator using Generator Expression AKA Yield comprehension:
'''
Generator expressions provide a concise way to create generator objects.
They're similar to list comprehensions but use parentheses () instead of square brackets [].
'''
# generator expression to produce squares of numbers:
squares = (x * x for x in range(10))

for square in squares:
    print(square)


#try to create program Making fibonacci series and factorial using generators

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)

'''
From geeksforgeeks
Return sends a specified value back to its caller 
whereas Yield can produce a sequence of values. 
We should use yield when we want to iterate over a sequence, but don't want to store the entire sequence in memory.
'''