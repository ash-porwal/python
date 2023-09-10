'''
https://www.w3schools.com/python/python_operators.asp
Python divides the operators in the following groups:
    Arithmetic operators (+,-,/,//(Floor division),%(Modulus), **(exponential))
    
    Assignment operators (Assignment operators are used to assign values to variables: =, +=, -=, /=, *=, %=, //= etc)
    
    Comparison operators (==, !=, >, >=, <=, <)
    
    Logical operators (Logical operators are used to combine conditional statements: and, or, not)
    
    Identity operators (Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location: is, is not)
    
    Membership operators(Membership operators are used to test if a sequence is presented in an object: in, not in)
    
    Bitwise operators(Bitwise operators are used to compare (binary) numbers: &(AND), |(OR), ^(XOR), ~(NOT), )

'''


a = 5
b = 6
# Arithmethic operators
print("The value of 5+6 is ", 5+6)
print("The value of 5*6 is ", 5*6)
print("The value of 5-6 is ", 5-6)
print("The value of 5/6 is ", 5/6) #Int always return a floating point number in python3 or greater version
#and this one // is called Floor division...Floor division is an operation in Python that divides two numbers and rounds the result down to the nearest integer
# Assignment Operators (+= -= *= /=)
a = 34  
print("before adding 2 value of a is", a)
#if we want to add 2 in value of a then we can do this
a += 2
print("after adding 2 value of a is",a)
#Similarly we can use these assignment operator
a -= 2
print(a)
a *= 2
print(a)
a /= 2
print(a)

#Comparison operators (==, >, >=, <, <=) ...comparison operators return boolean
b = 4>7 # so if it is true then it will return True else false
print(b)

#logical operators (And, OR, Not)
bool1 = True
bool2 = False
print("The value of bool1 and bool2  is", (bool1 and bool2)) #logical operators works like this...this is boolean algebra..And tab true return karega jab dono true honge..aur baaki saare cases mein false return karega
print("The value of bool1 and bool2  is", (bool1 or bool2)) # in case of OR ..dono mein se ek true ho jaye tab true return karega
print("The value of bool1 and bool2  is", (not bool2)) #not works with one variable ..Not will just reverse the result ..false ko true or true ko false

print(True == 1)
print(False == 0)

# So, 1 and 0 both holds the same value as True and False respectively but 1 and 0 are not boolean value
print(True + True)
