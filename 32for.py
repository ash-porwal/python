fruits = ['Apple', 'Oranges', 'Mangoes', 'Pineapple', 'Onion']
for item in fruits:
    print(item)
print()

# Below is the quiz

for item in fruits:

    if item == "Mangoes":
        fruits.remove("Mangoes")

    # we will notice it will skip the Pineapple iteration
    print(item)

    # above happened because when we removed one item, the list got updated and shifted next index to that removed item, 
    # and as it already got iterated to that index number, so it will skip iterating to that index
    print(list(enumerate(fruits)))

# Only way to fix it is to make copy of original list or we can use list comprehension
print()
fruits = ['Apple', 'Oranges', 'Mangoes', 'Pineapple', 'onion']
for item in fruits.copy():
    if item == "Mangoes":
        fruits.remove("Mangoes")

    print(item)

