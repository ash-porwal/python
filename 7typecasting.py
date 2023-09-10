# type function is used to find the data type of a given variable in Python.
# typecasting means we can change variables like if koi variable hai wo string hai then we can change it to int or any other var
#typecasting is a way to change one data type to other
a = "654" #here as we can see 654 is an integer but look closely it is in double quote so it is a string.
print(type(a)) # we can even check datatype by this
# so now if we want to add 5 to 654 .but it is a string and that 5 is int so we can't add string to int
# print(a+5) # this will show an error ...as i explained in line no.6
# so if we still want to add 5 to that then we can do typecasting
a = int(a) # here we did typecasting and this how we change string to int ..so now we can add 5 to that number
print(type(a)) #here we again checked which data type it has become
print(a+5)
a = float(a)
print(a)
#also if any nummber is in double quote then it is called String literal
# otherwise it will be called as numeric literal
''' and this is how we typecast other datatypes
Str(31)           # ”31” Integer to string conversion

int(“32”)       # 32 String to int conversion

float(32)       #32.0 Integer to float conversion'''