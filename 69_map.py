#we can do type casting using map of every item in list
# map(function, iterable, ...)
print("******This is Map******")
list1 = ["2","3","4","34","23","31"]
num = list(map(int, list1))
num = tuple(map(int, list1))
# print(num[2]+2)
print(type(num))
print((num))

list2 = [1,2,3,4,5]
number = list(map(str,list2))
print(type(number[0]))

print()
print("**********")
print()

def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]
for i in range(1, 10):
    val = list(map(lambda x: x(i), func)) #lambda x says x ek function hai jo return karta hai funcation ka naam with value of i...and yaha par func likha hai jo ki bol raha hai wo lambda function func list ke har ek item par lag raha hai
    #for an instance lambda x takes def square function with value i which is 0 while running first time
    print(val)


#Filter function - ye ek aisi list banata hai elments ki jispe given function true return karta hai
print()
print("******This is Filter******")

list4 = [1,2,3,4,5,6,7,8,9]
def greater(num):
    return num>5 #ab agar number greater than 5 hai to True return karega otherwise False return karega

#creating list with number greater than 5
#filter syntax - filter(function, Iterables)
gr_than_5 = list(filter(greater, list4)) #we have passed function name and list name
print(gr_than_5) #if we do not type cast gr_than_5 (at line 4) into list then it will return Filter object

print()
print("******This is Reduce******")
#if we write reduce directly then nothing will happen because this function is the part of the funtool library 
from functools import reduce
#so what reduce does is it add or product or do any operations on list items
list5 = [1,2,3,4,5]
#here we made lambda function and it returns x+y..and this function should be applied on list5
numms = reduce(lambda x,y: x+y, list5) 
print(numms)