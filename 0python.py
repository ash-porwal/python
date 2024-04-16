"""
Python was released by Guido van Rossum in 1991
-----------------------------------------------

-----------------------------------------------
- Python is Interpreted Language -
  That means that, unlike languages like C and its variants, Python does not need to be compiled before it is run. Other interpreted languages include PHP and Ruby.

- Python is Dynamically typed Language - means the type of our variables are going to be checked at run time and not at the compiled time.
    dynamically typed, this means that you don't need to state the types of variables when you declare them or anything like that. 

- In Python, functions are first-class objects. 
  This means that they can be assigned to variables, returned from other functions and passed into functions. Classes are also first class objects

- Python is a high level language - When we say "Python is a high-level language," 
    we're referring to the level of abstraction between the language and the computer's hardware. 
    Means - Python's syntax is closer to human language, making it easier to read and write. We don't need to write code in that language which machine understands.
    So, python code gets converted into machine code but we dont do it from our side, it is automatic.
    In Low level language we would be writing code in that syntax which machine would understand. like: 0110000111000
-----------------------------------------------


-----------------------------------------------
- PEP 8 - stands for Python Enhancement Proposal
  is the style guide for writing Python code. PEP 8 itself is just a document that describes the conventions for writing readable Python code.

- There are tools that have been created to check your code against the PEP 8 guidelines, 
  and these tools can issue warnings if your code doesn't adhere to the conventions.
  One popular tool is flake8. 
  When you run flake8 on your Python code, it checks for violations of PEP 8 guidelines and other potential programming issues, then warns you about them.

  Just in case if want to use flake8
  pip install flake8
  flake8 your_python_file.py
-----------------------------------------------

-----------------------------------------------
- Difference between scriptig and programming language?
  Scripting means - to automate the certain tasks, scripting languages don't require compilation steps and they are interpreted.
  Example: Java code needs to be compiled before running.
  Where - Python, PHP, JS - needs no compilation

  So, Programming languages are compiled whereas scripting languages are interpreted.
  But Python can also compile its code into bite code and then interpret it.
-----------------------------------------------

-----------------------------------------------
- difference between .py and .pyc file?
  
  .py Files:
    These are plain text files containing Python code.
    They are the files you write and edit, containing the source code of a Python program.
    These files are human-readable and need to be interpreted by the Python interpreter to execute the code.
  
  .pyc Files:
    These files are compiled Python files. 
    Python converts .py files into .pyc files as an intermediate step between reading the source code and executing the program.
    The bytecode compilation happens automatically. When you run a Python program, the interpreter first checks to see if the corresponding .pyc file exists and is up-to-date.
    They are stored in a __pycache__ directory under the directory containing the .py file.

  When .pyc files are created:
  .pyc files get created when a .py file is imported as a module in another Python script. The interpreter compiles the .py to .pyc to speed up future imports of the same module.
-----------------------------------------------

-----------------------------------------------
- What are Python namespaces?
  A namespace is a naming system used to make sure that names are unique to avoid naming conflicts.
  namespaces are like an organized storage system where every object (like variables and functions) gets a unique name that identifies it. When you create an object, Python keeps track of its name and where it belongs in your program. This tracking is done in a way similar to a dictionary, where each name (key) is linked to its location (value). 

  There are four main types of namespaces in Python, each serving different purposes:

  1. Built-in Namespace: This contains all the pre-defined objects that Python provides. These are always available and include functions like print() and len().

  2. Global Namespace: This is for objects that you create at the main program level, outside of any functions. Anything defined here can be accessed from anywhere within the program unless blocked by a local namespace.

  3. Enclosing Namespace: This involves names defined in any outer functions. If you have a function inside another function, the outer function's namespace is 'enclosing'. It affects the inner function but not the main program directly.

  4. Local Namespace: This is for names used inside a function. They exist only while the function is running and can't be accessed outside of it.
-----------------------------------------------





    



"""