
## Testing

- ***Testcase***: A collection of test (generally functions)
- ***Fixture***: A peace of code that runs before and/or after tests
- ***Assertion***: Actual test in form of conditional validation of expectation, failure of assertion is failure of test

- Example 01 - An test module

```python
PS C:\Users\HP\Desktop\work\PythonCheatsheet\10> python.exe .\unit_test_eg.py
Setup
Cleanup
.Setup
Cleanup
.Setup
Cleanup
.Setup
Cleanup
.Setup
Cleanup
.
----------------------------------------------------------------------
Ran 5 tests in 0.008s

OK
```

> Validate test module accompany

## Debugging

- Example 2 - Checking out Python Debugger (PDB) nad find help

```python
PS C:\Users\HP\Desktop\work\PythonCheatsheet\10> python
Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32

Warning:
This Python interpreter is in a conda environment, but the environment has
not been activated.  Libraries may fail to load.  To activate this environment
please see https://conda.io/activation

Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import pdb
>>> pdb.set_trace()
--Return--
> <stdin>(1)<module>()->None
(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where

Miscellaneous help topics:
==========================
exec  pdb

(Pdb) help break
b(reak) [ ([filename:]lineno | function) [, condition] ]
        Without argument, list all breaks.

        With a line number argument, set a break at this line in the
        current file.  With a function name, set a break at the first
        executable line of that function.  If a second argument is
        present, it is a string specifying an expression which must
        evaluate to true before the breakpoint is honored.

        The line number may be prefixed with a filename and a colon,
        to specify a breakpoint in another file (probably one that
        hasn't been loaded yet).  The file is searched for on
        sys.path; the .py suffix may be omitted.
(Pdb)
```

- Example 3 - Real Debugging

> Let's test a simple fibonacci number generator function showing error result

```python
PS C:\Users\HP\Desktop\work\PythonCheatsheet\10> python .\simple_debugging.py 4
- 4th Fibonacci number is 1
PS C:\Users\HP\Desktop\work\PythonCheatsheet\10>
```

> Let's start debug in running high level (without digging inside functions)

```
PS C:\Users\HP\Desktop\work\PythonCheatsheet\10> python -m pdb .\simple_debugging.py 4
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(1)<module>()
-> import sys
(Pdb) l
  1  -> import sys
  2
  3
  4     def fibonacci_number(nth):
  5         """Find nth Fibonacci number"""
  6         a, b, c = 0, 1, 1
  7         if nth == 0:
  8             return a
  9         elif nth == 1:
 10             return b
 11         else:
(Pdb) w
  c:\programdata\anaconda3\lib\bdb.py(580)run()
-> exec(cmd, globals, locals)
  <string>(1)<module>()
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(1)<module>()
-> import sys
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(4)<module>()
-> def fibonacci_number(nth):
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(17)<module>()
-> if __name__ == '__main__':
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(18)<module>()
-> print("- {}th Fibonacci number is {}".format(sys.argv[1],
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(19)<module>()
-> fibonacci_number(sys.argv[1])))
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(18)<module>()
-> print("- {}th Fibonacci number is {}".format(sys.argv[1],
(Pdb) n
- 4th Fibonacci number is 1
--Return--
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(18)<module>()->None
-> print("- {}th Fibonacci number is {}".format(sys.argv[1],
(Pdb) n
--Return--
> <string>(1)<module>()->None
(Pdb) n
The program finished and will be restarted
```

> Note l list code line executed, w specifies detail of the module executed n for just next line in same level, note another point while module load function body not parsed


> Let's move inside function

```
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(1)<module>()
-> import sys
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(4)<module>()
-> def fibonacci_number(nth):
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(17)<module>()
-> if __name__ == '__main__':
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(18)<module>()
-> print("- {}th Fibonacci number is {}".format(sys.argv[1],
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(19)<module>()
-> fibonacci_number(sys.argv[1])))
(Pdb) s
--Call--
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(4)fibonacci_number()
-> def fibonacci_number(nth):
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(6)fibonacci_number()
-> a, b, c = 0, 1, 1
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(7)fibonacci_number()
-> if nth == 0:
(Pdb) display a, b, c, nth
display a, b, c, nth: (0, 1, 1, '4')
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(9)fibonacci_number()
-> elif nth == 1:
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(12)fibonacci_number()
-> while c == int(nth):
(Pdb) n
> c:\users\hp\desktop\work\pythoncheatsheet\10\simple_debugging.py(14)fibonacci_number()
-> return b
(Pdb) display a, b, c, nth
display a, b, c, nth: (0, 1, 1, '4')
(Pdb)
```

