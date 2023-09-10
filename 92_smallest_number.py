'''
To find the smallest number we are going to take our variable as None
'''

smallest_value = None

number_list = [55,46,1,34,99,23, 11]
for num in number_list:
    if smallest_value == None:
        smallest_value = num
    elif smallest_value > num:
        smallest_value = num

print("This is the smallest value", smallest_value)