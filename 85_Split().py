#Using Split() we can take multple arguments..like this...but this should be in string only..later we can convert it
# a, b = input("Enter two values: ").split()
# print(a, b)
# a, b, c = input("Enter two values: ").split()
# print(a, b, c)

#if we put * while printing the list
lis1 = [1,2,3,4]
print(lis1)
print(*lis1)


#we can split on basis of anything
name_list = "ash,por,and"
print(name_list.split())
print(name_list.split(','))