> Clear that we are not moving inside the while loop when we should have so condition is bad, should have been '<'
> Note the use of display to print names in context
> Also we could have put below code in front of any line where we want to set break point

```python
import pdb; pdb.set_trace()
```


## Virtual Environment

- Example 4 - Creating, entering and exiting virtual environment

```
C:\Users\HP\Desktop
λ python -m venv venv

C:\Users\HP\Desktop
λ .\venv\Scripts\activate.bat

C:\Users\HP\Desktop
(venv) λ python -c "import sys; print(sys.version)"
3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]

C:\Users\HP\Desktop
(venv) λ .\venv\Scripts\deactivate.bat
C:\Users\HP\Desktop
λ rmdir venv\
The directory is not empty.

C:\Users\HP\Desktop
λ rmdir /s venv\
venv\, Are you sure (Y/N)? Y

C:\Users\HP\Desktop
```

## Packaging projects

- Example 5 - Module installation

    - Steps:
      - Create module and setup script
      - Create virtual environment to test import
      - Install module
      - Validate import works

```
C:\Cmder
λ cd ..\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci\

C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
λ python -m venv fibonacci_env

C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
λ .\fibonacci_env\Scripts\activate.bat

C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
(fibonacci_env) λ python setup.py install
running install
running build
running build_py
creating build
creating build\lib
copying fibonacci.py -> build\lib
running install_lib
copying build\lib\fibonacci.py -> C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci\fibonacci_env\Lib\site-packages
byte-compiling C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci\fibonacci_env\Lib\site-packages\fibonacci.py to fibonacci.cpython-38.pyc
running install_egg_info
Writing C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci\fibonacci_env\Lib\site-packages\Fibonacci-0.1_SNAPSHOT-py3.8.egg-info

C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
(fibonacci_env) λ python -c "import fibonacci; fibonacci.__file__"

C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
(fibonacci_env) λ python -c "import fibonacci; print(fibonacci.__file__)"
C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci\fibonacci.py

C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
(fibonacci_env) λ .\fibonacci_env\Scripts\deactivate.bat
C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
λ
C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
```

> Lets check setup script

```
PS C:\Users\HP\Desktop\work\PythonCheatsheet\10> cat .\fibonacci\setup.py
from distutils.core import setup

setup(
    name="Fibonacci",
    description="Fibonacci Number Generator",
    version="0.1-SNAPSHOT",
    author="Sankar Mukherjee",
    author_email="my_email@something.com",
    license="Apache License 2.0",
    py_modules=["fibonacci"],
    keywords="fibonacci"
)
```

- Example 6 - Module distribution

