'''
API stands for Application Programming Interface.
it is basically a tool that allows you to get data from a database and then use it whatever the way you want
Example -
When you use an application on your mobile phone, the application connects to the Internet and sends data to a server.
The server then retrieves that data, interprets it, performs the necessary actions and sends it back to your phone.
The application then interprets that data and presents you with the information you wanted in a readable way.
This is what an API is - all of this happens via API.
'''
from email.mime import image
import requests  #it is a python library which helps us in making the http request

# We made response variable name and we saved request.get..now this function gonna do is tell request to go and get the information from this URL 
response = requests.get("https://randomfox.ca/floof")
#now whenever we make http request it is going to return a status code that tells us some information about how the request went..and now the default is 200 or Okay which means the response went well and all the information was returned fine
print(response.status_code) #checking the status code
print(response.text) #another way to  check the response and it will return in string format..but actually we are getting this in Json file 
print(response.json) #here we get an actual dictionary we can work with

# so we can create a new variable and assign it response.json value
fox = response.json()

# now it must contains keys..lets check
print(fox.keys()) #so we got image and link as key name
print(fox["image"])