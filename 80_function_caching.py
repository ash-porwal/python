# jab koi function ko output dene mein kuch time lag raha ho..
# lekin again dobara wo function run karae to ab wo turant output de..
# ye tabhi possible hai jab hum output ko store karae ..this is called function caching aka Memoization.

# we have to imporrt lru_cache from functool...lru_cache is a decorator

"""
Memoization is a technique in Python (and other programming languages) 
where you store the results of expensive function calls and return 
the cached result when the same inputs occur again. 
This can help speed up programs by avoiding unnecessary recalculations.
"""
import time
from functools import lru_cache # LRU stands for Least Recent Used

@lru_cache
def fun1(n):
    time.sleep(n)
    return n

print("Calling fun1()")
a = fun1(3)
print(a)
print("Calling fun1() again")
a = fun1(3)
print(a)