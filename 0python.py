"""
Python was released by Guido van Rossum in 1991
-----------------------------------------------

-----------------------------------------------
- Python is Interpreted Language -
  That means that, unlike languages like C and its variants, Python does not need to be compiled before it is run. Other interpreted languages include PHP and Ruby.
  Programs written in interpreted languages are executed by an interpreter, which reads the source code line-by-line or block-by-block, translates it into machine code, and runs it immediately. This process happens every time the program is run.

  Compiled Languages: Programs written in compiled languages are transformed (compiled) into machine code by a compiler before they are run. The output is a standalone executable file that can be run on its own without further translation. This compilation is done only once, and the executable can be run many times afterward.

- Python is Dynamically typed Language - 
    Python is described as a dynamically typed language because the type of a variable is determined at runtime, not in advance.
    dynamically typed, this means that you don't need to state the types of variables when you declare them or anything like that. 

    Advantages of Dynamic Typing:
      1. Rapid Development: Faster prototyping and fewer lines of code to write since there is no need to define types.
      2. Ease of Learning: Simplifies the learning curve for new programmers because they can focus on programming concepts without worrying about static type definitions.
      3. High Flexibility: Supports polymorphism seamlessly, allowing the same function to process objects of different classes.
    Disadvantages of Dynamic Typing:
      1. Performance: Generally, dynamically typed languages are slower than statically typed languages because type checking is done at runtime.
      2. Potential for Runtime Errors: Errors related to type mismatch might only occur at runtime, which can lead to bugs that are detected later in the development cycle or even after deployment.
      3. Lack of Immediate Clarity: In larger codebases or with multiple developers, it might be less clear what type of data a function expects or returns, leading to misuse or bugs.

- In Python, functions are first-class objects. 
 "first-class object" refers to any entity that can be dynamically created, destroyed, passed to a  
  function, returned as a value, and assigned to a variable.
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


-----------------------------------------------
- Different types of memory in Python?
  Types of memory - 
  1. Stack memory - all methods, function calls, references are stored in this.
  2. Private heap memory - all values and objects are stored

  for example
  x = 5
  so, here x is referring to an object so it will get saved in Stack memory
  while 5 is value, so will get saved in Private heap 

  >>> x = 5
  >>> id(x)
  4309451120
  >>> x = x+1 # here now x is refering to the new memory location
  >>> id(x)
  4309451152
  >>> 
  >>> y = 5 # as 5 was already in Private heap, so y is now pointing to the same memory location.
  >>> id(y)
  4309451120 # see? same id as x
  >>> 
  So, if we get something in Heap memory, so one or more than one object can refer that heap memory.

     
  When, there a value in Private Heap memory and no object refers to that memory, then
  that value in heap memory is considered as Dead object - and this mechanism is called reference counting. And that dead value will move to grabage collector

- How Memory is managed in Python?
  Python manages its memory through a private area called the "heap" where all Python objects and values are stored. This area is only accessible by the Python interpreter, which means regular programs can't access it directly.

  Here's how Python handles memory:
  1. Memory Allocation: Python has a memory manager that takes care of setting aside memory in the heap for Python objects. This system makes sure Python programs have the memory they need to run.

  2. Garbage Collection: Python uses a built-in system called a "garbage collector" to reclaim memory once objects are no longer needed. When a Python object is no longer used by the program (meaning nothing in the program is referring to it anymore), the garbage collector removes it from memory. This process helps Python make efficient use of memory by freeing up space that's no longer being used.

- What do you mean by Grabage collector and reference counting?
  Reference counting:
    Reference counting is memory management technique, where each object in memory keeps a count of the number of references pointing to it. When an object is created, its reference count is initialized to 1 and when the object gets dellocated when there is no reference to that in program.
    there reference are always counted and stored in the memory.
    When reference count of an object reaches 0 then reference counting garbage collection algorithm
    cleans up the object immediately.
    for example - x=5 # in this x is pointing to 5, so it has one reference 
    now, if we delocate and point x to a new value then nothing is pointing to 5 thus reference count becomes 0, so now reference counting garbage collection algorithm will get trigger and cleans up the memory.
  
  Garbage collector:
    Python deleted unwanted objects automatically to free the memory space.
    The process by which Python cleans up the memory and reclaim the memory is called Garbage Collector.
    Python garbage collector runs during the program execution and is triggerd when object is 
    reference count reaches 0.
    The gc module defines the function to enable or disable garbage collector
    - gc.enable()
    - gc.disable()


- What is Duck typing and why python is called dynamically types language?
  Python don't have problem with if we don't declare the type of the variable.
  It gets to type of variable in the runtime.
  Python also takes care of the memory management that's why Python is a dynamically typed language.

-----------------------------------------------


-----------------------------------------------
- Module vs Packages vs Libraries
  Module - it is a code file which contains collection of functions, classes and variables (example - random module, JSON, OS)
  Packages - it is a collection of module, and this package dir will also have __init__.py so that we can import modules.
            and in general we import module from packages 
  Library - it is a collection of python packages(example - requests, Pandas, Numpy)
-----------------------------------------------

-----------------------------------------------
- Difference between range & xrange
  xrange was in python2
  range is in pyhton3
  The only difference is that range returns a Python list object 
  and xrange returns generator object. It creates the values as you need them with a special technique called yielding. That's is why xrange is called lazy evaluation.

  For example:
    a = range(1, 5000)
    b = xrange(1, 5000)

    print("The return type of range() is : ")
    print(type(a)) # list object

    print("The return type of xrange() is : ")
    print(type(b)) # xrange object
  
  Memory consumtion of range is higher as compare to xrange
  we can proof this with
  print(sys.getsizeof(a))
  print(sys.getsizeof(b))

  1. xrange of Python2 is now range in Python3
  2. as range returns list object, so it is better than xrange when it comes to operation.
  3. xrange is faster than range


-----------------------------------------------

-----------------------------------------------
- What is pickling and unpickling?
  Pickling is the process of converting a Python object into a byte stream. so that it can be saved in file.
  This serialized form of the object can be stored in a file or sent over a network. 

  import pickle

    # Define a sample dictionary
    data = {'key': 'value', 'hello': 'world'}

    # Serialize the data into a byte stream
    serialized_data = pickle.dumps(data)

    # Alternatively, write the serialized data to a file
    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)


  Unpickling involves converting the byte stream back into a Python object.

  import pickle

  # Assuming we have a file containing pickled data from the previous example
  with open('data.pkl', 'rb') as file:
      data = pickle.load(file)

  # Now 'data' is a Python dictionary again
  print(data)
-----------------------------------------------

-----------------------------------------------
- What is GIL?
  Global Interpreter Lock
  The GIL ensures that only one thread can execute Python bytecode at a time.
  It is like a hurdle as it doesn't allow multi-threading in python.

  Although the GIL allows multiple threads to be created in a Python program, 
  it limits concurrent execution of Python bytecode, 
  which means Python threads might not effectively utilize multiple CPU cores.
  So, Instead of using threads, using multiple processes can bypass the GIL.

  Each Python process gets its own Python interpreter and memory space 
  so the GIL won't be a bottleneck.
-----------------------------------------------

-----------------------------------------------
- What is monkey patching in Python?
  it is a practice of modifying or extending modules, 
  classes, or methods at runtime, 
  typically after they have already been imported or defined. 
  This technique allows for changing the behavior of a piece of code without altering 
  the original source code directly. 
-----------------------------------------------

-----------------------------------------------
- Difference between append and extend?
  append - adds element at the end
  extend - adds all elements from an iterable to the end of the list.
-----------------------------------------------

-----------------------------------------------
- Built-in data types Properties in Python
  1. List
     1. Mutable: Lists can be modified, which means you can add, remove, or change items after the list creation.
     2. Ordered: Lists maintain the order of elements in which they were inserted.
     3. Indexable: Each element in a list can be accessed using an index. Python lists are zero-indexed.
     4. Allows Duplicates: Lists can have multiple identical entries; i.e., they can contain the same value more than once.
     5. Dynamic Size: Lists can grow or shrink dynamically as items are added or removed.

  2. Tuples
     1. Immutable: Once a tuple is created, it cannot be modified. No additions, deletions, or changes.
     2. Ordered: Tuples maintain the order of elements in which they were inserted.
     3. Indexable: Elements can be accessed via indices, similar to lists.
     4. Allows Duplicates: Tuples can contain the same value more than once.
     5. Used for Fixed Data: Ideal for storing collections of items that should not change throughout the program's life.

  3. Dictionary
     1. Mutable: You can change, add, and remove items after the dictionary has been created.
     2. Unordered (until Python 3.7), Ordered (Python 3.7 and later): 
        Earlier versions did not maintain any order, but as of Python 3.7, dictionaries remember the insertion order.
     3. Key-Value Pairs: Data in dictionaries are stored and fetched by keys, not by index.
     4. Keys Must Be Unique: Each key must be unique, although values may be duplicated.
     5. Dynamic Size: Can grow and shrink as needed.

  4. Sets
     1. Mutable: You can add and remove elements from the set.
     2. Unordered: Sets do not record element position or order of insertion and 
        therefore cannot be indexed.
     3. No Duplicates: Sets automatically remove any duplicate entries.
     4. Sets are not Indexed
     5. Used for Uniqueness Operations: Excellent for membership testing, 
        removing duplicates from a sequence, and computing mathematical operations such as intersection, 
        union, difference, and symmetric difference.
-----------------------------------------------
- what is silicing?
  Slicing in Python is a technique used to access a range of elements 
  from sequences such as lists, tuples, strings, and other iterable objects.
  Slicing allows us to extract a subset of elements from a sequence.
  The syntax for slicing is:
      sequence[start:stop:step]
-----------------------------------------------
- What is OOPs?
  1. OOPs stand for Object-Oriented Programming system 
  2. It is a programming paradigm(a typical example) that is based on the concept of objects.
  3. With OOPs we can model real-world entities as objects.

  The four core pillars of OOPs are - 
  1. Encapsulation - bundling the methods into a single unit called class.
  2. Abstraction - 
  3. Inheritance - Allowing a new class to inherit the properties from an existing class.
                   Which helps in code reusability and establish hierarchical relationship
                   between classes.
  4. Polymorphism - This provides ability to different classes to be treated as instance
                    of the same class through a common interface.


"""