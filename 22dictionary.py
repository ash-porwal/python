# Dictionary is a collection of key value pairs
dictionary = {
    "a": "Hello! I am Ashish Porwal",
    "b": "and i am making dictionary",
    "marks": [78, 85, 98],
    "dictionary2": {'b': 'this is inside another dic',
                    'c': 'this is another'
    } #this is how we can make another dictionary
}

# print(dictionary[0]) #will throw error because dictionaries are unordered so we cant access the value through index
print(dictionary['a'])
print(dictionary['a'][0])
print(dictionary['a'][0:6])
# print(dictionary[0]) this is wrong we cant get any key value through index
dictionary['b'] = "ok this the new value of b"
print(dictionary['b'])
print(dictionary['marks'])
print(dictionary['dictionary2'])
print(dictionary['dictionary2']['b']) 
print(dictionary['dictionary2']['c']) 
# print(dictionary['dictionary2']['b']['c'])

'''
******Properties of Python Dictionaries******
- It is unordered...means inka koi order nahi hota ki ye first hai wo second hai like this
- It  is mutable....means we can change the value of dictinary
- It is indexed..means it saves the keyvalue in the index
   When we say a dictionary in Python is indexed, 
   it means that we can access its values using unique keys, not through numerical indices as we do with lists or tuples.
- It cannot contain duplicate keys...means ye jab bhi new value karenge koi index ki to wo purani value se replace kar dega
'''
