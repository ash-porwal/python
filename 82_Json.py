import json
# JSON stands for JavaScript Object Notation

"""
Keep in mind - 
In JSON key value pair are not in Single quote, so they must be in double quote like this
{
    "person": "ashish"
}

Also the boolean value is in lower case, and not in upper case, so it is false not False(which is in python)
{
    "person": "ashish",
    "value": false
}

"""
print("------Serialization------")

"""
Serialization - The process of encoding JSON 
serialization term refers to the transformation of data into a series of bytes to be stored or transmitted across a network.
so we create a file using dump or dumps method
when we write into disk we perform serialization.

dump() vs dumps()

dump() - when we are writing Python object into a file then we use this
dumps() - when we want to print or capture it into memory then we use this, with indent=4 we can make it pretty
          dumps() converts Python object into JSON string
"""
data2 ={
    "car" : "Mustang",
    "salary" : 150000,
    "allegations" : False #in javascript we do not have false with capital F..it is small f
}

# dumps - to print pretty JSON
javascript = json.dumps(data2, indent=4)
print(javascript) #so here as we printed it ..it made False as false..and now you can use this data2 in JavaScript
print(type(javascript))

# writing into file - 
with open("test.json", 'w') as f:
    json.dump(data2, f, indent=4)
    print("Created test.json file successfully")

print()
print("------Deserialization------")
"""
Deserialization - in this we turn JSON into Python objects with load() and loads() methods
load - converts into python object if reading from JSON file
loads = converts JSON string into python object
"""
#we are making String to Json
data = '{"value1" : "Ashish","value2" : 500 }'
print(data)
print(type(data))
print()
parsed = json.loads(data)
print(parsed)
print(type(parsed))
print(parsed["value2"])
# lets try to open above file
with open("test.json", 'r') as f:
    print(json.load(f))