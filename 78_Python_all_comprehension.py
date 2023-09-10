#comprehension is a one linear for loop 


#suppose if we want to make a list of those numbers which are divisible by 5 then we do like this

# ls = []
# for i in range(100):
#     if i%5 == 0:
#         ls.append(i)
# print(ls)

#but it was a bit lengthy ..we can do this using list comprehension
#inside list 'for i in range(100)' this is for loop and 'i' at first written it prints the value ..and if part is condition

# [result for element in list]
ls = [i for i in range(100) if i%5 == 0]
print(ls)

#Dictionary Comprehension
#suppose we making dictionary having key item pairs 100...so worst way to make such type of dictionary that we create all items by ourself one by one
#and smarter way is using Dictionary Comprehension

print()
print("Dictionary Comprehension")
print()

dict1 = {i :f"item{i}" for i in range(100)} #and after for loop we can add condition in it
print(dict1)

print()
print("Value:Key pair - It is a reverse of key value pair")
print()
#we can even reverse the key value pair using Dictionary Comprehension
dict2 = {i:f"items{i}" for i in range(10)}
dict2 = {value:key for key, value in dict2.items()}
print(dict2)


print()
print("Sets Comprehension")
print()
clothes = {i for i in range(5)}
print(clothes)


print()
print("Generator Comprehension")
print()

this_is_gen = (i for i in range(5))
print(this_is_gen)
print(this_is_gen.__next__())
print(this_is_gen.__next__()) #..and so on