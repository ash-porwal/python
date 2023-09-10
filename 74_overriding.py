class A:
    a_var = "I am class A variable"
    def __init__(self): #those methods which starts and ends with double underscore are called dunder methods
        self.var = "Inside class A's constructor"
        print("auto")
        self.a_var = "a_var part two inside method"

class B(A):
    b_var = "I am class B variable"

x = A()
y = B() #here we made y as object of class B ..and B class is child class of A and we find __init__ method inside A so that is why it will automatically call 

print(y.b_var)
print(y.a_var)
