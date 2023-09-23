"""
multiprocessing module allows you to create parallel processes, 
which can help you fully utilize CPU cores and bypass the Global Interpreter Lock (GIL) 
that exists in the CPython interpreter. 
"""

from helpers.time_cal import get_time, time_stamp, kill_time
import multiprocessing as mp
import os


def func(param):
    # mp.current_process().name - to get process name
    # os.getpgid() - to get Process id
    print(f"Starting: {mp.current_process().name} ({os.getpid()}) ....{time_stamp()}") 
    kill_time()
    print(f"{os.getpid()} finished!! at {time_stamp()}")

@get_time
def main():

    # now we will create a process, it is same as we created Thread
    # Process: The simplest way to start a new process is by using the Process class.
    # mp.Process(name=<This will be the name of the process>, target= <here we define function name which we want to trigger>, args= <pass arguments as tuple> )
    process_1 = mp.Process(name="This is process 1", target=func, args=('Sample1',))
    process_2 = mp.Process(name="This is process 2", target=func, args=('Sample2',))

    # and here we can start these processes
    process_1.start()
    process_2.start()

    # till it wait till join processes gets completed
    process_1.join()
    process_2.join()

# if want to know number of processes in your computer
print("NUmber of processes on this machine: ", mp.cpu_count())
main()

# as compare to Thread, Processing is faster than threading
# Threading and Asyncio should be used more if creating API requests because you are waiting on external source.
# With multi processing we use when calculations that you have to be done on your computer



# -----------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------------")
"""
Communication Between Processes: 
One of the challenges of multi-processing is safely communicating between processes.
The Queue and Pipe classes are the most common ways to do this.

Process: Allows us to spawn a new process.
Queue: Provides a way to communicate between processes using a queue (First-In-First-Out data structure).
Queue class, which will allow us to pass data between the main process and the child process.
"""


from multiprocessing import Process, Queue

def worker(q):
    q.put("Data from worker") # This function simply puts the string "Data from worker" into this queue.

if __name__ == "__main__":
    q = Queue()
    p = Process(target=worker, args=(q,))

    # -----Explaination of p.start()-----
    # This line starts the process p, which means the worker function will be called in a new process.
    p.start()


    # -----Explaination of q.get()-----
    # After starting the process, the main process waits for data on the queue. The q.get() call is
    # blocking, which means it will wait until there's data available in the queue. Once the worker function
    # puts data into the queue, q.get() retrieves it, and it's then printed by the main process.
    print(q.get())

    # -----Explaination of p.join()-----
    # This ensures that the main process waits until the child process p (which is executing the worker 
    # function) completes its execution. Using join() is a good practice as it helps in ensuring all 
    # processes have completed before the main process continues or exits.
    p.join()

"""
In summary:

- A new process p is spawned to run the worker function.
- The worker function sends a message ("Data from worker") back to the main process via the queue q.
- The main process retrieves and prints this message.
- The main process waits for the child process to finish before continuing.
"""