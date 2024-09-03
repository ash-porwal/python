'''
We can open file in 4 different modes:
1. open('/path/to/file', 'r') # in read mode
2. open('/path/to/file', 'w') # in write mode - this overwrite the file
3. open('/path/to/file', 'a') # in appending mode
4. open('/path/to/file', 'x') # create a specific file

Then we can open files in text or binary mode
- open('/path/to/file', 'rt') # in read mode - text
- open('/path/to/file', 'rb') # in read mode - binary # we read Images or Videos files in binaries

there are two types of files
    text file - stores data in form of strings and characters
    binary files - it stores data in form of bytes, a group of 8 bytes each. It is use to store image, video, pdf, csv, audio
'''


# python has built-in function to open or close the file it is... open("file name", "r/w")here r or w stands for if want to read type r otherwise w
f = open("file.txt", "r") #if we do not write "r" here then by default it is r
data = f.read()
# data = f.read(6) #if we write some number inside paranthesis like f.read(5) then it will read first 5 character {including spacebar}
print(data)
# once we opened the file so we have to close too
f.close()