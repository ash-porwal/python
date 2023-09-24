"""


"""
import os
import time
from random import randint
from multiprocessing import Process, Pipe, current_process # imported Process, Pipe and current_process

def sender(connection):
    print(f"Sender process name: {current_process().name} and its PID is {os.getpid()}...")

    for _ in range(5):
        random_num: int = randint(1,10)
        connection.send(random_num)
        print(f"Random integer was sent: {random_num} from {current_process().name}")

        #now we want some delay
        time.sleep(0.5)
    print(f"Sending: 'None'... from {current_process().name}")
    connection.send(None)
    print("Finished sending data..")


def receiver(connection):
    print(f"Received in process: {current_process().name} and its PID is {os.getpid()}...")

    while True:
        data = connection.recv()
        print(f"{data} was received in {current_process().name}")

        if not data:
            break
    print("Done with receiving data...")

def main():
    c1, c2 = Pipe()

    sender_fun = Process(target=sender, args=(c2,))
    receiver_fun = Process(target=receiver, args=(c1,))

    sender_fun.start()
    receiver_fun.start()

    sender_fun.join()
    receiver_fun.join()



if __name__ == "__main__":
    main()