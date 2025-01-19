"""
- pip stands for - pip install package
    it's a tool that allows us to install and manage libraries and dependencies 
    that aren't distributed as part of the standard library. 
- Just like for other programming language:
    - JavaScript: npm
    - Ruby: gem
    - .net: NuGet

- So, pip doesn't get install with python, but in windows Python installer wizard gives us option to install pip
    but in case of Linux environment: pip comes in a separate package called python3-pip, 
    which you need to install with sudo apt install python3-pip

- we can find pip binaries with
    `where pip` command for windows
    `which pip` command for Linux/MacOS

- In case, if we have multiple python versions, so if we want to install some libraries for other python version
    then we need to specify it: `python3 -m pip` or `python3.12 -m pip` or `python2 -m pip`
    Notice: The `-m` switch tells Python to run a module as an executable of the python interpreter.

- Installing packages in Virtual Environment
    To avoid installing packages directly into your system Python installation, you can use a virtual environment.
    Using pip inside a virtual environment has three main advantages. You can:
    1. makes sure that we are using the right Python version for the project.
    2. makes sure that pip is referring to the correct python version.
    3. Use a specific package version for your project without affecting other projects
    ```
    # to make virtual env
    $ python -m venv venv/  # python uses built-in venv package to create virtual environment
    # to activate it
    $ source venv/bin/activate
    ```

- May face Path not found when running pip
    try running: `pip3 --version`
    above command should give pip version and that pip pointing to which python,
    
    if it gives error like Path is not recognizible or command not found then -
    it is because your system can't find pip in the locations listed in your PATH variable. 
    On Windows, PATH is part of the system variables. 
    On macOS and Linux, PATH is part of the environment variables. 

    We can run command `echo $PATH`
    The output of above command will show a list of locations (directories) on your disk 
    where the operating system looks for executable programs. 
    Depending on your system, locations can be separated by a colon (:) or a semicolon (;).


    Two supported methods can help you install pip again and add it to your PATH:
    1. The ensurepip module
    2. The get-pip.py script

    The `ensurepip` module has been part of the standard library since Python 3.4. 
    It was added to provide a straightforward way for you to reinstall pip 
    if, for example, you skipped it when installing Python or you uninstalled pip at some point. 
    we can run:
    ```
    # we can run this on windows/linux/windows
    $ python -m ensurepip --upgrade

- pip gets the packages from pypi
    These packages are published to the Python Package Index(PyPI)

- we can also chain the packages when installing multiple modules
    `pip install requests pandas`
    so, we can add as many pacakges as we want, 
    
- requirements.txt 
    but when we have many modules to install then requirements.txt comes handy

- `pip list`: to check number of packages installed in the current environment

- `pip show <package-name>`: To get more information about a specific package, you can look at the package's metadata.

- checking package version in python script
    ```
    >>> import requests
    >>> requests.__version__
    "x.y.z"
    >>> requests.__file__
    '.../venv/lib/python3.12/site-packages/requests/__init__.py'

    ```

- Using a Custom Package Index
    By default, pip uses PyPI to look for packages.
    But pip also gives you the option to define a custom package index.
    It is helpful if you want to work with packages that aren't publicly available

    for example, I want to install requests library from some other place, not from pypi
    in that case I would need to give flag `-i` or `--index-url` -> `-i` is just a short hand of --index-url

    `python -m pip install -i https://test.pypi.org/simple/requests`

    If, we want to set -i flag permanently then, we can set in config file of pip
    we can get config file of pip by running:
    `(venv) $ python -m pip config list -vv`  # here, -vv stands for verbose

    pip config file name is: pip.conf

- If package is hosted on github instead of Pypi, then we can run:
    `python -m pip install git+https://github.com/realpython/rptree`
    With the git+https scheme, you can point to a Git repository that contains an installable package.

    or we can do below
    ```
    $ git clone https://github.com/realpython/rptree
    $ cd rptree
    $ python -m venv venv/
    $ source venv/bin/activate
    (venv) $ python -m pip install -e .  # -e is shorthand of --editable, and it is called editable mode.
    ```
    In above, instead of using a package name, you use a dot (.) to point pip to the current directory.

- pip freeze
    so, we already know `pip list` will list out the installed packages with their version name
    now, `pip freeze` will list out all those packages like this
    ```
    dev@ash-MacBook-Air ~ % pip freeze
    agate==1.7.1
    agate-dbf==0.2.2
    agate-excel==0.2.5
    agate-sql==0.5.9
    appnope==0.1.3
    ```

    So, we can use freeze command to generate requirement.txt like this
    `pip freeze > requirements.txt`

    and when going to install modules from that file
    we can run: `python -m pip install -r requirements.txt`

    The -r (short for requirements) flag tells pip install to install all the packages listed in the specified requirements file

- If we want to installl package without installing any dependencies, then we need to use
  this flag: --no-deps
  example: pip install [package_name] --no-deps

- Uninstalling package:
    Notice that when you installed requests, you got pip to install other dependencies too.
    Now, if we want to uninstall the module with the dependencies then this is where the show command in pip comes in handy.

    ```
    (venv) $ python -m pip show requests

    Name: requests
    Version: 2.32.3
    Summary: Python HTTP for Humans.
    Home-page: https://requests.readthedocs.io
    Author: Kenneth Reitz
    Author-email: me@kennethreitz.org
    License: Apache 2.0
    Location: .../python3.12/site-packages
    Requires: certifi, idna, charset-normalizer, urllib3
    Required-by:
    ```
    Notice last two lines has Requires and Required-by
    So, the show command tells you that requests requires certifi, idna, charset-normalizer, and urllib3. 
    You probably want to uninstall those too.

    Now, we can remove with `pip uninstall`
    `(venv) $ python -m pip uninstall certifi`
    or
    `(venv) $ python -m pip uninstall -y charset-normalizer idna requests`
    or
    `(venv) $ python -m pip uninstall -r requirements.txt -y`  # with -y switch, it won't ask again to confirm uninstallation.

- Alternative tools to pip
    these are: conda, poetry, pipenv, uv

"""