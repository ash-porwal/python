"""
String all methods - Python3.11

'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 
'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 
'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
"""

s = "hello World! 123"
s2 = "   extra space   "

# capitalize
print(s.capitalize())  # Hello world! 123

# casefold
print("HELLO WORLD!".casefold())  # hello world!

# center
print("hello".center(20, '-'))  # -------hello--------

# count
print(s.count('l'))  # 3

# encode
print(s.encode())  # b'hello World! 123'

# endswith
print(s.endswith('123'))  # True

# expandtabs
print("hello\tworld!".expandtabs(4))  # hello   world!

# find
print(s.find('World'))  # 6

# format
print("Hello, {}!".format("world"))  # Hello, world!

# format_map
print("Hello, {name}!".format_map({"name": "world"}))  # Hello, world!

# index
print(s.index('World'))  # 6

# isalnum
print(s.isalnum())  # False (due to space and exclamation mark)

# isalpha
print("hello".isalpha())  # True

# isascii
print(s.isascii())  # True

# isdecimal
print("123".isdecimal())  # True

# isdigit
print("123".isdigit())  # True

# isidentifier
print("variable1".isidentifier())  # True

# islower
print("hello".islower())  # True

# isnumeric
print("123".isnumeric())  # True

# isprintable
print(s.isprintable())  # True

# isspace
print(s2.isspace())  # False

# istitle
print(s.istitle())  # False

# isupper
print("HELLO".isupper())  # True

# join
print(", ".join(["1", "2", "3"]))  # 1, 2, 3

# ljust
print("hello".ljust(10, '-'))  # hello-----

# lower
print("HELLO".lower())  # hello

# lstrip
print(s2.lstrip())  # "extra space   "

# maketrans & translate
trans = str.maketrans('lo', 'ol')
print("hello world".translate(trans))  # heoll worold

# partition
print("hello world".partition(' '))  # ('hello', ' ', 'world')

# removeprefix (Python 3.9+)
print("testcase".removeprefix("test"))  # case

# removesuffix (Python 3.9+)
print("testcase".removesuffix("case"))  # test

# replace
print("hello world".replace("world", "Python"))  # hello Python

# rfind
print("hello world world".rfind('world'))  # 12

# rindex
print("hello world world".rindex('world'))  # 12

# rjust
print("hello".rjust(10, '-'))  # -----hello

# rpartition
print("hello world world".rpartition('world'))  # ('hello world ', 'world', '')

# rsplit
print("hello world world".rsplit(' '))  # ['hello', 'world', 'world']

# rstrip
print(s2.rstrip())  # "   extra space"

# split
print("hello world".split(' '))  # ['hello', 'world']

# splitlines
print("hello\nworld".splitlines())  # ['hello', 'world']

# startswith
print("hello".startswith('he'))  # True

# strip
print(s2.strip())  # "extra space"

# swapcase
print("Hello World".swapcase())  # hELLO wORLD

# title
print("hello world".title())  # Hello World

# upper
print("hello".upper())  # HELLO

# zfill
print("42".zfill(5))  # 00042
