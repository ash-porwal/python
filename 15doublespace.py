#to detect if there is doubespace in program
d = "This is test of double space  ok"
ds = d.find("  ") #this will return index number
print(ds) #if there is double space in program then it will give some value otherwise return -1