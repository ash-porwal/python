#Write a program to accept the marks of 6 students and display them in a sorted manner.

s1 = int(input("Student 1 total marks: "))
s2 = int(input("Student 2 total marks: "))
s3 = int(input("Student 3 total marks: "))
s4 = int(input("Student 4 total marks: "))
s5 = int(input("Student 5 total marks: "))
s6 = int(input("Student 6 total marks: "))

Listmarks = [s1,s2,s3,s4,s5,s6,]
Listmarks.sort()
print(Listmarks)