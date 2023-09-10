'''
decorators
are the function which takes another function as an argument and returns a function
decorator takes the result of a function, modifies the result and returns it.
we use @function_name  to specify a decorator to be applied on another function
'''



def decor(fun):
    def inner():
        print("Inner function before enhancing function")
        fun()
        print("Inner function after enhancing function")
    return inner
    
@decor
def fun1():
    print("this is function 1")
    print("using decorator we will enhance this function")
#now decorator will take this function as a parameter and adds some functionality and return this function

save_fun = decor(fun1)
## save_fun = inner
# save_fun()

# fun1()


