#sometimes we want to send http request 
#The requests module allows you to send HTTP requests using Python.
#there are many types of requests -
# like - get..head...delete...patch


#get request is for mai koi URL mein jau aur uska content le aau

import requests
#when we want to fetch resource from the server we use get() method
r = requests.get("https://randomfox.ca/floof/")
#Now, we have a Response object called r. We can get all the information we need from this object
#and we can even add parameters to this URL link..and we make a dictionary and add value
furture_info = {"first":"Ashish", "last":"Porwal"}
#now we can pass this info to the link using Params
r = requests.get("https://randomfox.ca/floof/", params=furture_info)
print(r.url)
#when we print this url we see ? that is called query string so those parameters are converted into query string


print("type of response - ", type(r))
print() 
print("Url - ",r.url)
print() 
print("Header - ", r.headers)
print()
print("text - ", r.text) #.text likhne se ye get function mein jo URL hai uska content aa jayega


print() 
#Now if we want to download the image then we copy the image URL
req = requests.get("https://miro.medium.com/max/700/1*mk1-6aYaf_Bes1E3Imhc0A.jpeg")
#now to see the response of the image :
print(req.content) #this will print the bytes from the image..so we can take those bytes and save those to a file on our machine..so to do this
with open('yoda.png', 'wb')as f: #yoda is gonna be the name of the image ..wb mode is write byte ...and we will just open that as f
    f.write(req.content)
    #if we run this then we wont get any output down in the terminal but it will save those image to the python folder or wherever you are writing this program

print()

#post request 
    # When we want to send data to the server..i.e post is for adding the data to the server
    #r = requests.post('https://httpbin.org/post', data={'key': 'value'})
'''
The post() method sends a POST request to the specified url.

The post() method is used when you want to send some data to the server.

Syntax - requests.post(url, data={key: value}, json={key: value}, args)
args means zero or more of the named arguments in the parameter table below. Example:
requests.post(url, data = myobj, timeout=2.50)


'''

url  = "www.something.com"
# #data mein dictionary hogi
# data = {
#     'p1':1,
#     'p2':2
# }
# #ab ye data mein bhejna chahta hu
# r2 = requests.post("url" = url ,"data" =  data)