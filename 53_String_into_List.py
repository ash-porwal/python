count = 0
n = input("Enter: ")
name = 'ok this is the time ok'
print(name.split()) #this .split() will convert string into list
for i in name.split(): # to get one particular word from string in list form
    if i == n:
        count +=1
print(count)