#jab koi function ko output dene mein kuch time lag raha ho..lekin again dobara wo function run karae to ab wo turant output de..ye tabhi possible hai jab hum output ko store karae ..this is called function caching
# we have to imporrt lru_cache from functool...lru_cache is a decorator
import time
from functools import lru_cache

@lru_cache
def fun1(n):
    time.sleep(n)
    return n

print("Calling fun1()")
a = fun1(3)
print(a)
print("Calling fun1() again")
print(a)