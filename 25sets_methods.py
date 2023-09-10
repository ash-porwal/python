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
- Sets are mutable.
- Sets are unordered # Elements order doesn't matter
- Sets are unindexed # Cannot access elements by index and cant perform slicing
- There is no way to change items in sets
- Sets cannot contain duplicate values
'''

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
print(a.union(b)) #return Values which exist in a or b
print()
print(a|b) # another way of Union method ..using pipeline symbol

print()
print(a.intersection(b)) #return Values which exist in a and b
print(a&b) # we can use Ampersand symbol for intersection
print()

print(a.difference(b)) #return Values which exist in a but not in b

# we can update the set too
items: set = {'ashish', 'porwal'}

items.update({'Rahul'})
print(items)