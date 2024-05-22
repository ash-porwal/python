x = [1, 2, 3]
y = x
y.append(4)
print(x) # output?


# -------------
def append_elem(lst, elem): # proof that value is passed as reference in python
    lst.append(elem)

x = [1, 2, 3]
append_elem(x, 4)
print(x) # output?


# ---------------
x = [1, 2, 3]
y = x
y = [4, 5, 6]
print(x) # output?
print(y) # output?


# -------------

x = [1, 2, 3, 4, 5]
y = x[:]
y[0] = 10
print(x)
print(y)



# -------------
x = {'a': 1, 'b': 2}
y = x
y['a'] = 10
print(x)

