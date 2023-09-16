"""
Python was released by Guido van Rossum in 1991

- Python is Interpreted Language - Interpreted means that the code is executed line by line and needs to be compiled.

- Python is Dynamically typed Language - means the type of our variables are going to be checked at run time and not at the compiled time.
    So, in python if we run print(1 + "hello") it is going to give error after running the code, but if it were a Static typed language
    then it wouldn't even allow to run print(1 + "hello").

- Python is a high level language - When we say "Python is a high-level language," 
    we're referring to the level of abstraction between the language and the computer's hardware. 
    Means - Python's syntax is closer to human language, making it easier to read and write. We don't need to write code in that language which machine understands.
    So, python code gets converted into machine code but we dont do it from our side, it is automatic.
    In Low level language we would be writing code in that syntax which machine would understand. like: 0110000111000


- PEP 8 is the style guide for writing Python code. PEP 8 itself is just a document that describes the conventions for writing readable Python code.

- There are tools that have been created to check your code against the PEP 8 guidelines, 
  and these tools can issue warnings if your code doesn't adhere to the conventions.
  One popular tool is flake8. 
  When you run flake8 on your Python code, it checks for violations of PEP 8 guidelines and other potential programming issues, then warns you about them.

  Just in case if want to use flake8
  pip install flake8
  flake8 your_python_file.py


"""