```
C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
λ dir
 Volume in drive C is OS-SSD
 Volume Serial Number is 747F-67DE

 Directory of C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci

25-02-2022  13:09    <DIR>          .
25-02-2022  13:09    <DIR>          ..
25-02-2022  11:57               449 fibonacci.py
25-02-2022  12:56               314 setup.py
               2 File(s)            763 bytes
               2 Dir(s)  16,627,822,592 bytes free

C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
λ python setup.py sdist --format zip
running sdist
running check
warning: check: missing required meta-data: url

warning: sdist: manifest template 'MANIFEST.in' does not exist (using default file list)

warning: sdist: standard file not found: should have one of README, README.txt, README.rst

writing manifest file 'MANIFEST'
creating Fibonacci-0.1-SNAPSHOT
making hard links in Fibonacci-0.1-SNAPSHOT...
hard linking fibonacci.py -> Fibonacci-0.1-SNAPSHOT
hard linking setup.py -> Fibonacci-0.1-SNAPSHOT
creating dist
creating 'dist\Fibonacci-0.1-SNAPSHOT.zip' and adding 'Fibonacci-0.1-SNAPSHOT' to it
adding 'Fibonacci-0.1-SNAPSHOT'
adding 'Fibonacci-0.1-SNAPSHOT\fibonacci.py'
adding 'Fibonacci-0.1-SNAPSHOT\PKG-INFO'
adding 'Fibonacci-0.1-SNAPSHOT\setup.py'
removing 'Fibonacci-0.1-SNAPSHOT' (and everything under it)

C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
λ dir
 Volume in drive C is OS-SSD
 Volume Serial Number is 747F-67DE

 Directory of C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci

25-02-2022  13:10    <DIR>          .
25-02-2022  13:10    <DIR>          ..
25-02-2022  13:10    <DIR>          dist
25-02-2022  11:57               449 fibonacci.py
25-02-2022  13:10                68 MANIFEST
25-02-2022  12:56               314 setup.py
               3 File(s)            831 bytes
               3 Dir(s)  16,631,136,256 bytes free

C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
λ dir dist\
 Volume in drive C is OS-SSD
 Volume Serial Number is 747F-67DE

 Directory of C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci\dist

25-02-2022  13:10    <DIR>          .
25-02-2022  13:10    <DIR>          ..
25-02-2022  13:10             1,174 Fibonacci-0.1-SNAPSHOT.zip
               1 File(s)          1,174 bytes
               2 Dir(s)  16,631,132,160 bytes free

C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
λ  tar -tvf .\Fibonacci-0.1-SNAPSHOT.zip
drwxrwxr-x  0 0      0           0 Feb 25 13:10 Fibonacci-0.1-SNAPSHOT/
-rw-rw-r--  0 0      0         449 Feb 25 11:57 Fibonacci-0.1-SNAPSHOT/fibonacci.py
-rw-rw-r--  0 0      0         275 Feb 25 13:10 Fibonacci-0.1-SNAPSHOT/PKG-INFO
-rw-rw-r--  0 0      0         314 Feb 25 12:56 Fibonacci-0.1-SNAPSHOT/setup.py
C:\Users\HP\Desktop\work\PythonCheatsheet\10\fibonacci (10)
```

## Third Party Package Installation

- Example 7 - PIP

```
λ cd ..\Users\HP\Desktop\work\PythonCheatsheet\10\

C:\Users\HP\Desktop\work\PythonCheatsheet\10 (10)
λ python -m venv my_venv

C:\Users\HP\Desktop\work\PythonCheatsheet\10 (10)
λ .\my_venv\Scripts\activate.bat

C:\Users\HP\Desktop\work\PythonCheatsheet\10 (10)
(my_venv) λ pip freeze

C:\Users\HP\Desktop\work\PythonCheatsheet\10 (10)
(my_venv) λ pip install nose
Collecting nose
  Downloading nose-1.3.7-py3-none-any.whl (154 kB)
     |████████████████████████████████| 154 kB 1.3 MB/s
Installing collected packages: nose
Successfully installed nose-1.3.7
WARNING: You are using pip version 20.2.3; however, version 22.0.3 is available.
You should consider upgrading via the 'c:\users\hp\desktop\work\pythoncheatsheet\10\my_venv\scripts\python.exe -m pip install --upgrade pip' command.

C:\Users\HP\Desktop\work\PythonCheatsheet\10 (10)
(my_venv) λ pip freeze
nose==1.3.7

C:\Users\HP\Desktop\work\PythonCheatsheet\10 (10)
(my_venv) λ pip uninstall nose
Found existing installation: nose 1.3.7
Uninstalling nose-1.3.7:
  Would remove:
    c:\users\hp\desktop\work\pythoncheatsheet\10\my_venv\lib\site-packages\nose-1.3.7.dist-info\*
    c:\users\hp\desktop\work\pythoncheatsheet\10\my_venv\lib\site-packages\nose\*
    c:\users\hp\desktop\work\pythoncheatsheet\10\my_venv\man\man1\nosetests.1
    c:\users\hp\desktop\work\pythoncheatsheet\10\my_venv\scripts\nosetests-3.4.exe
    c:\users\hp\desktop\work\pythoncheatsheet\10\my_venv\scripts\nosetests.exe
Proceed (y/n)? y
  Successfully uninstalled nose-1.3.7

C:\Users\HP\Desktop\work\PythonCheatsheet\10 (10)
(my_venv) λ pip freeze

C:\Users\HP\Desktop\work\PythonCheatsheet\10 (10)
(my_venv) λ .\my_venv\Scripts\deactivate.bat
C:\Users\HP\Desktop\work\PythonCheatsheet\10 (10)
λ rmdir /s my_venv\
my_venv\, Are you sure (Y/N)? Y
```