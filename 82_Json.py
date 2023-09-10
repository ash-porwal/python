import json

#we are making String to Json
data = '{"value1" : "Ashish","value2" : 500 }'
print(data)
print(type(data))
# print(data["value2"]) #so here shows error because it is a string and in string there is no key value pair

#json.loads parsed kar deta hai...matlab string ko json format mein convert kar deta hai
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
