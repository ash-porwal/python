"""
So, lock will help in this way - suppose if there is a thread which we want to run only that thread at that time, 
so we can lock that thread and no other threds gets executed untill that lock is released.
"""

import threading
import time

# here we are gonna create a lock varibale which we can use later
lock = threading.Lock()

def counter(limit: int, name: str):
    for i in range(limit):
        time.sleep(0.5)
        print(name, i+1, sep=':')
    
def task1():
    lock.acquire()
    counter(5, 'Thread-1')
    lock.release()

def task2():
    lock.acquire() # we defined lock.acquire here, means it wont get trigger until the previous function lock.acquire gets release
    counter(5, 'Thread-2')
    lock.release()

def task3():
    counter(5, 'Thread-3')

def main():

    #creating threads
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t3 = threading.Thread(target=task3)

    # lets try to lock t1
    t1.start() # so we want to use lock in task1 function then we want to define lock.acquire() and lock.release()
    t2.start()
    t3.start() # this will get triggered even if we are locking thread in func1becuase there is no lock.acquire and release is defined in this function.

if __name__ == "__main__":
    main()