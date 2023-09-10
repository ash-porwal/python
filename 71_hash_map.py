#this returns where that paticular item value is stored
# def get_hash(key):
#     h = 0
#     for char in key:
#         h+= ord(char) #ord() function will find the ascii value of that particular item
#         return h%100 #we are assuming that 100 is the size of the array/list
    
# print(get_hash("March 6"))

#creating hash table
class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h+= ord(char) #ord() function will find the ascii value of that particular item
            return h%100 #we are assuming that 100 is the size of the array/list

# Now we want to add key:value pairs in hash map
    def add(self, key, value): #we want to add a key value pair in hash map
        h = self.get_hash(key) #so first thing we do get our hash..so for a given key it will give us hash(hash is just function to find where it stored that value) 
        self.arr[h] = value

    #now we want that it should get the value of key just by putting the key name ..this function is for that
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

t = HashTable()
print(t.get("Hello"))

print(t.get_hash("march 6"))