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