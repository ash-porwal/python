#A RegEx, or Regular Expression...can be used to check if a string contains the specified search pattern
import re

#Primarially we have findall, search, split, sub, finditer function

#findall - The findall() function returns a list containing all matches.
print("Findall -")
txt1 = "The rain in Spain"
x = re.findall("ai", txt1)
print(x)
print()
#The list contains the matches in the order they are found.
#If no matches are found, an empty list is returned:

# Search() -  The search() function searches the string for a match, and returns a Match object if there is a match.
              #If there is more than one match, only the first occurrence of the match will be returned:
print("Search -")
txt2 = "The rain in Spain"
x = re.search("\s", txt2)
print("The first white-space character is located in position:", x.start()) 
#If no matches are found, the value None is returned:
print()

#Split() = split() function returns a list where the string has been split at each match
print("Split -")
txt3 = "The rain in Spain"
x = re.split("\s", txt3)
print(x)
print()

#Sub() - sub() function replaces the matches with the text of your choice
print("Sub -")
#Replace every white-space character with the number 9
txt4 = "The rain in Spain"
x = re.sub("\s", "9", txt4)
print(x)

