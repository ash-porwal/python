dictionary = {
    "a": "Hello! I am Ashish Porwal",
    "b": "and i am making dictionary",
    "marks": [78, 85, 98],
    "dictionary2": {'c': 'this is another',},
    1 : 2 #this 1 is key also whose value is 2 ..so we can make both int int
}


#we can check using "in" operator to check if key exists or not
print("a" in dictionary) #will return Boolean and it only checks for keys and not for values.

#this will print all keys inside dictionary - .key() function
print(dictionary.keys()) 
print(type(dictionary.keys())) 

#this is how we can make list by doing typecasting
print(list(dictionary.keys())) 

#we can also print their value - .values()
print(dictionary.values())

#similarly we can check the values if that value exits in the dic or not using - "in" keyword
#syntax - "value" in dict_name.values()
print("Hello! I am Ashish Porwal" in dictionary.values())

 #this returns tupel - contains - key: value pair
print(dictionary.items())

#we can update dictionary too
print(dictionary)
update = {
    "new" : "A new update"
}
dictionary.update(update)
print(dictionary)

#Looking for Key which doesn't exists ..this wont throw error if the value is not present in dictionary..this returns none
print(dictionary.get("marks2")) 
# print(dictionary["marks2"]) #this throws error if that value is not present in the dictionary
#and this is the differnece between .get and [] syntax 
print()

#Second way to update items in dictionaries
dictionary["SecondUpdate"] = "This"
print(dictionary)

print()
dictionary["SecondUpdate"] = "newUpdate"
#here we tried two keys with same name...it updates the "SecondUpdate" key value to the new value which is "newUpdate" ...hence keys are not mutable
print(dictionary)

#how to remove item
print()
del dictionary["SecondUpdate"] #we put key name inside square bracket
print(dictionary)

print()
#another way to remove item is using pop method -
#syntax - dict_name.pop("key_name")
dictionary.pop("a")
print(dictionary)

# setdefault method - In this if we try to get some value of some key if that exists then it is gonna return and if doesn't exists then we can set the custome value.
print(dictionary.setdefault('a', 'There is no key name "a"'))