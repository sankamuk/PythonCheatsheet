## Functions

Block of code with one or more input and a single or none output.

- Example 1 - Function usage

```python
>>> def func01(x):
...   print("hello {}".format(x))
...
>>> func01('sankar')
hello sankar
>>> v01 = func01('sankar')
hello sankar
>>> v01
>>>

>>> def returnfunc(x):
...   return "hello {}".format(x)
...
>>> returnfunc("sankar")
'hello sankar'
>>> v02 = returnfunc("sankar")
>>> v02
'hello sankar'

```

## Modules

It's a self-contained group of names functions or class or even variables. This can import as a whole and each names 
component can be invoked and used. Simply put module is a file executable by Python interpreter and adds callable 
components in current constructs which can be invoked when required.

- Example 2 - Module usage

```python
PS C:\Users\HP\Desktop\work\PythonCheatsheet> cat .\03\mod_01.py

def func01(x):
    print("hello {}".format(x))


def returnfunc(x):
    return "hello {}".format(x)

PS C:\Users\HP\Desktop\work\PythonCheatsheet> python .\03\mod_01.py
PS C:\Users\HP\Desktop\work\PythonCheatsheet>

>>> import mod_01
>>> mod_01.func01('sankar')
hello sankar
>>> from mod_01 import func01
>>> func01('sankar')
hello sankar

```

> Note when we import module it just imports the function in context but does nothing. But we can import it module in 
> Python programme and use the imported components.

- Example 03 - Runnable module

```python
PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> cat mod_02.py

def func01(x):
    print("hello {}".format(x))


print(__name__)
PS C:\Users\HP\Desktop\work\PythonCheatsheet\03>

PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> python mod_02.py
__main__
PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> python
>>> import mod_02
mod_02

```

> Note how the ***special variable*** ```__name__``` behaves differently based on how the same is invoked. 
> We use this to make module executable.

```python
PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> cat mod_02.py

def func01(x):
    print("hello {}".format(x))


if __name__ == '__main__':
    func01('sankar')
PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> python .\mod_02.py
hello sankar
PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> python
>>> import mod_02
>>> mod_02.func01('sankar')
hello sankar

```

> Note when we import a module the compiler only runs the definition (i.e. def's)

***RECOMENDATION*** Always make modules import-able by functionality in its function and using `___main___` check. 
Allowing it to be easily sharable and testable.


- Example 04 - Final recommended module design

```python
PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> cat mod_03.py
import sys


def func01(x):
    print("hello {}".format(x))


def main(arg):
    func01(arg)


if __name__ == '__main__':
    main(sys.argv[1])
PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> python mod_03.py 'sankar'
hello sankar
PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> python
Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32

Warning:
This Python interpreter is in a conda environment, but the environment has
not been activated.  Libraries may fail to load.  To activate this environment
please see https://conda.io/activation

Type "help", "copyright", "credits" or "license" for more information.
>>> from mod_03 import (main, func01)
>>> func01('sankar')
hello sankar
>>> main('sankar')
hello sankar
>>>

```

## Documentation & Comments

Document pattern can be different style, but below we list two most widely used format.

- Example 05 - Documentation pattern

```python
PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> cat mod_04.py
"""
Hello World Module

Usage:
    python mod_04.py <String To Greet>
"""
import sys


def func01(x):
    """Hello Method."""
    print("hello {}".format(x))


def main(arg):
    """
    Main function
    :param arg: String
    :return: Return from function call func01
    """
    func01(arg)


if __name__ == '__main__':
    main(sys.argv[1])
```

> Using documentation for help

```python
>>> import mod_04
>>> help(mod_04.main)
Help on function main in module mod_04:

main(arg)
    Main function
    :param arg: String
    :return: Return from function call func01

>>> help(mod_04.func01)
Help on function func01 in module mod_04:

func01(x)
    Hello Method.

>>>
```

> Module Documentation

```python
>>> import mod_04
>>> help(mod_04)
Help on module mod_04:

NAME
    mod_04 - Hello World Module

DESCRIPTION
    Usage:
        python mod_04.py <String To Greet>

FUNCTIONS
    func01(x)
        Hello Method.

    main(arg)
        Main function
        :param arg: String
        :return: Return from function call func01

FILE
    c:\users\hp\desktop\work\pythoncheatsheet\03\mod_04.py


```

- Example 06 - Commenting code

```python
PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> cat mod_05.py

...

# Start
if __name__ == '__main__':
    main(sys.argv[1])  # Calling main function

```

- Example 07 - She-bang (Unix Only)

```python
PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> cat mod_06.py
#!/usr/bin/env python3
"""
Hello World Module

Usage:
    python mod_04.py <String To Greet>
"""

...
```

> The only purpose is to identify the target for your code
