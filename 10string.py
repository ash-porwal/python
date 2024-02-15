# The string is a data type in Python.

# A string is a sequence of characters enclosed in quotes.

# We can primarily write a string in three ways:

# Single quoted strings : a = 'qwerty'
# Double quoted strings : b = "qwerty"
# Triple quoted strings : c = '''qwerty'''
# so why needed three ways to put strings..
# cuz if we write something in apostrophy then we use double quote so the compiler wont get confused
# like this =
# a = "Ashish's"
# and if we are using double and sigle quote then we then can ise triple  quotes...alos if we want to print multiline then also  we should put in triple quote
# a = '''ashish's and ashish"s '''

# if we want length of string..we can use len function
# this is how we concatenate two
greet = 'good morning, '
name = 'Ashish'
print(greet + name) # if we add two strings then it may complete one sentnece
# we can also do this
c = greet + name
print(c)

#strings are immutable

# f-string
key = "key"
print(f"{key:10} Value") # here we can create 10 spaces, or n number of spaces
print(f"{key:>10} Value") # here it can create 10 spaces before the key varaible
print(f"{key:<10} Value") # here it can create 10 spaces after the key varaible
print(f"{key:^10} Value") # here it can put it in perfectly center

# we can provide any character instead of empty space
print(f"{key:-^10} Value") # here printing 10 dashes(-)
print(f"{key:->10} Value")
print(f"{key:-<10} Value")

# Rounding Floating point number using fstring
number: float = 10_000.32432534
print(f"{number:.2f}") # here I've rounded it to two decimal places using 2f -> .<number of decimal place you want>f

# we can convert to percentage
num: float = 0.096
print(f"{num:.2%}")


big_num = 10_000_000.234234
print(f"{big_num:,.2%}")