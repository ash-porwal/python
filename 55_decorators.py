def f1(f):
    def f2():
        print("this is before calling the function")
        f() #this f is a parameter of f1 ..check line 1
        print("this is after calling the function")
    return f2

def f3():
    print("This is f3 ")


x = f1(f3) #here i am calling f1 taking f3 as an argument
x()

print()
print("**********")
print()

#so this line 11 and 12 we can write it as a shortcut as @f1(if you want to call f1)
def f1(f):
    def f2():
        print("this is before calling the function")
        f() #this f is a parameter of f1 ..check line 1
        print("this is after calling the function")
    return f2
@f1 #this is called decorator and @ is  the short form of f1...and this decorator will pass f3() as an argument in f1
def f3():
    print("This is f3 ")

f3() #here the call begins so will go to line 22 but compiler will see just above line 22 there is @ sign which will calll f1 first before f3()
