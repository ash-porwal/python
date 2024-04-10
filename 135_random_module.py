# Python Random module generates random numbers in Python. 
import random

# Methods in random module:

# randint()
# Synatx: randint(start, end) # start and end must be integer
# randint helps us generate random number within a range


for i in range(5):
    print(random.randint(1,100))

# seed()
# This is used to generate the same random number again and again
# syntax: random.seed( l, version )
#   l : Any seed value used to produce a random number.
#   version : A integer used to specify how to convert l in a integer.
for i in range(5):
    random.seed(0)
    print(random.randint(1,100))

print()
# choice()
# returns a random item from an iterable
# Syntax: random.choice(sequence)
list1 = [1, 2, 3, 4, 5, 6]  
print(random.choice(list1)) 

print()
# random.choices()
# returns multiple random elements from the list with replacement.
# Syntax : random.choices(sequence, weights=None, cum_weights=None, k=1)


