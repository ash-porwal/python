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