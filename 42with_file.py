#using with we do not need to close the file ..it automatically closes 

# and opening file with keyword with this is called context manager
with open('file.txt', 'r') as z:
    z = z.read() # z.read() will read all the lines in text
    # we can even specify how many character we want to read - like if I want to read 10 character then we can do like: z.read(10)
    # if we want to read a single line from file then we have - z.readline()
    # if we want to read that file lines in a list then we can do - z.readlines()
print(z)
with open('file.txt', 'w') as z:
    z = z.write('ok this is updated file1') # whatever is written inside write() will get appended in new file.
    # just in case if you wanted to text in a new line, then we can do this: z.write("\nThis is new text", 'a)
print(z)

# Also keep in mind, if we open file with read mode or write mode then it wont allow us to do write method and read method respectively.
# so if you want to read a file also want to use write mode then we can come up with +, this allows us to use both methods simultaneously.

with open('file.txt', 'a+') as text: # we can use 'w+' or 'r+' to use read and write methods
    text.write("\nThis is new line")
    print(text.read())

    # if I want to seek(read or look) a file from starting then I would use 
    text.seek(0)
    print(text.read()) #noticed this time we got the output written but above text.read printed empty line

# We can even create our own Context Manager

class File:

    def __init__(self, name: str) -> None:
        self.name = name

    # now we would want to define __enter__ dunder method,
    # so when we do - with open("file.txt") in the backend this __enter__ gets triggered
    def __enter__(self):
        print(f"Opening file: {self.name}...")
        return self # and here we returned instance so that it can work inside with block
    
    # now we need to define __exit__ dunder method,
    # so that it can close that file which got open (this is also part of the Context Manager)

    # here defined 3 parameters: exc_type, exc_value, exc_tb, 
    # so in case if something happens wrong while reading the file exit dunder method will take that according and perform what should do based on error
    def __exit__(self, exc_type, exc_value, exc_tb): 
        # but we are not going to use above error statemnet parameters,
        # and simply making a print statement
        print(f"Closing {self.name} file...")

if __name__ == "__main__":
    file_name = input("Please enter file name: ")
    
    # now we can use our own context manager class
    # Notice here we used File instead of Open which is our class.
    with File(file_name) as f:
        print(f.name)
