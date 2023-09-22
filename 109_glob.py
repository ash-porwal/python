"""
The glob module find all the pathnames matching a specified pattern according to the rules used by the Unix shell. 
It's especially useful when you want to work with files that have a certain naming pattern in a directory. 
"""
import glob

# lets check if any json file presents in /tmp directory or not
print(glob.glob('*.json', root_dir='/tmp')) # glob.glob(<path_name>) takes path name, and we can use linux Wildcards.
# if the file doesn't exists in that file then it is going to return an empty list.

# if we want to search just in subdirectories
print(glob.glob('*/*.json', root_dir='/tmp'))

# if we want to search recursively
# recursive parameter, which, when set to True, will search for files in subdirectories recursively.
print(glob.glob('**/*.json', root_dir='/tmp', recursive=True))

"""
-----------------------------------------------------
* matches any sequence of characters in a filename or directory name, but it doesn't span directory separators.
-----------------------------------------------------
** matches any sequence of characters, including directory separators (i.e., it can match across multiple directory levels).
"""

# glob.iglob() is an iterator which yields the same values as glob() would return, 
# but without storing all the names in memory at once. 
# This can be useful if you're dealing with a very large number of files:
for filename in glob.iglob('*.txt'):
    print(filename)

