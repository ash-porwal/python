def do_something(num: int):
    print(num)
    if num == 1:
        print("Breaking function")
        return  # in function return works like break, as it will exit the function and returning nothing

    # we are calling the function again
    do_something(num-1)


do_something(5)
