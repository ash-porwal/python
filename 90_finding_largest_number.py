#suppose we have a list of numbers or we take the list of numbers from user, so to print the largest number we will
#be creating a variable and assign it value -1 and we will suppose this is the largest number we have seen so far
#so now we will compare -1 with each element of the list 

largest_number = -1
number_list = [55,46,1,34,99,23, 11]

for num in number_list:
    if num > largest_number:
        largest_number = num
    print(largest_number, num)

print("This is the largest number - ", largest_number)