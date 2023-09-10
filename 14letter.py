letter = '''Dear Name!
You are selected!
Date'''
n = input("Enter name:\n")
d = input("Enter Date:\n")
letter = letter.replace("Name", n)
letter = letter.replace("Date", d)
print(letter)