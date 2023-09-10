x = 6 #global variable
def fun1():
    x = 5 #local variable
    print("fun1 value:", x)

fun1()

print("*************")

y = 6 #global variable

def fun2():
    # y += 5 #we are trying to change value  of y which is global variable ..so we cannot change it and in order to change we need to write global keyword before y inside function
    global y
    y +=5
    print("fun2 value:", y)

fun2()

print("*************")

k = 6
def fun3():
    # k += 5 #we are trying to change value  of k which is global variable ..so we cannot change it and in order to change we need to write global keyword before k variable inside function
    global k
    k = 22 #but if we define variable k as a new value right after using global keyword ..then it will prefer the local value of k
    k +=5
    print("fun3 value:", k)

fun3()

print("*************")

def fun4():
    z = 10 #here z is local varibale wrt fun4() but for fun5() it is a nonlocal or enclosing variable 
    def fun5():
        nonlocal z # so make z variable update we use nonlocal keyword
        z += 12 
        print("Z value inside fun5: ", z)
    print("before calling fun5 value of z:",z)
    fun5()
    print("after calling fun5 value of z:",z) #here value of z will be the same as defined in global variable because we are using global keyword inisde fun5()
    # fun5()

fun4()

'''
Local Variable: A variable declared within a function is known as a local variable. It is accessible only inside that function, not outside.

Global Variable: A variable declared outside all functions is a global variable. It is accessible from any function in the script.

Nonlocal (or Enclosing) Variable: When you have nested functions (a function inside another function), 
a variable declared in the outer function is considered nonlocal to the inner function. 
This variable isn't truly global, because it isn't accessible everywhere in the script, 
but it's also not local to the inner function. Instead, it's in an enclosing scope.

'''