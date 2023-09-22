"""
Semaphores are just like locks but they allow us to run more than one thead at a time and we can lock them up.
"""
import threading
import time

# we will create semaphore object here amd we need to include the numbers of semaphores
sem = threading.Semaphore(3) # so basically here we define how many threads we want to use for our program.

def do_something(id: int):
    sem.acquire()
    print(f"Running id --> {id}")
    time.sleep(5)
    print(f"Finished running id --> {id}")
    sem.release()

for i in range(4):
    thread = threading.Thread(target=do_something, args=(i,))
    thread.start()

# So, as we acquire the threads, we want to release them too but sometimes we forget it,
# so we can use `with` keyword
# so defining do_something function again using `with` keyword
"""
def do_something(id: int):
    with sem:
        print(f"Running id --> {id}")
        time.sleep(5)
        print(f"Finished running id --> {id}")
"""