def some_funtion(name:str, age: int, /): #here / defines that these are postional only argument before / and should be passed in postion as it is 
    print(name, age)

# some_funtion(name='ash', age=5) # this will throw error because in this we are defining arguments with keys, which is wrong because of / placed in parameter
some_funtion('ash', 26) # this is correct way


# In case of keyword argument, we define * and any parameter after * we want to assign its value with the keyword of that parameter otherwise * is gonna absorb everything
def key_word_arguement(*, name: str, age: int):
    print(name, age)

key_word_arguement(name='ash', age=26) # so we ca only reach name and age only by referring to them

# here is combined example of keyword and positonal arguments
def combine_example(pos_only1, pos_only2, /, standard1, standard2, *, kwd_only1, key_only2): 
    print(pos_only1, pos_only2, standard1, standard2, kwd_only1, key_only2)

combine_example('first_postional', 'second_postional',)

'''
positional arguments: we need to define them as it is in the same order, and we cannot assign its value with the keywords.
standard arguemnt: we assign its value either with keyword or directly.
keywords argument: we can only define their value with keyword otherwise * is gonna absorb everything
'''