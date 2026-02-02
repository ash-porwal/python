"""
String all methods - Python 3.11
================================

This module documents commonly used Python string (`str`) methods.

General Notes
-------------
• Strings are immutable — methods return new values.
• Any modification creates a new object in memory
• Methods do NOT modify the original string.
• Strings are ordered and supports indexing and slicing
Note: Ordered means each character has a fixed position (index), and we can access characters using indexing

General Syntax
--------------
result = string.method(param1, param2, ...)
"""

# ---------------------------------------------------------------------
# SAMPLE STRINGS
# ---------------------------------------------------------------------

s = "hello World! 123"
s2 = "   extra space   "

# ---------------------------------------------------------------------
# STRING METHODS
# ---------------------------------------------------------------------

# capitalize()
# Syntax: str.capitalize()
# Params: none
# Returns: str
print(s.capitalize())  # Hello world! 123

# casefold()
# Syntax: str.casefold()
# Returns: str
print("HELLO WORLD!".casefold())  # hello world!

# center()
# Syntax: str.center(width[, fillchar])
# Returns: str
print("hello".center(20, '-'))  # -------hello--------

# count()
# Syntax: str.count(sub[, start[, end]])
# Returns: int
print(s.count('l'))  # 3

# encode()
# Syntax: str.encode(encoding='utf-8', errors='strict')
# Returns: bytes
print(s.encode())  # b'hello World! 123'

# endswith()
# Syntax: str.endswith(suffix[, start[, end]])
# Returns: bool
print(s.endswith('123'))  # True

# expandtabs()
# Syntax: str.expandtabs(tabsize=8)
# Returns: str
print("hello\tworld!".expandtabs(4))  # hello   world!

# find()
# Syntax: str.find(sub[, start[, end]])
# Returns: int
print(s.find('World'))  # 6

# format()
# Syntax: str.format(*args, **kwargs)
# Returns: str
print("Hello, {}!".format("world"))  # Hello, world!

# format_map()
# Syntax: str.format_map(mapping)
# Returns: str
print("Hello, {name}!".format_map({"name": "world"}))  # Hello, world!

# index()
# Syntax: str.index(sub[, start[, end]])
# Returns: int
print(s.index('World'))  # 6

# isalnum()
# Syntax: str.isalnum()
# Returns: bool
print(s.isalnum())  # False

# isalpha()
# Syntax: str.isalpha()
# Returns: bool
print("hello".isalpha())  # True

# isascii()
# Syntax: str.isascii()
# Returns: bool
print(s.isascii())  # True

# isdecimal()
# Syntax: str.isdecimal()
# Returns: bool
print("123".isdecimal())  # True

# isdigit()
# Syntax: str.isdigit()
# Returns: bool
print("123".isdigit())  # True

# isidentifier()
# Syntax: str.isidentifier()
# Returns: bool
print("variable1".isidentifier())  # True

# islower()
# Syntax: str.islower()
# Returns: bool
print("hello".islower())  # True

# isnumeric()
# Syntax: str.isnumeric()
# Returns: bool
print("123".isnumeric())  # True

# isprintable()
# Syntax: str.isprintable()
# Returns: bool
print(s.isprintable())  # True

# isspace()
# Syntax: str.isspace()
# Returns: bool
print(s2.isspace())  # False

# istitle()
# Syntax: str.istitle()
# Returns: bool
print(s.istitle())  # False

# isupper()
# Syntax: str.isupper()
# Returns: bool
print("HELLO".isupper())  # True

# join()
# Syntax: separator.join(iterable)
# Returns: str
print(", ".join(["1", "2", "3"]))  # 1, 2, 3

# ljust()
# Syntax: str.ljust(width[, fillchar])
# Returns: str
print("hello".ljust(10, '-'))  # hello-----

# lower()
# Syntax: str.lower()
# Returns: str
print("HELLO".lower())  # hello

# lstrip()
# Syntax: str.lstrip([chars])
# Returns: str
print(s2.lstrip())  # extra space   

# maketrans() & translate()
trans = str.maketrans('lo', 'ol')
print("hello world".translate(trans))  # heoll worold

# partition()
# Syntax: str.partition(sep)
# Returns: tuple
print("hello world".partition(' '))  # ('hello', ' ', 'world')

# removeprefix()
# Syntax: str.removeprefix(prefix)
# Returns: str
print("testcase".removeprefix("test"))  # case

# removesuffix()
# Syntax: str.removesuffix(suffix)
# Returns: str
print("testcase".removesuffix("case"))  # test

# replace()
# Syntax: str.replace(old, new[, count])
# Returns: str
print("hello world".replace("world", "Python"))  # hello Python

# rfind()
# Syntax: str.rfind(sub[, start[, end]])
# Returns: int
print("hello world world".rfind('world'))  # 12

# rindex()
# Syntax: str.rindex(sub[, start[, end]])
# Returns: int
print("hello world world".rindex('world'))  # 12

# rjust()
# Syntax: str.rjust(width[, fillchar])
# Returns: str
print("hello".rjust(10, '-'))  # -----hello

# rpartition()
# Syntax: str.rpartition(sep)
# Returns: tuple
print("hello world world".rpartition('world'))  # ('hello world ', 'world', '')

# rsplit()
# Syntax: str.rsplit(sep=None, maxsplit=-1)
# Returns: list[str]
print("hello world world".rsplit(' '))  # ['hello', 'world', 'world']

# rstrip()
# Syntax: str.rstrip([chars])
# Returns: str
print(s2.rstrip())  #    extra space

# split()
# Syntax: str.split(sep=None, maxsplit=-1)
# Returns: list[str]
print("hello world".split(' '))  # ['hello', 'world']

# splitlines()
# Syntax: str.splitlines(keepends=False)
# Returns: list[str]
print("hello\nworld".splitlines())  # ['hello', 'world']

# startswith()
# Syntax: str.startswith(prefix[, start[, end]])
# Returns: bool
print("hello".startswith('he'))  # True

# strip()
# Syntax: str.strip([chars])
# Returns: str
print(s2.strip())  # extra space

# swapcase()
# Syntax: str.swapcase()
# Returns: str
print("Hello World".swapcase())  # hELLO wORLD

# title()
# Syntax: str.title()
# Returns: str
print("hello world".title())  # Hello World

# upper()
# Syntax: str.upper()
# Returns: str
print("hello".upper())  # HELLO

# zfill()
# Syntax: str.zfill(width)
# Returns: str
print("42".zfill(5))  # 00042
