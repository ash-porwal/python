from time import perf_counter
from functools import wraps
from datetime import datetime

def get_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        end_time = perf_counter()
        print(f"Time: {end_time - start_time} seconds") 
    return wrapper

def time_stamp() -> str:
    return f'{datetime.now():%H:%M:%S}'

def kill_time():
    for _ in range(10**5):
        ...