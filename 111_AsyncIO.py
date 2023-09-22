"""
As we know code runs one line at a time and each line have to wait for previous line.
And if you want that code should not wait for the response of earlier line and should go for the next line
"""

"""
Before diving deep, it's crucial to understand these two concepts:

Concurrency: Doing multiple things in overlapping periods, but not necessarily at the same exact time. For
example, if you're cooking and listening to music, you're doing them concurrently but not in parallel.
So, In concurrency - if you run two functions, then one functions gets triggered and while that function is running
it will start trigger another function, so that means in concurrency both functions are not starting at the same time.

But in case of Parallelism it start a new thread, means we can run two functions at the same time.

Parallelism: Doing multiple things at the exact same time. This typically requires multiple CPUs or threads.
so, parallelism need a single core

##### Asyncio is a concurrent way to deal with code, so with asyncio we can create only one thread, while with Threading module we can create multiple threads.
"""

import asyncio
import requests

# to run asyncronous code we must have an entry point
# like if I want to create this function which should gets executed and return a reponse when it is done.
# now below function can be put to the side and return the response when it is done.

async def main(): 
    print("THis is main function")
    ...


# but to run async program we need to call 
asyncio.run(main()) # it takes function name

# keep in mind Asynchronous function are also referred to as Coroutine and a Coroutine is a function that can suspended and resumed.

# A coroutine is a special type of function that can pause its execution before reaching return, 
# and it can indirectly pass control to another coroutine for some time.

# You define a coroutine using async def:
async def hello():
    print("Hello,")
    await asyncio.sleep(1) # The await keyword is used to call another coroutine and wait for it to finish. So, we can replace any other function name with .sleep()
    print("world!")



# so, now if you want the compiler should wait for async function then we will need to use await keyword

async def get_data(api) -> dict :
    print("Getting response")
    data = requests.get(api).json()
    # suppose here I want compiler to wait till it gets response
    await asyncio.sleep(3)
    return data

# --------------------------------------------------------------------------------
# Now lets create full code

import asyncio
import requests

async def get_data(api) -> dict :
    print("Getting response")
    data = requests.get(api).json()
    print("Got resposne")
    # suppose here I want compiler to wait till it gets response
    print("Sleeping for 3secs")

    await asyncio.sleep(3)
    print("Done sleeping")

    return data

async def counter():
    for i in range(5):
        await asyncio.sleep(0.5)
        print(i)


async def main_normal():
    await counter()
    await get_data("https://dummyjson.com/comments")

asyncio.run(main_normal())

# In above we noticed that it is waiting for counter to get finished then get_data, which is just like a normal script

# Now we will create some taks
# If you want to run multiple coroutines concurrently, you can use tasks. 
# A Task is a subclass of Future that wraps a coroutine.
print()

async def main():
    print("creating Tasks while calling async fucntions")
    task1 = asyncio.create_task(counter()) # here we are creating tasks, and as soon as we create task it gets executed, and to get the return value(whihc is called fututre), we will need to assign a variable to it. 
    task2 = asyncio.create_task(get_data("https://dummyjson.com/comments"))

    # This is how we can cancel the task: task1.cancel()
    # This returns True is task is done: task1.done()

    # now we can call both functions at the same time
    counting: int = await task1
    data: dict = await task2

    # now like above we created two tasks and if there are more tasks needed to create then we had to declare that
    # there is something with which we can create multiple tasks by defining task single time: asyncio.gather() - this takes functions(coroutine) inside it.
    # tasks = asyncio.gather(
    #     get_data("https://dummyjson.com/comments"),
    #     get_data("https://dummyjson.com/comments"),
    #     get_data("https://dummyjson.com/comments"),
    #     return_execption=True # here did return execption True so it will help in this way, suppse first two times API call gets succeed but at the last attempt we got some exception, so if we had not define this things, then we wouldn't be getting any results even from first two calls 
    # )
    # On above I called get_data function 3 times.
    # but we get result as an array
    # results = await tasks
    # print(results)


asyncio.run(main())
