"""
"Pickling" is a term in Python used to describe the process of serializing and deserializing data. 
In simple terms, pickling is the conversion of a Python object into a byte stream, 
and unpickling is the inverse operation, where the byte stream is converted back into an object. 
This can be useful for saving the state of an object or for sending it across a network.

-----------------------------------------------------
Key Concepts:
-----------------------------------------------------

Serialization: when we say "serializing data," we are referring to the process of converting a Python object into a sequence of bytes. 

Deserialization: The process of converting serialized data back into its original form.

Pickling: Python-specific terminology for serialization.

Unpickling: Python-specific terminology for deserialization.

-----------------------------------------------------
The pickle module in Python's standard library provides 
the necessary functions to perform pickling and unpickling.
-----------------------------------------------------

- pickle.dump(obj, file): Serialize obj as a byte stream to file.

- pickle.dumps(obj): Serialize obj and return the resulting bytes.

- pickle.load(file): Deserialize a byte stream from file to produce an object.

- pickle.loads(bytes_object): Deserialize an object from a byte stream.
"""

import pickle

# Create a sample dictionary
data = {
    'name': 'Ashish', 
    'age': 26, 
    'is_learner': True
    }


# Serialize (pickle) the data into a byte stream
serialized_data = pickle.dumps(data)
print(serialized_data)
# Now, we can deserialize (unpickle) the byte stream back into an object
deserialized_data = pickle.loads(serialized_data)
print()
print(deserialized_data)  # Output: {'name': 'John', 'age': 30, 'is_student': False}

"""
-----------------------------------------------------
Precautions:
-----------------------------------------------------

- Security: You should never unpickle data received from untrusted or unauthenticated sources. 
The process can execute arbitrary code and potentially harm or compromise your system.

- Compatibility: Pickled data may not always be compatible across different versions of Python or between different systems. 
If long-term storage or interoperability is a concern, consider alternative serialization methods or formats, like JSON or XML.

- Performance: While pickling is convenient, it might not always be the most performant way to serialize data, especially for large datasets. 
Depending on the use-case, you might want to explore other serialization libraries or methods.
"""

# Lets try to dump serialized data

with open('my_info.pkl', 'wb') as file:
    pickle.dump(data, file)

# To load the data back:
with open('my_info.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
print(loaded_data)

