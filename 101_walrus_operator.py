# The walrus operator, :=, was introduced in Python 3.8 as a new syntax called the "assignment expression".

# This operator allows you to assign a value to a variable as part of an expression.

# The main advantage of the walrus operator is that it can help in situations 
# where you both want to check a value and also use that value. 
# One common use-case is while checking a value in a loop.


# Without the walrus operator:

# data = input("Enter data: ")
# while data:
#     # process data
#     print(f"You entered: {data}")
#     data = input("Enter data: ")

# With the walrus operator:

while (data := input("Enter data: ")):
    print(f"You entered: {data}")
