# Write a program to input eight numbers from the user and display all the unique numbers (once).
#means agar number print ho toh wo number repeated nahi hona chahiye
#to ye kaam ham sets bana kar kar sakte hai  
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))
n5 = int(input("Enter number 5: "))
n6 = int(input("Enter number 6: "))
n7 = int(input("Enter number 7: "))
n8 = int(input("Enter number 8: "))
print(type(n1))
s = {n1,n2,n3,n4,n5,n6,n7,n8}
print(s)

#What would be the length of following..guess it then see output
test = set()
test.add(20)
test.add(20.0)
test.add("20")
print(test)
print(len(test))
# so it is happening because in python 20.0 and 20 count as one number...that is why even 20.0 is not printed