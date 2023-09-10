#Object introspection means object ke baare mein janana ki wo kis class se aaya hai 
class A:
    def fun1(self):
        pass

class B:
    pass

a = A()
#ways to do object introspection
print(type(a)) 
print(type("This is string")) #in output we can see it is from string class

#similarly we can use id to know the id of the object...every time id assign is different
print(id("This is string")) #in output we can see it is from string class
print(id(a)) 

#dir function
print(dir(a)) #dir are tells all those methods which are defined 