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


"""
Use case of Bitwise operator
"""

"""
Use case of OR bitwise
"""
a = 2
if (a == 1) or (a == 2):
    print(a)

# now I will use bitwise operator for above condition
a = 2
if a == (1 | 2):
    print(a)

"""
Explain above 
1 in binary is 01.
2 in binary is 10.

When you perform 1 | 2:
  01
| 10
-----
  11


11 in binary is equal to 3 in decimal.

So, (1 | 2) evaluates to 3. The code if a == (1 | 2): is checking if a is equal to 3
"""


"""

Use case of XOR operator:
A practical use case of the XOR (exclusive OR) bitwise operator in Python is in swapping the values of two variables without using a temporary variable. 
The XOR operator, denoted by ^, is true if and only if one operand is true and the other is false.
"""

a = 5
b = 10

# Swap the values
a = a ^ b
b = a ^ b  # Now b becomes the original value of a
a = a ^ b  # Now a becomes the original value of b

print("a:", a)  # Output will be 10
print("b:", b)  # Output will be 5

"""
break down how this works:

a = a ^ b assigns to a the result of a ^ b. Now a holds the combined bit information of the original a and b.
b = a ^ b effectively extracts the original a from the new a and assigns it to b. After this line, b has the original value of a.
a = a ^ b now extracts the original b (since b is now the original a) from the new a and assigns it back to a.
"""

"""
Use case of & bitwise
"""
def is_even(number):
    return (number & 1) == 0

# Test the function
print(is_even(4))  # Output: True, because 4 is even
print(is_even(5))  # Output: False, because 5 is odd

"""
The bitwise AND operation compares each bit of two numbers. It returns 1 for each position where both corresponding bits are 1, and 0 otherwise. When you perform number & 1, you're essentially comparing the least significant bit (LSB) of number to the LSB of 1.

In binary, the LSB of an even number is always 0, and the LSB of an odd number is always 1. Here's why:

Even Number: In binary, an even number ends with 0. For example, 4 in binary is 100, and 8 in binary is 1000.
Odd Number: An odd number ends with 1 in binary. For example, 5 in binary is 101, and 7 in binary is 111.

The Function's Logic
1. number & 1: This expression performs a bitwise AND between number and 1. If number is even, its binary representation ends in 0, so number & 1 results in 0. 
              If number is odd, its binary representation ends in 1, so number & 1 results in 1.

2. == 0: This checks whether the result of number & 1 is 0. If it is, the number is even; otherwise, it's odd.
"""