"""
In multiprocessing there is a data sharing issue.

So, suppose there is global varibale and with one process we are chaning that global varibale value to some other value.

Now, that process can change the global varibale but when that process gets end that global varibale value will again become the original value which global variable had.
So, that happens because each Process will have its own memory, and when that Process gets end that memory will get destory.

Now, we can handle this thing with Pipes or also can be handled with Queue

- Pipe is a communication method provided by the multiprocessing module in Python to enable 
  inter-process communication (IPC)
  In multi processing a pipe is the connection between two processes.

Here's a basic overview of how pipes work:

- Creation: The Pipe() function returns a pair of connection objects connected by a pipe, 
  which can be used for bidirectional communication.

- Send and Receive: You can send Python objects with the send() method and receive them with 
  the recv() method on a connection object.

- Close: Once you're done with a connection, it's a good practice to close it using the close() method.
"""

from multiprocessing import Process, Pipe

def main():

    # when we create Pipe() object then it gonna return two ends of the pipes - connection1(used for receiving) and connection2(used for sending)
    # but if we set duplex=true, like this parent_conn, child_conn = Pipe(duplex=true), then we could send and receive data from both ends of connections.

    c1, c2 = Pipe()

    # this is how we use Pipe, here we used pipe to send
    c2.send("Hello back from parent process!") #if we had set duplex=true then we could able to send data from c1 also.

    # c1.poll() #this returns either True or False, depending on whether if we are waiting for data to be received
    print(f"Data to be received:{c1.poll()}") #  Since you've just sent data, this will return True.

    # Now the object which we are going to receive is going to come from front end of the pipe.
    obj = c1.recv() # this is blocking until we receive it. So, need to make sure we have something to receive before using this.
    print(obj)
    print(f"Data to be received:{c1.poll()}")


if __name__ == "__main__":
    main()

# that is how a Pipe work, now in next file we gonna know about how can we use it in process.