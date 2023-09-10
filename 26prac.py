# Write a program to create a dictionary of Hindi words with values as their English translation. 
# Provide the user with an option to look it up!    
trans = {
    "kursi" : "chair",
    "paani" : "water",
    "pustak": "book",
}
print("Enter these words to see English translation -")
print(list(trans.keys()))
# print(list(trans.values())) #will show error because there is no such libraries..for showing the values

c = input("Enter word to see English translation:\n")
print("its means:", trans[c])