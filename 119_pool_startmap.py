"""
Pool.starmap is similar to Pool.map, but with an added capability: 

- it's designed to handle functions that take multiple arguments. 

- While Pool.map is suited for functions that take a single argument, 
  Pool.starmap allows you to pass multiple arguments to your target function by supplying an 
  iterable of argument tuples.

The name "starmap" comes from the idea that it "unpacks" arguments from tuples using the * syntax.
"""

# Scenario: 
# Imagine you have a function multiply that multiplies two numbers. 
# You have a list of pairs of numbers, and you want to multiply each pair using multiple processes.


from multiprocessing import Pool

def multiply(x, y):
    return x * y
# data = [(x,y), (x,y), ...]
data = [(1, 2), (3, 4), (5, 6), (7, 8)]

if __name__ == "__main__":
    with Pool() as pool:
        results = pool.starmap(multiply, data)
    print(results)

# The results are collected and returned in the same order as the input data. 
# Thus, print(results) will output [2, 12, 30, 56].
