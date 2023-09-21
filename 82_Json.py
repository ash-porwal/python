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

#we are making String to Json
data = '{"value1" : "Ashish","value2" : 500 }'
print(data)
print(type(data))
# print(data["value2"]) #so here shows error because it is a string and in string there is no key value pair

# json.loads() - this function is used to parse JSON data and return Python object. (this object can be dict, list, string, boolean, None) - depending on the structure of the data
parsed = json.loads(data)
print(parsed)
print(type(parsed))
print(parsed["value2"])

# Json.dumps function  used for dictionaries compatible for javascript
data2 ={
    "car" : "Mustang",
    "salary" : 150000,
    "allegations" : False #in javascript we do not have false with capital F..it is small f
}
javascript = json.dumps(data2)
print(javascript) #so here as we printed it ..it made False as false..and now you can use this data2 in JavaScript
print(type(javascript))

# Keep in mind, if opening a JSON file with open or context manager
# it gonna read the data inside that file as string, so we need to convert that string into dict

"""
This is how we can do

with open('path/to/file', 'r') as f:
    data: str = f.read()
    # now we covnert above string into DICT
    dict_data = json.loads(data) # so if it is a string we use loads method, but we can pass file path directly and load() method - json.load('/path/to/file')
"""

# if we want to convert DICT to JSON then
# for this we have json.dumps() - it takes dict inside dumps
some_dict = {'value': None}
json.dump(some_dict)