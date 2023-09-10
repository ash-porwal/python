'''
An exception is a runtime error which can be handled by a programmer
all exception are respresented as classes in python.

Type of exceptions:
    Built-in exception - they are pre-defined exception. The base class is BaseException for all built-in exception.
    example - SyntaxError, NameError, TypeError, RuntimeError, ImportError, ArthmeticError etc

    User defined exception - a programmer can create his own exceptions

ques. - so why do we need to handle the exception?
ans.  - if we do not handle exception..and exception occurs in the program then our program will get terminate.
        and suddenly termination of program may corrupt the program
        or maybe there is data loss because of exception from database or from file.

How to handle exception?
We use "try" block (try block mein wo code likhte hai jo exception cause kar sakta hai)
and another block is "except" this block is use to catch an exception that is raised in try block...there could be multiple except block for the try block
there is "else" block too and the code run in else block only when there is no occured exception in the program
and in the "finally" block ..this block will get executed irrespective of whether there is exception or not

syntax of try-
    try:
        statement   
 
syntax of except block -
    #we use this when we already know what kind of exception there is going to be
    1. except ExceptionClassName: 
            statement
    
    2.  except ExceptionClassName as object:
            statement
    
    3.  multiple exception within tuple
        #except (ExceptionClassName1, ExceptionClassName2, ExceptionClassName3,.....)         
            
            
'''

a= int(input("Enter a:"))
b= int(input("Enter b:")) #if user enters 0 in input then it will occur ZerorDivisonError now to handle it
c = a/b
print("program is not terminated")

print(c)

print()

#lets handle exception..so to handle our first task is to find ki kon si line hai jo exception throw kar raha...
# so  c = a/b wala code exception thorw kar raha..so we write in "try" block
a= int(input("Enter a:"))
b= int(input("Enter b:"))
try:
    c = a/b
    print("This is in try block")
    print(c)
#now if this block throws an exception so to handle it we have to write except block
except ZeroDivisionError:
    #to handle we are simply giving a message to the user
    print("Divison by Zero is not allowed")
print("program is not terminated in the mid")


#using another syntax of exception

a= int(input("Enter a:"))
b= int(input("Enter b:"))
try:
    c = a/b
    print(c)
except ZeroDivisionError as obj: #this obj contains description of ZeroDivisonError..which we are printing in this block
    print(obj)
print("program is not terminated")

# and if we think there could be more execptions in our try except block then we can either any kind of exception with -> 
# except Exception as e:  
# or we can specifically raise
# except ZeroDivisionError: so problem with this one is if there is other kind of exception happened then this block won't be able to handle it.

# suppose we could get ZeroDivisionError and ValueError in our block and if we want it to raise specifically just those two
try:
    pass
except ValueError:
    print("This is value error")
except ZeroDivisionError:
    print("This is zeo division error")

# and if we want we handle ValueError and any other error then we can do like this
try:
    pass
except ValueError:
    print("This is value error")
except Exception as e:
    print("This is some exception", e)