"""
To check how much time somewhere it takes in Python to run code.
For this we would need to import time module.
from time module we can use performance counter class - perf_counter
"""
import time

start_time: float = time.perf_counter()

for _ in range(8**8):
    ...
end_time: float = time.perf_counter()

print(f"Script ran for {end_time - start_time} in seconds")

# Note: Time of running code is also depends on the CPU usage.