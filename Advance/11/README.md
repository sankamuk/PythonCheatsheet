
## Packages

Pythons basic unit of application software is Module (basically a file), while if the application consists of multiple modules we call it Package (directory).
Package is a Module consisting of sub Modules.

```
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> dir


    Directory: C:\Users\HP\Desktop\work\PythonCheatsheet\11


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        25-02-2022     17:35                fibonacci_mod
d-----        25-02-2022     17:31                __pycache__
-a----        25-02-2022     11:57            449 fibonacci.py
-a----        25-02-2022     17:29            227 README.md


PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> dir fibonacci_mod


    Directory: C:\Users\HP\Desktop\work\PythonCheatsheet\11\fibonacci_mod


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        25-02-2022     17:34                __pycache__
-a----        25-02-2022     11:57            449 fibonacci_mod_mod.py


PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> python
Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32

Warning:
This Python interpreter is in a conda environment, but the environment has
not been activated.  Libraries may fail to load.  To activate this environment
please see https://conda.io/activation

Type "help", "copyright", "credits" or "license" for more information.
>>> import fibonacci
>>> print(fibonacci.fibonacci_number(3))
1
>>> type(fibonacci)
<class 'module'>
>>> fibonacci.__path__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'fibonacci' has no attribute '__path__'
>>> fibonacci.__file__
'C:\\Users\\HP\\Desktop\\work\\PythonCheatsheet\\11\\fibonacci.py'
>>>
>>> import fibonacci_mod
>>> import fibonacci_mod.fibonacci_mod_mod
>>> type(fibonacci_mod)
<class 'module'>
>>> type(fibonacci_mod.fibonacci_mod_mod)
<class 'module'>
>>> fibonacci_mod.__path__
_NamespacePath(['C:\\Users\\HP\\Desktop\\work\\PythonCheatsheet\\11\\fibonacci_mod'])
>>> fibonacci_mod.__file__
>>> fibonacci_mod.fibonacci_mod_mod.__file__
'C:\\Users\\HP\\Desktop\\work\\PythonCheatsheet\\11\\fibonacci_mod\\fibonacci_mod_mod.py'
>>> fibonacci_mod.fibonacci_mod_mod.__path__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'fibonacci_mod.fibonacci_mod_mod' has no attribute '__path__'
>>> print(fibonacci_mod.fibonacci_mod_mod.fibonacci_number(3))
1
```

## Module discovery

- 'sys.path' is a list fo directory where Python searches for modules. The search occurs from left to right in the list.

```python
>>> import sys
>>> sys.path
['', 'C:\\Users\\HP\\Desktop\\work\\PythonCheatsheet\\venv\\Scripts\\python38.zip', 'C:\\ProgramData\\Anaconda3\\DLLs', 'C:\\ProgramData\\Anaconda3\\lib', 'C:\\ProgramData\\Anaconda3', 'C:\\Users\\HP\\Desktop\\work\\PythonCheatsheet\\v
env', 'C:\\Users\\HP\\Desktop\\work\\PythonCheatsheet\\venv\\lib\\site-packages']

```

> Note the first element of sys.path is by default set to '', i.e. current directory

- Example 2 - Appending to SYS.PATH

```python
>>> import sys
>>> sys.path
['', 'C:\\Users\\HP\\Desktop\\work\\PythonCheatsheet\\venv\\Scripts\\python38.zip', 'C:\\ProgramData\\Anaconda3\\DLLs', 'C:\\ProgramData\\Anaconda3\\lib', 'C:\\ProgramData\\Anaconda3', 'C:\\Users\\HP\\Desktop\\work\\PythonCheatsheet\\v
env', 'C:\\Users\\HP\\Desktop\\work\\PythonCheatsheet\\venv\\lib\\site-packages']
>>> import fibonacci_mod_mod
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'fibonacci_mod_mod'
>>> sys.path.append('fibonacci_mod')
>>> import fibonacci_mod_mod

```

- Example 3 - Alternate to SYS.PATH

```
λ set PYTHONPATH=%PYTHONPATH%;fibonacci_mod                                                          
                                                                                                     
C:\Users\HP\Desktop\work\PythonCheatsheet\11 (11 -> origin)                                          
λ python                                                                                             
Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32 
                                                                                                     
Warning:                                                                                             
This Python interpreter is in a conda environment, but the environment has                           
not been activated.  Libraries may fail to load.  To activate this environment                       
please see https://conda.io/activation                                                               
                                                                                                     
Type "help", "copyright", "credits" or "license" for more information.                               
>>> import fibonacci_mod_mod                                                                         
>>>                                                                                                  
>>> import sys
>>> sys.path
['', 'C:\\Users\\HP\\Desktop\\work\\PythonCheatsheet\\11\\%PYTHONPATH%', 'C:\\Users\\HP\\Desktop\\work\\PythonCheatsheet\\11\\fibonacci_mod', 'C:\\ProgramData\\Anaconda3\\python38.zip', 'C:\\ProgramData\\Anaconda3\\DLLs', 'C:\\ProgramData\\Anaconda3\\lib', 'C:\\ProgramData\\Anaconda3', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\locket-0.2.1-py3.8.egg', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32\\lib', 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\Pythonwin']                                                                                                     
```

