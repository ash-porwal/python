"""
First we will get to know the differences between multi-processing, threading and asyncio

Asyncio - In this it uses one single thread but while it is waiting on some function, it can trigger another fucntion and can switch back and forth.

Threading - it is like asyncio but in this that new function can start in new thread.

So, these both - Asyncio and Threading runs concurrently.

While in multiprocesssing it runs in Parallel execution - both Processes can be start at exactly at the same time.
So, in multiprocessing each processes gets its own GIL (Global Interpreter Lock).

# we can lock the processes in multiprocessing with Semaphores too.
"""