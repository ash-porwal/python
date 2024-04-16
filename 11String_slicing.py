# Slicing is used to access parts of sequences like lists, tuples, and strings.
# String Slicing:
# A string in Python can be sliced for getting a part of the string. ..like if we want just two character from ashish
# The index in a string starts from 0 to (length-1) in Python.
name = 'Ashish'
print(name[0])
print(name[4]) # we can get any character of that particular index if we put that index number
# if we want to change a particular index like
# name [3] = 'f' #this wont work... so we cannot change any  
print(name[0:3]) # ye bol raha hai ki print karo name variables 0 se 2 tak ke index ..i.e. 0,1,2 indexes will be print (3rd index wont print)..and this is called string slicing
#print(name[:4])..here it will take from min to 3
#print(name[2:])..here it will take from 2 to last index

#negative index ...in negative counting last character of string will be -1, then second last will be -2 and so on
print(name[-4 : -1])
print(name[-4 : ])
# print(name[-1 : -4]) # this wont work because counting should start from lower number first then higher number

#skipping of string
d = "qwertyuioplkjhgfdsa"
print(d[0:4:1]) # ye last wali jo value hai iska kaam hai jaise we have 1 at the end to iska matalb hai koi character skip na karo...agar uski jagah 2 hota to ek character skip hoke aata
print(d[0:8:2])
print(d[1:8:2])
print(d[0::2])
print(d[0::3])
print(d[1:9:3])

'''
we read this name[0:4] as - 
----name sub 0 through 4-----
'''