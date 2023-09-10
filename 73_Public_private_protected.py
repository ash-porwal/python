''' Variables are of three types:
        Public - any information which you want to see by everyone.
        Protected - any inforamtion which you want to see by some people chosen by you.
        Private - any info which only you can see.

like in class if you want to make a: 
    public variable then directly put that in class like showed below 
    protected variables are made with single underscore before the name of the variable...so that that variable can be access by that class itself or can be access by that class object but cannot be access by outer class
    private variables can be made by putting double underscore before variable name  ...so it means that variable is saying do not use it outside the class..so even the object cannot acces it directly
    but that object can access private variable if we write it with that class name ...as showed below  

'''

class Variables:
    one = "This is public variable"
    _two = "This is protected variable"
    __three = "This is Private variable and hence should not be used outside the class"

    def fun1(self):
        pass

ashish = Variables()
print(ashish.one)
print(ashish._two)
# print(ashish.__three) #see this is a private variable and it can only be access outside the class as shown below
print(ashish._Variables__three)  