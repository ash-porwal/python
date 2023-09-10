'''
When we dont have fixed amount of element then we prefer while loop. 
So in condition we prefer that condition which is going to get false at some point otherwise while loop will go in infinite

The while keyword is used to create a while loop.

A while loop will continue until the statement is false.
'''

x = 0
while x < 5:
    print("printed"+str(x))
    # print(type(x))
    x = x+1

fruits = ['Apple', 'Oranges', 'Mangoes', 'Pineapple', 'onion']
f = 0
while(f<len(fruits)):
    print(fruits[f])
    f = f + 1
