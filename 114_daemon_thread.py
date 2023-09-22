"""
Daemon threads are background threads that automatically exit as soon as the main program finishes executing. 
By default, threads are non-daemon.

Daemon threads are considered as low priority threads. so Daemon threads only stay alive as long as there is other thread running.
"""

import threading

def print_numbers_up_to(n):
    for i in range(n):
        print(i)

# we can set daemon threads like this
t = threading.Thread(target=print_numbers_up_to, args=(3,), daemon=True)
t.start()