> Note setting OS Environment 'PYTHONPATH' (with set in Windows and export in *NIX) remember separator according to OS (; for Windows and : for *NIX)

- Example 4 - Module Init

```
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> cat .\fibonacci_mod\__init__.py
print("Module fibonacci_mod imported!")
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> dir .\fibonacci_mod\


    Directory: C:\Users\HP\Desktop\work\PythonCheatsheet\11\fibonacci_mod


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        26-02-2022     21:25                __pycache__
-a----        25-02-2022     11:57            449 fibonacci_mod_mod.py
-a----        26-02-2022     21:27             41 __init__.py


PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> python
Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32

Warning:
This Python interpreter is in a conda environment, but the environment has
not been activated.  Libraries may fail to load.  To activate this environment
please see https://conda.io/activation

Type "help", "copyright", "credits" or "license" for more information.
>>> import fibonacci_mod
Module fibonacci_mod imported!
>>> fibonacci_mod.__file__
'C:\\Users\\HP\\Desktop\\work\\PythonCheatsheet\\11\\fibonacci_mod\\__init__.py'
>>>
```

> One cool usage of Init is shown below

```
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> cat .\fibonacci_mod\__init__.py
from fibonacci_mod.fibonacci_mod_mod import fibonacci_number
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> python
Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32

Warning:
This Python interpreter is in a conda environment, but the environment has
not been activated.  Libraries may fail to load.  To activate this environment
please see https://conda.io/activation

Type "help", "copyright", "credits" or "license" for more information.
>>> import fibonacci_mod
>>> fibonacci_mod.fibonacci_number(3)
1
>>> dir(fibonacci_mod)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'fibonacci_mod_mod', 'fibonacci_number']
>>>
```

- Example 5 - Relative Import

```
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> cat .\fibonacci_mod\__init__.py
from .fibonacci_mod_mod import fibonacci_number
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> python
Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32

Warning:
This Python interpreter is in a conda environment, but the environment has
not been activated.  Libraries may fail to load.  To activate this environment
please see https://conda.io/activation

Type "help", "copyright", "credits" or "license" for more information.
>>> import fibonacci_mod
>>> fibonacci_mod.fibonacci_number(3)
1
>>> dir(fibonacci_mod)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'fibonacci_mod_mod', 'fibonacci_number']
>>> from fibonacci_mod import *
>>> fibonacci_number(3)
1
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'fibonacci_mod_mod': <mo
dule 'fibonacci_mod.fibonacci_mod_mod' from 'C:\\Users\\HP\\Desktop\\work\\PythonCheatsheet\\11\\fibonacci_mod\\fibonacci_mod_mod.py'>, 'fibonacci_number': <function fibonacci_number at 0x00000250CD4D74C0>}
```

> Like '.' you can also use '..' to access higher level directory.

## Namespaces

> Below is our structure

```commandline
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11\namespaces> tree /F
Folder PATH listing for volume OS-SSD
Volume serial number is 747F-67DE
C:.
├───legs2
│   └───mammels
│           human.py
│
└───legs4
    └───mammels
            dogs.py

```

- Example 6 - Using Namespacing

```python
>>> import sys
>>> sys.path.extend(['legs2', 'legs4'])
>>> import mammels.human
>>> import mammels.dogs
>>> mammels.human.__file__
'legs2\\mammels\\human.py'
>>> mammels.dogs.__file__
'legs4\\mammels\\dogs.py'
```

## Executable directory

- Example 7 - Simple directory execution

```commandline
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> cat .\dir_to_execute\__main__.py
print("Directory executes!!!")
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> python dir_to_execute
Directory executes!!!
```

> Note how 'dir_to_execute' automatically added to path

- Example 7 - Zipped archive execution

```commandline
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> python dir_to_execute.zip
Directory executes!!!

```

## An project layout

- Example 8 - Example sample project layout

```commandline
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> tree project /F
Folder PATH listing for volume OS-SSD
Volume serial number is 000000AA 747F:67DE
C:\USERS\HP\DESKTOP\WORK\PYTHONCHEATSHEET\11\PROJECT
│   setup.py
│   __main__.py
│
└───project
    │   project_source.py
    │   __init__.py
    │
    ├───project_utils
    │       utils.py
    │       __init__.py
    │
    └───tests
            test_code.py
            __init__.py

```

## Implementing Singletons

- Example 9 - Sample usage of singleton

```commandline
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11> cd .\singleton_example\
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11\singleton_example> python .\using_global_list.py
sankar
Jade
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11\singleton_example> cat .\global_list.py

_global_list = []


def add_element(e):
    _global_list.append(e)


def list_elements():
    return iter(_global_list)
PS C:\Users\HP\Desktop\work\PythonCheatsheet\11\singleton_example> cat .\using_global_list.py
import global_list

global_list.add_element("sankar")
global_list.add_element("Jade")

for e in global_list.list_elements():
    print(e)
```

> Note since the nodule is loaded only once thus the list is initialized only once

