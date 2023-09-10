# we can store function to some variable  like this -
# def fun1()
#    pass
# a = fun1 #remember we do not use parenthensis while putting it into variable

# Functions can be passed as arguments to other functions: Because functions are objects we can pass them as arguments to other functions.
# Functions that can accept other functions as arguments are also called higher-order functions.

# Functions can return another function

def student(z: int):  # def is short for define
    print(z)
    return (sum(z)/400)*100


# in python functions are called just by writing function name student()
sm1 = [98, 56, 85, 92]
# percent1 = student(sm1) #((sm1[0]+sm1[1]+sm1[2]+sm1[3])/400)*100

sm2 = [55, 89, 82, 86]
# percent2 = student(sm2)

print(student(sm1), student(sm2))

# parameters are a way for us to pass some infomation into a function

'''
functions can be nested function
functions can return function
When we call function without using paranthesis we are referring the function...and it gives us the memory location
Function can take functions as a parameter
Naming convention of function -> words should be lower case and separated by underscore
'''

# we can do type hinting while returning the function too, like what type it is gonna be


def sum_numbers(a: int, b: int) -> int:
    return (a+b)


print(sum_numbers(5,5))
