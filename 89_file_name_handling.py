file_name = input("Enter the file which you want to read: ")
try:
    file = open(f"{file_name}")
except:
    print(f"{file_name} file doesn't exists")
    quit()
for line in file:
    line = line.strip()
    print(line)