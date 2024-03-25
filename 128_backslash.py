# The backslash (\) serves as an escape character in Python and has several uses. 
"""
Here are the primary applications of the backslash in Python:

String Escapes: 
In string literals, the backslash is used to escape characters that otherwise have a special meaning.
    \\ : Backslash (\)
    \' : Single quote (')
    \" : Double quote (")
    \n : Newline
    \t : Tab
    \r : Carriage return
    \b : Backspace
    \f : Form feed
    \a : Bell (makes a sound, rarely used)
    \v : Vertical tab (rarely used)
    \ooo : Octal value (e.g., \012 for newline)
    \xhh : Hex value (e.g., \x0a for newline)
    \uhhhh : 16-bit hex value (Unicode, e.g., \u03B1 for Greek alpha)
    \Uhhhhhhhh : 32-bit hex value (Unicode)
"""
print("This is a tab:\tSee?")
print("This is a newline:\nNew line starts here.")

# Line Continuation:  The backslash can be used to indicate that a statement spans multiple lines.
s = "This is a very long string that " \
    "spans multiple lines for better readability."

# Raw Strings: 
# Strings prefixed with an r or R treat backslashes as literal characters and do not interpret them as escape characters.
print(r"This is a raw string. Newlines are not interpreted: \n See?")

# Path Representation: 
# On Windows, paths use backslashes. 
# However, because the backslash is also an escape character in Python strings, 
# you often use either double backslashes (\\) or raw strings.
path1 = "C:\\Users\\User\\Documents"
path2 = r"C:\Users\User\Documents"
