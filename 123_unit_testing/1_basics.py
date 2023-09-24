"""
Unit tests are segments of code written to test other pieces of code, typically a single 
function or method, that we refer to as a unit.

Python has two main frameworks to make unit testing easier: unittest and PyTest.
unittest has been part of Python's standard library since Python 2.1 but Pytset is easier to install.


unittest module provides tools for testing your code. Here's a basic guide to get started:

1. Setting up a Test:

    - First, you'll need to import the unittest module and the function or class you want to test.
    - Create a test class that inherits from unittest.TestCase
    - Within this class, define methods that will test different parts of your code.

2. Writing a Simple Test:
    - Let's say you have a function called formatted_name() 
      that takes a first and last name and returns them in a formatted manner:

    def formatted_name(first, last):
        return f"{first.title()} {last.title()}"
    
        
    To test this function:

    import unittest
    from your_module import formatted_name

    class NamesTestCase(unittest.TestCase):
        def test_formatted_name(self):
            full_name = formatted_name('john', 'doe')
            self.assertEqual(full_name, 'John Doe')

3. Running the Test:
   - If you save your test in a file named test_module.py, you can run it from the command line using:
   python -m unittest test_module.py

   # If the test passes, no output will be shown. If it fails, unittest will tell you why.
"""
# Example
# import unittest
# from test_file import formatted_name

# class NamesTestCase(unittest.TestCase):
#     def test_formatted_name(self):
#         full_name = formatted_name('john', 'doe')
#         self.assertEqual(full_name, 'John Doe')


"""
Concept to cover: Arrange-Act-Assert model

    - In this first we want to arrange or set up the condition for a test.
    - Then we want to act upon that test by calling the function that you are trying to test.
    - Then we want to see if the results are what you expected them to be.

And as pytest is easier to use, we are going to import it
"""

import pytest

# Now to create a test, you just need to create a function that starts with word 'test'

def test_some_fun():
    assert True

# Now to test it, simply type pytest in module
# In your terminal or command prompt, navigate to the directory containing your test file.
# Run the test by simply typing: pytest <file_name>.py



# lets try to fail a test
# def test_some_fun_fails():
#     assert False
 
def add(a, b):
    return a + b

def test_add():
    result = add(3, 5)
    assert result == 8

# so, here steps are going to involve like

class TestGroup:
    def test_add(self):
        a, b = 1, 1 # Arrange

        actual = add(a,b) # Act

        expected = 2

        assert actual == expected # Assert