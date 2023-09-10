# logical operators are ---> AND, OR, NOT
# AND - This will be true if both the operands are true
# OR - This will be true when either statement is correct
# NOT - this will invert the True to false and vice-versa

age = int(input("Enter your age"))
if (age <= 80 and age >= 18):
    print("you can drive")
else:
    print("You cannot drive!")