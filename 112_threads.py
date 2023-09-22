"""
Thread
A thread is the smallest unit of a CPU's utilization, and it consists of a program counter, a register set, and a stack space.

Global Interpreter Lock (GIL)
The GIL is a mutex (or a lock) that allows only one thread to execute Python bytecode at a time in a process. 
This means that even on multi-core systems, your Python threads won't run in true parallel if they are compute-bound.

"""

import threading
import time

def some_test_func(name: str, thread_count: str) -> None:
    print(f"Hello my name is {name} and this is running with {thread_count}")
    print("Sleeping for 10secs")
    time.sleep(10)
    print("Done Sleeping")

if __name__ == '__main__':

    # now we will create threads
    t1 = threading.Thread(target=some_test_func, args=('Ashish', 'Thread1')) # Syntax: threading.Thread(target=<function name>, args= (arg1, arg2)) 
    t2 = threading.Thread(target=some_test_func, args=('Ashish', 'Thread2'))

    # now we have got two threads, now we can start them
    t1.start()
    t2.start()

    # Wait until the thread completes
    t1.join() # so just in case if there is one more thread which depeneds upon t1 then we can use use t1.join() before starting that thread - t3.start()
    print("Thread1 completed")
