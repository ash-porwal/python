# we can use assert like below
def some_fun(some_dict: dict):
    """
    Check if the provided parameter is a dictionary.
    
    Args:
    - some_dict (dict): The dictionary to be checked.
    
    Raises:
    - AssertionError: If the provided parameter is not a dictionary.
    
    Returns:
    - None

    Example:
    >>> some_fun({})
    >>> some_fun([])  # This will raise an AssertionError with the message "The parameter is not a dict"
    
    Note:
    This function does not perform any operation other than checking the type.
    """

    # assert expression[, message]
    assert isinstance(some_dict, dict), "The parameter is not dict"

    # we can check on below too
    # assert y > 0, "y should be greater than 0"  





value = {
    "Name": 'Ashihs',
    "Language": 'Python'
}
# value = 'ash'
some_fun(value)

# So happening above is we are checking if that parameter is dict or not with isinstance.
# if it is not dict type then it is going to raise error with message whatever we have wrriten.

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

product_info = {'name': 'Shirt', 'price': 3000}
print(apply_discount(product_info, 0.25))  # This will work fine

# Uncommenting the following will raise an AssertionError because of the excessive discount
# print(apply_discount(product_info, 1.25))

# If we run python file like this: python3 -O 105_assert.py (this is called debug mode is False)
# then assertion statements are going to get ignored

# So above I defined doc strings too, and when python program runs doc strings consume memory,
# so if we want python program to run without docstring then I would run it as: python3 -OO  105_assert.py