#Lambda functions or anonymous function..it is a one liner function
#Lambda definition does not include a “return” statement, it always contains an expression that is returned.
def fun1(x, y):
    return x-y
print(fun1(5, 1))

# lambda arguments: expression
fun2 = lambda x, y : x - y
print(fun2(4, 3))

# we dont write lambda expression directly like below, because it is not going to return anything
# lambda x, y : x - y
# so what I did, I assign fun2 = lambda x, y : x - y
# then basically my function name is fun2 now, which has two parameters x and y
# so now i can call this function - fun2(4, 5)

#so this both ways to create function fun1 and fun2 

print()
print("***********")
print()

def fun4(a):
    print(a[1])
    return a[1]

list1 = [[1, 45], [56, 11], [12, 2]]  
list1.sort(key= fun4) #in sort key takes an argument we can pass functions inside it
# in line no. 20 this will sort all elements at index 1 of every sub list 
print(list1)

#So we can use lambda function 
list2 = [[20, 30], [5, 44], [60, 90]]
list2.sort(key = lambda x:x[1])
print(list2)

# Please note type hinting is not valid in lambda