#Methods of lsits
check = [1, 56, 76, 89, 2, 0, -5]
#.sort- this function will short the list means it will make values in ascending order.
check.sort() # this uses Timsort, it is a hybrid of - merge and insertion sort
print(check)

#.reverse ... this function will reverse the list
check.reverse() 
print(check)

#.append ..... adds something at the end of the list
check.append(32)
check.append(36)
check.append("Cool")
print(check)

#.insert ..this will add that value in the place of index
#syntax - list_name.insert(position, element)
check.insert(0, 66)
print(check)
check.insert(2, 66)
print(check)

#.pop(index_number) ...to remove that particular index but if you leave paranthesis empty like this .pop() then it will remove last item
check.pop(1)
print(check)

#.remove(that value which need to delete)
check.remove(66)
# check.remove(66)
print(check)