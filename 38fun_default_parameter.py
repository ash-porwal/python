# greet someone using a function, and we gonna use a default parameter,
# means if while calling the function if we don't pass parameter then we have set its value, which will get picked
# And keep in mind after setting default parameter we cannot set non default parameter, but we can set default parameter after default parameter
def greet(name = "Mr. Unknown"): 
    print("Good Morning "+name)

x = input("enter your name\n")
greet(x)
greet()

# trying to set non default parameter after default parameter -> which shows as invalid syntax
# def greet(name = "Mr. Unknown", last_name):
#     print("Good Morning "+name)

# trying to set a default parameter after default parameter -> this works
def greet(name = "Mr. Unknown", last_name = "Porwal"):
    print("Good Morning "+name)

# we can also jump directly to any parameter

def details(name: str, last_name: str = "Porwal", age: int = 25):
    print(f'Hello, my name is {name} {last_name} and I am {age} old')

details('Ashish', age=26) #here i skipped last_name as I want it to pick default value but wanted to change value of age

# Also keep in mind the difference between parameter and arguments
# When we call the function with some inserted value then we refer that as argument, and we define parameters in the function while creating it.

"-----------------------------------------------------------"
# this default parameter will gets created only once and when
# function is created, if we call function two times and in the 
# first time that default parameter gets updated then in the
# second time of calling this function it will have value gets
# assigned from first time
# Example below code

def test(v, l=[]):
    print("RN value of l: ", l)
    l.append(v)
    return l

l1 = test(1)
print("l1: ", l1)
l2 = test(123)
print("l2: ", l2)
l3 = test('a')
print("l3: ", l3)
