# val = print(input("Enter any value\n"))
val = (input("Enter any value\n"))
print(type(val))
val = int(val)
print(type(val))

# If_elif_else ladder
if(val > 50):
    print("Your value is more than 50")
elif(val > 55):
    print("Your value is less than 50")  
elif(val == 50):
    print("Your value is 50")      

# Multiple if statement
# if (val > 50):
#     print("value is more than 50")
# if(val>50):
#     print("value is more than 50")
# if(val>50):
#     print("Value is more than 50")
# else:
#     print("value is less than 50")


#this is called Single line Conditional statement in other language it is called ternary operator.
num = 100
which_num = "even" if num % 2 == 0 else "odd" #note we do not use any colons or anything .. just write it as a single line.
print(f"Number if {which_num}")

print("Success") if 10>2 else print("Fail")
# Do THIS if TRUE else DO THIS

'''so, here above we used conditional statement as an expression( variable ko jo bhi assign hota hai wo expression bolte hai.) otherwise we cant use conditionlal statement like an 
expression if we want to use like this

which_num = if num % 2 == 0: 

so the above is going to give invalid syntax.

for example - 
    num = "Ashish"
    so here Ashish is expression
'''