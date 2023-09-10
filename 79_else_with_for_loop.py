#for loop ke saath else tabhi chalta hai jab for loop normally end ho..matlab for loop ko break statement na mile

for i in range(5):
    print(i)

else:
    print("This for loop ended properly")

#but if we put break statement
print()
print("For loop with break")
print()
for j in range(5):
    print(j)
    break
else:
    print("This for loop ended properly")

print()
#so we can use else like..jab koi item check karte hai aur wo na mile to else part mein likh do ki that item was not found
for z in range(5):
    if z == 6:
        break
else:
    print("That number was not found")