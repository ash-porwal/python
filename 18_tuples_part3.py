# Type casting in tuple

# Suppose if we have one type where all elements are int, then we do type casting like below, 
# for indefinite tuples.

numbers: tuple[int, ...] = (1,2,3,4)

# if that tuple contains multiple data type, then we divide them with | pipe symbol, it stands for OR
numbers: tuple[int | str, ...] = (1,2,3,4, "Ash")