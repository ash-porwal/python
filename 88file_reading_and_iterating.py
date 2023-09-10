print("READING A FILE!")
file = open('file.txt')
'''for line in file:
	print(line)'''

#this above will add a new line which is empty line, and in the origin file we dont have these white spaces, they are just creeated  by print() statement
#now, to deal with this, we just want to print each line as it is without a new line, we will be usng rstrip() method

print("handling White spaces created by print() statement")
for line in file:
	line = line.rstrip()
	print(line)
