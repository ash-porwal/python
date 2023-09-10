# Set is a collection of non-repetitive elements...koi bhi same item name ya int dobara nahi lega
a = {'f', 'g', 'h', 1}
print(a)
#now here we are going to repeat 1 again and now it wont print the repeated item
a = {'f', 'g', 'h', 1, 1}
print(a)
#sets look similar to dictionary but let's check its class
print(type(a))

#now if we want to make an empty set then...if you are doing this
b = {}
print(b)
print(type(b)) #here we saw in output it makes empty dictionary

#now empty sets can be created using this syntax
c = set()
print(c)
print(type(c))
c.add(300)
c.add(350)
print(c)

