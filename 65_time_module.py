# we have to loops and we want to find which loop takes what time
# so to know that we use time module
import time

initial1 = time.time() #time ke andar ek time function hota hai jo ki return karta hai number of ticks
print(initial1)
i = 1
while i<11:
    print("i-", i)
    i +=1
    time.sleep(1) #ye wait kara kara ke print karayega
print("While loops took", time.time()-initial1,"secs")

print()

initial2 = time.time() #new initial time for "for loop"
for x in range(1, 11):
    print("x-", x)
print("for loops took", time.time()-initial2,"secs")

#hence while loop and for loop run in the same time

localtime = time.asctime(time.localtime(time.time()))
print(localtime)