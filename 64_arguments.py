# Convention (normal argument, *args, **kwargs)
# we use * when we want to take unlimited amount of arguments,
# for example when we use print() function then we can print any amount of values -> print('a') or print(1,2,3,4) so it takes unlimited amount of arguments

# similarly we can achieve this in our custom function we just have to define * with arguments and if it is a keyword argument then we can define with two **

# *args allows a function to accept any number of positional arguments.
# **kwargs allows a function to accept any number of keyword arguments.

# *kwargs for dictionary
def fun1(*x, **y):
    # print(x[2])
    print(x)
    print(type(x))
    print(y)


list1 = ["a", "b", "c", "d", "e"]
fun1(*list1)

dic1 = {"a": 1, "b": 2, "c": 3}
fun1(**dic1)

def some_fun(*name: str, age: int) -> None:
    print(name, age)

some_fun("a", "b", age=10) # when we define args then to assign value to age, we have to explicitly define age

print()
"""
Arguments are passed by reference,
means if we change anything within a function, then it will
reflect in the original value as well
"""
def test_f(l:list):
    l[0]=100 # changing vlaue inside function

l = [1,2,3]
test_f(l)
print(l)

# but in this case
def test_f(l:list):
    l=[30,45,50] # here it is allocating a new object in the memory

l = [1,2,3]
test_f(l)
print(l)