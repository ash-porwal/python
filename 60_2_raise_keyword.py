# we can rase some errors too like below

name: str = input("Please enter your name: ")

if name.isdigit(): #isdigit is a method used in string which checks if value coontains numbers or not
    raise Exception("Please enter alphabets")

# if you want to check only for alpha then we have - isalpha() - which returns True if value is alpha
if name.isalpha():
    raise Exception("String got alphabets")

# if we have alphanumeric value in string then we have isalnum() method which returns true if string contains either alpha  or numeric or both
if name.isalnum():
    raise Exception("It also contains numeric value")
