#using with we do not need to close the file ..it automatically closes 

# and opening file with keyword with this is called context manager
with open('file.txt', 'r') as z:
    z = z.read()
print(z)
with open('file.txt', 'w') as z:
    z = z.write('ok this is updated file')
print(z)

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
