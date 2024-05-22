"""

Recursion is a technique in which function calls itself directly or indirectly
- Base Case: 
    Every recursive function must have a base case, 
    which is the condition under which the function stops calling itself. 
    Without a base case, a recursive function would continue to call itself indefinitely, 
    leading to a stack overflow.

- Recursive Case: 
    This is the part of the function where the recursion actually occurs. 
    The recursive case must alter the state of the problem in such a way as to move it towards 
    the base case.

"""
# def do_something(num: int):
#     print(num)
#     if num == 1:
#         print("Breaking function")
#         return  # in function return works like break, as it will exit the function and returning nothing

#     # we are calling the function again
#     do_something(num-1)


# do_something(5)

# 0 1 1 2 3 5 8
def fibonnaci(n, series = [0, 1]):
    if(n == 2): # base condition
        return series

    newSum = series[-1] + series[-2] # hypothesis
    series.append(newSum)
    return fibonnaci(n - 1, series) # 


print(fibonnaci(10))