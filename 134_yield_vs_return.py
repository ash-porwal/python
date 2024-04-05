"""
yeild vs return

return :
    When we want all the values at once - is when we use return in function
yield :
    But when a function uses yield, 
    it's like the function is pausing, handing you a result, 
    and then waiting. 
    When you ask for more, it picks up where it left off and hands you the next result.
    This process is called "generating"  
"""
print("Retun in function")
# Using return
def get_numbers_with_return(limit):
    numbers = [i for i in range(limit)]
    return numbers

# Using the function
numbers = get_numbers_with_return(5)
print(numbers)

print()
print("Yield in function")
def get_numbers_with_yield(limit):
    for i in range(limit):
        yield i

# Using the generator function
returned_num = get_numbers_with_yield(5)
print(returned_num) # generator object, need loop to get the value
for num in returned_num:
    print(num)