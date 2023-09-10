for x in range (6):
    print(x)
    if x == 3:
        # pass
        break
else:
    # it works like this if everything is going to successfully execute in a for loop then it is going to print else block, if we got break statement then it wont go in else block
    print("Successfully loop done") 


# we can also turncate the new line in print statement, we just need to define it -> end=
for x in range (6):
    print(x, end=' ')
else:
    print("Successfully loop done")
