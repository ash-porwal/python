# using this api: https://dummyjson.com/comments
import requests
import json, os

api: str = 'https://dummyjson.com/comments'

data = requests.get(api).json() # in request module we can convert this object into json directly
# so this will help us avoid doing json.loads(<str>) to convert into python dict object, above directly converts into python object.

# print(data)

# file name
root_path = '/tmp/Json_data/'
file_name = "dummy-data.json"

# Creating file if not exists
os.makedirs(root_path, exist_ok=True)

print("Directory exists:", os.path.exists(root_path))

# opening that file
with open(f"{root_path}{file_name}", 'w') as f:
    # using json.dump because  it writes the Python dictionary to a file in JSON format with an indentation of 4 spaces.
    json.dump(data, f, indent=4) # json.dumps() helps us specify indentation
    print("File created:", os.path.exists(f"{root_path}{file_name}"))
