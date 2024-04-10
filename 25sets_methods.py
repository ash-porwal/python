c = set()
print(c)
print(type(c))

#adding the value inside empty set
c.add("ok")
c.add(4)
c.add(4) #if we are adding the same value inside set then it wont add that value
c.add("Well Done")
# c.add([45, 56, 78])#this will throw an error ..we can not add list inside set..because list contain can be changed 
c.add((4,5,6)) #this is a tuple sowe can add tuple inside list ..because tuple cannot be changed
# c.add({5,78}) #similarly we cannot put dictionary because it is unhashable(means we can its containt)
print(c)

''' 
******Properties of Sets******
- Sets are mutable but elements of set should be immutale.
- Sets are unordered # Elements order doesn't matter
- Sets are unindexed # Cannot access elements by index and cant perform slicing
- There is no way to change items in sets
- Sets cannot contain duplicate values
'''

# When we say a set is mutable, we mean that you can change the contents of the set after it's created. 
# This includes:
# - Adding elements to the set.
# - Removing elements from the set.
# - Clearing the entire set.

# These operations change the set in place without creating a new set.
my_set = {1, 2, 3}
my_set.add(4)  # Adding an element
my_set.remove(2)  # Removing an element
print(my_set)  # Output will be {1, 3, 4}

# Immutability of Set Elements
# On the other hand, the elements that you add to the set must be immutable. 
# This is because sets rely on the hash values of their elements to check for equality 
# and determine the uniqueness of elements.
# For example, you can add a tuple to a set because tuples are immutable:
my_set.add((5, 6))

# my_set.add([7, 8])  # This will raise a TypeError
# we can add - integer, string


print(len(c)) #it will print length of set..means kitne items hai

c.remove("Well Done") #will remove that containt
print(c)
print( c.pop()) #this remove any random value inside set
print(c)

# there is discard method too, so the difference is that in remove method if something that does not exists in the set
# then it is going to throw an error, while discard won't do it if the removing element does not exists
c.discard('ash')

c.union({45, 67})
print(c)

#Common Sets operations
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
print(a.union(b)) # returns all Values which exist in a and b (and will remove all duplicate values)
print()
print(a|b) # another way of Union method ..using pipeline symbol

print()
print(a.intersection(b)) #return Values which exist in both a and b
print(a&b) # we can use Ampersand symbol for intersection
print()

print(a.difference(b)) #return Values which exist in a but not in b

# we can update the set too
items: set = {'ashish', 'porwal'}

items.update({'Rahul'})
print(items)