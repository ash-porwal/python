'''Escape sequence character
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.


\n(use for newline), \t(for making tab(Space)), \'(single quote), \\(backslash)etc
and what is raw string? - Ans. Raw strings are useful when handling strings that use a lot of backslashes
'''

a = "Hello\nthis is me\nso sad you do not remember me"
b = "Hello \t this is me\nso sad you do not remember me"
c = "if u want to print ba\ck sl\\ash then use double \\"
print(a)
print(b)
print(c)

#just example 
#we will take input of name and it should come up with "You are best" when you print it
a = input("Enter your name: ")
print("You're are best!", a) #here if you see we put string in double quote and the name variable in just as is it..so that is how we print
print(a, "You're are best!") 
# print(a,+ "You're are best!") #here this will show error
# print("You're are best!", + a) #here this will show error
print(a + "You're are best!") #this will print but we wont see any gap
