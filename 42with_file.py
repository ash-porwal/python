#using with we do not need to close the file ..it automatically closes 

with open('file.txt', 'r') as z:
    z = z.read()
print(z)
with open('file.txt', 'w') as z:
    z = z.write('ok this is updated file')
print(z)