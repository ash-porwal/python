# "match-case" refers to a pattern matching construct introduced in Python 3.10

def describe_value(x):
    match x:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case 2:
            return "Two"
        # this is how we can use operators
        case 1 | 2:
            print("This is OR condition")
        # we can even put a if condition
        case 55 if x == 55:
            print("This is 55")
        # The _ in the case block serves as a "catch-all" wildcard.
        # it will match any value
        case _:
            return "Other"

print(describe_value(0))  # Output: Zero
print(describe_value(1))  # Output: One
print(describe_value(2))  # Output: Two
print(describe_value(5))  # Output: Other
