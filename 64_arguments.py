# Convention (normal argument, *args, **kwargs)
# we use * when we want to take unlimited amount of arguments,
# for example when we use print() function then we can print any amount of values -> print('a') or print(1,2,3,4) so it takes unlimited amount of arguments

# similarly we can achieve this in our custom function we just have to define * with arguments and if it is a keyword argument then we can define with two **
# *kwargs for dictionary
def fun1(*x, **y):
    # print(x[2])
    print(x)
    print(type(x))
    print(y)


list1 = ["a", "b", "c", "d", "e"]
fun1(*list1)

dic1 = {"a": 1, "b": 2, "c": 3}
fun1(**dic1)

def some_fun(*name: str, age: int) -> None:
    print(name, age)

some_fun("a", "b", age=10) # when we define args then to assign value to age, we have to explicitly define age