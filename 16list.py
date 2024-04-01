#python lists are just like container to store a value of a data type ..in that order
# we can create a list using []
a = [5, 4, 6, 98, 45, "ashish"]
print(a) #this is how we print list
print(a[2])
a[0] = 56
print(a) 
a[0] = "as"
print(a) 

# list can have different types of variables
b = [500, "Ashish", True, 6.5]
print(b) 

#silicing of list
friends = ["Ashish", "Khushi", "Ruchi", "Sonu"]
print(friends[0:3])

#This is how we can sum the numbers in list
l = [4, 5, 6, 7]
# l = ['6', '7']
# print(l[0] + l[1] + l[2] + l[3]) #noob way to sum.
# print(sum(l)) #this is the best way to sum of list

print()
print("Ways to concatinate the two lists")
print(l + friends)

#if we directly print on appending or extending then we will get None
# print(l.extend(friends))
# print(l.append(friends))

# l.extend(friends) #this will merge the both lists
# print(l)
l.append(friends) #append will add the whole list at -1 index
print(l)



'''
Aliasing List in Python:
The process of giving a new name to an existing one is called aliasing.
The new name is called an alias name. 
Both names will refer to the same memory location. 
If we do any modifications to the data, then it will be updated at the memory location. 
Since both the actual and alias name refer to the same location, any modifications done on an existing object will be reflected in the new one also.

'''
# Like if I take
x=[10, 20, 30]
y = x
x[0] = 90
print(x)
print(y)

# above both x and y will get updated as both refers to the same memory location
'''
Cloning in List:
The process of creating duplicate independent objects is called cloning. 
We can implement cloning by using the slice operator or by using the copy() method. 
These processes create a duplicate of the existing one at a different memory location. 
Therefore, both objects will be independent, and applying any modifications to one will not impact the other.
'''

x=[10, 20, 30]
y=x[:] # when we do y = x[:], we're creating a shallow copy of the list x and assigning it to y
# A new list object is created as a copy of x and assigned to y. The slice notation [:] creates a new list that includes all elements of x, effectively making a shallow copy.
print(x)
print(y)
print(id(x))
print(id(y))

x[1] = 99
print(x)
print(y)
print(id(x))
print(id(y))