#variables are the name given to a memory location in a program
a = "Ashish"
b = 50000
c = 89.90
d = True # this is boolean ..it can be either true or false
d = None # this is none 
#in python program it will automatically detect if we write something in double quote then it will consider as string ..if there is normal integer then it will detect as integer and for decimal numbers it if there is decimal then it will detect flaot
# Keywords – Reserved words in Python
# Identifiers – class/function/variable name
print(a)
print(b)
print(c)
print(d)
print(d)
#and this is how we print

#if we want to know which type of variable it is then
print(type(a))
print(type(b))
print(type(c))
print(type(d))

'''Rules for defining a variable name: (Also applicable to other identifiers)

A variable name can contain alphabets, digits, and underscore.
A variable name can only start with an alphabet and underscore.
A variable can't start with a digit.
No white space is allowed to be used inside a variable name
Variable names are case sensitive too
If you want to define a variable name which contains two words then separate them with _ like this: first_name'''

_c = "Yo"
A = "Porwal"
print(_c)
print(A)

# What are constants?
'''
So, In other programming language we can define constants and these are the varibales which should not be changed.
In python there is no way to define constant but we have this convention if we want to define constant whose varibale shouldn't change
then we can do with all capital letters, like below

API_KEY = "ksmdflsmdlfgdfgasdfasdfaspogjgpm"

'''

# What is type hinting?

'In python suppose I want to define a string, then I would do this'
first_name = 'Ashish'
'I did not define explicilty as string, python interpreter will automatically understand it is a string'


'Now the concept of type hinting requires us to actually explicitly say that we are using a string here:'

first_name: str = 'Ashish'
print(first_name)

# similarly we can type hint - int, dict, set, tuple

some_list: list = ['a', 'b', 'c']
# or we can more specify it
some_list: list[str] = ['a', 'b', 'c']



# if we assign some integer value in varibale with uderscore, then in output it is going to be ignored
some_number = 1000_00 #so this practise is recommneded if dealing with high numbers
print(some_number)