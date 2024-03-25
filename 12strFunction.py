g = "ok this is me"
print(g[0:4]) #in this 0 1 2 3 indexes will be print so yeah that space coming between ok and this that space also save in one index

#these are the functions of strings

#1. len() function
print(len(g)) #this will count the number and give us value....mind that it will also count spacebar
#2. var_nam.endswith("") ..to check if it ends will it or no..so it will just return boolean
print(g.endswith("is"))
print(g.endswith("me"))
#3. var_nam.count("")
print(g.count("this")) 
#4 capitalize()..this funciton makes the first letter capital
print(g.capitalize())
#5 .find()..ye help karta hai koi word ko find karne mein...lekin firt occurence of that word in the string
print(g.find("is"))
#6 .replace()..to replace particular word aur jaha bhi wo word hoga toh wo  replace kar dega
print(g.replace("me", "Ashish"))


print("To check all the methods of the string")
print()
print(dir(str))


# join
l = ['some', 'comment']
print(''.join(l))

# join() is a string method in Python. 
# It is called on a string (which can be an empty string, as in this case) and takes an iterable (like a list) 
# as its argument.
# The method concatenates the items in the provided iterable, using the string it was called on as a separator. 

# In this example, join() is called on an empty string (''). 
# This means the items of the list l will be concatenated without any separator between them.

# so if you want to concatinate strings and it is big then prefer .join() way instead of '' + ''

#-----------------------------------------------------
# backslash
#-----------------------------------------------------
# Suppose if you want to print something or take something which interpreter will read it as some command of some unique characters
# then to avoid this situation we can use \ or raw string
print('\'')
