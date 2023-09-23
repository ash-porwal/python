"""
A pool can be used to spread out multiple computations across our CPU cores, so that they run in parallel 
without us having to do anything.

Map: It can be used to parallelize the execution of a function across multiple input values.
"""
from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
        print(results)



# If still dont understand then -
"""
As we already know this is map built-in module
map is a function that:

- Takes another function as one of its arguments.
- Takes an iterable (like a list) as another argument.
- Applies the given function to each item of the iterable.
- Returns a new iterable with the results.
"""
# Let's say you have a list of numbers and you want to double each number. 
# Here's how you'd use map to achieve this:
def double(x):
    return x * 2

numbers = [1, 2, 3, 4]
doubled_numbers = map(double, numbers)

# So

"""
So, pool.map is similar to the built-in Python map function but with a twist: 
it distributes the work across multiple processes to potentially speed up the computation, 
especially for CPU-bound tasks.

Pool
When you create a Pool, you're setting up multiple processes (often as many as there are CPU cores, 
but you can specify a different number). 
These processes can run tasks in parallel, which is especially helpful if you have a CPU-bound function 
that you need to run on a large dataset.

Map
Just like the regular map, pool.map takes a function and an iterable. 
It applies the function to each item of the iterable. 
But instead of doing this sequentially, it distributes the work across the processes in the pool.
"""
# Imagine you have a CPU-intensive function work and a large list of items data. 
# You want to apply work to each item in data.

from multiprocessing import Pool

def work(x):
    # Some CPU-intensive operation here
    result = "result"
    return result

data = ['item1', 'item2', 'item3', ...]

with Pool() as pool:
    results = pool.map(work, data)

# Here, results will contain the results of applying work to each item in data.
"""
How it works:

- When you call pool.map(work, data), the data is divided into chunks.
- Each process in the pool picks up a chunk and starts applying the work function to every item in that chunk.
- When all processes are done, pool.map collects the results and returns them in the same order as the input data.
"""


# Suppose we have a function slow_square that simulates a slow computation by sleeping for a second 
# and then returns the square of the number passed to it.
# We want to apply this function to a list of numbers using pool.map.

from multiprocessing import Pool
from time import sleep

def slow_square(n):
    sleep(1)  # Simulate a slow computation
    return n * n

data = [1, 2, 3, 4]

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        results = pool.map(slow_square, data)
    print(results)

"""

When you run this code:

- The numbers [1, 2, 3, 4] are each passed to the slow_square function in parallel because 
  we've used a pool of 4 processes.

- Even though each call to slow_square takes a second (due to the sleep), 
  all four numbers are processed simultaneously, so the entire computation finishes roughly in 1 second.

- After all processes finish their computations, pool.map collects the results.

- The results are returned in the same order as the input data. 
  So, even if the third process (processing the number 3) finishes before the second process 
  (processing the number 2), the result for the number 3 won't be placed before the result for the number 2.

- The print(results) statement will output [1, 4, 9, 16], which are the squares of the numbers 
  in the data list.
"""
