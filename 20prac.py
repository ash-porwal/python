# Write a program to store 7 fruits in a list entered by the user
f1 = input("Fruit 1 name: ")
f2 = input("Fruit 2 name: ")
f3 = input("Fruit 3 name: ")
f4 = input("Fruit 4 name: ")
f5 = input("Fruit 5 name: ")
f6 = input("Fruit 6 name: ")
f7 = input("Fruit 7 name: ")

fruitlist = [f1, f2, f3, f4, f5, f6, f7]
print(fruitlist)
fruitlist[2] = "orange" #this is how we can change the value  if it is list
print(fruitlist)
# fruitlist.replace("fruitlist[1]","Apple")
# print(fruitlist)
# fruitlist.replace("f2","Apple")