"""
Linting refers to the process of analyzing code to detect and report potential errors, stylistic issues, or
violations of programming conventions, without actually executing the code. In the context of Python, linting is 
used to ensure that code conforms to PEP 8 (the Python Enhancement Proposal that outlines the style guide for 
Python code) and other best practices.

---------------------------------------------------------------------------------------------------------
Popular Python Linters:
---------------------------------------------------------------------------------------------------------

- PyLint: One of the most well-known linters for Python. It checks the code against a vast collection of coding standards and heuristics.

- flake8: A wrapper around other tools (like pyflakes for logical errors and mccabe for complexity) and includes style checks against PEP 8.

- black: Often referred to as "The Uncompromising Code Formatter", black not only checks but also automatically reformats code to conform to its style. It doesn't offer as many configuration options as other tools, which is a deliberate choice to ensure consistency.

- mypy: While not a linter in the traditional sense, mypy checks Python code for type consistency using optional type hints introduced in Python 3.5.

- bandit: Focuses on finding common security issues in Python code.

---------------------------------------------------------------------------------------------------------
To Use above tools
---------------------------------------------------------------------------------------------------------

- pyline
    install it: pip install pylint
    how to use: pylint your_file.py
    If you have a specific configuration, you can specify it using the --rcfile flag: pylint --rcfile=path/to/config.rc your_file.py

what the --rcfile flag does in the context of PyLint?
PyLint provides a lot of checks and sometimes, you might want to enable or disable specific checks or customize the behavior of these checks. 
Instead of specifying these customizations every time you run PyLint, you can save them in a configuration file.
This configuration file is often referred to as the .pylintrc file. 
It contains all your preferences and custom rules for how PyLint should evaluate your code. 
You can have a global .pylintrc file for your whole system, a user-specific one, 
or even project-specific ones.


Using the --rcfile flag
When running PyLint, it will look for configuration in a default order, typically starting with the current directory for a .pylintrc file, 
then checking user-specific locations, and so on. If you want to specify a particular configuration file instead of 
letting PyLint search for it, you use the --rcfile flag followed by the path to your desired configuration file.

Let's say you have a configuration file stored in /myconfigs/pylint_config.rc. 
Instead of moving this file to your project directory or another location that PyLint checks by default, you'd run:
pylint --rcfile=/myconfigs/pylint_config.rc your_file.py

By doing this, you're telling PyLint to use the configuration settings from /myconfigs/pylint_config.rc when analyzing your_file.py.



- flake8
    install: pip install flake8
    usage: flake8 your_file.py
    configuration: Flake8's configuration can be stored in various files like .flake8, setup.cfg, or tox.ini.
By default, flake8 checks for logical and stylistic errors. You'll get a list of issues with line and column numbers.

- blake
    install: pip install black
    usage: black your_file.py
    Configuration: Black has very few configuration options by design. 
    However, some basic configurations can be stored in pyproject.toml:
"""

# Keep in min
# It's important to clarify that PyLint and flake8 itself does not "fix" or "format" code automatically like tools such as black or autopep8.
# Instead, PyLint/flake8 provides feedback on where your code does not conform to standards (like PEP 8) and suggests how to fix those issues.


# Trying to get feedback on below code with pylint
import math, sys


def example1():
    x = {"a": 37, "b": 42, "c": 927}
    y = "hello " "world"
    z = "hello " + "world"
    a = "hello {}".format("world")


class foo(object):
    def f(self):
        return 37 * -2

    def g(self, x, y=42):
        return y


def f(a):
    return 37 + -+a[42 - x : y**3]


# When we run pylint we get some error messages
'''
************* Module 126_linting
126_linting.py:2:0: C0301: Line too long (107/100) (line-too-long)
126_linting.py:3:0: C0301: Line too long (112/100) (line-too-long)
126_linting.py:4:0: C0301: Line too long (109/100) (line-too-long)
126_linting.py:7:0: C0301: Line too long (105/100) (line-too-long)
126_linting.py:9:0: C0301: Line too long (105/100) (line-too-long)
126_linting.py:11:0: C0301: Line too long (137/100) (line-too-long)
126_linting.py:13:0: C0301: Line too long (140/100) (line-too-long)
126_linting.py:15:0: C0301: Line too long (266/100) (line-too-long)
126_linting.py:17:0: C0301: Line too long (149/100) (line-too-long)
126_linting.py:21:0: C0301: Line too long (105/100) (line-too-long)
126_linting.py:23:0: C0301: Line too long (105/100) (line-too-long)
126_linting.py:28:0: C0301: Line too long (132/100) (line-too-long)
126_linting.py:31:0: C0301: Line too long (141/100) (line-too-long)
126_linting.py:32:0: C0301: Line too long (112/100) (line-too-long)
126_linting.py:40:0: C0301: Line too long (139/100) (line-too-long)
126_linting.py:41:0: C0301: Line too long (115/100) (line-too-long)
126_linting.py:42:0: C0301: Line too long (112/100) (line-too-long)
126_linting.py:45:0: C0301: Line too long (115/100) (line-too-long)
126_linting.py:48:0: C0301: Line too long (132/100) (line-too-long)
126_linting.py:55:0: C0301: Line too long (109/100) (line-too-long)
126_linting.py:56:0: C0301: Line too long (117/100) (line-too-long)
126_linting.py:66:0: C0301: Line too long (141/100) (line-too-long)
126_linting.py:67:0: C0301: Line too long (142/100) (line-too-long)
126_linting.py:1:0: C0103: Module name "126_linting" doesn't conform to snake_case naming style (invalid-name)
126_linting.py:71:0: C0410: Multiple imports on one line (math, sys) (multiple-imports)
126_linting.py:74:0: C0116: Missing function or method docstring (missing-function-docstring)
126_linting.py:76:0: W1404: Implicit string concatenation found in assignment (implicit-str-concat)
126_linting.py:78:8: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
126_linting.py:75:4: W0612: Unused variable 'x' (unused-variable)
126_linting.py:76:4: W0612: Unused variable 'y' (unused-variable)
126_linting.py:77:4: W0612: Unused variable 'z' (unused-variable)
126_linting.py:78:4: W0612: Unused variable 'a' (unused-variable)
126_linting.py:81:0: C0115: Missing class docstring (missing-class-docstring)
126_linting.py:81:0: C0104: Disallowed name "foo" (disallowed-name)
126_linting.py:81:0: R0205: Class 'foo' inherits from object, can be safely removed from bases in python3 (useless-object-inheritance)
126_linting.py:82:4: C0116: Missing function or method docstring (missing-function-docstring)
126_linting.py:85:4: C0116: Missing function or method docstring (missing-function-docstring)
126_linting.py:85:16: W0613: Unused argument 'x' (unused-argument)
126_linting.py:89:0: C0116: Missing function or method docstring (missing-function-docstring)
126_linting.py:90:25: E0602: Undefined variable 'x' (undefined-variable)
126_linting.py:90:29: E0602: Undefined variable 'y' (undefined-variable)
126_linting.py:71:0: W0611: Unused import math (unused-import)
126_linting.py:71:0: W0611: Unused import sys (unused-import)

------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)


So, these E(E0602), W(W0611), C stands for
R: means you have to refactor your code following the good practice
C: Your code violates the standard coding standards.
W: Warning for stylistic problems or some slight programming issues
E: Error - means there are important program issues
F: fata errors that stop code processing

'''