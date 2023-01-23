
## Install Pytest

```commandline
pip install pytest
```

## Project Structure

There can be many ways of arranging test code but the one i feel is as below:

```
   <Project Home>
        setup.py
        requirement.txt
        <project name>
            → Your application code
        tests
            → Testing code (module and directory should match your application code inder project name)
```

- Example 01 - Sample project

```commandline
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31> tree proj_01 /F
C:\USERS\HP\ONEDRIVE\DESKTOP\WORK\PYTHONCHEATSHEET\TESTING\31\PROJ_01
│   requirement.txt
│   setup.py
│
├───proj_01
│   ├───core
│   │       main.py
│   │
│   └───utils
│       │   utility.py
│
└───tests
    ├───core
    │       test_main.py
    │
    └───utils
            test_utility.py
```

## List test under scope

```commandline
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01> pytest --collect-only
======================================================================================================== test session starts =========================================================================================================
platform win32 -- Python 3.8.8, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01
collected 2 items                                                                                                                                                                                                                     

<Module tests/core/test_main.py>
  <Function test_greet>
<Module tests/utils/test_utility.py>
  <Function test_hello>

===================================================================================================== 2 tests collected in 0.06s =====================================================================================================
```

## Run test

- Success

```commandline
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01> pytest
======================================================================================================== test session starts =========================================================================================================
platform win32 -- Python 3.8.8, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01
collected 2 items                                                                                                                                                                                                                     

tests\core\test_main.py .                                                                                                                                                                                                       [ 50%]
tests\utils\test_utility.py .                                                                                                                                                                                                   [100%]

========================================================================================================= 2 passed in 0.05s ==========================================================================================================
```

> Below is a more verbose option

```commandline
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01> pytest -v
======================================================================================================== test session starts =========================================================================================================
platform win32 -- Python 3.8.8, pytest-7.1.2, pluggy-1.0.0 -- c:\users\hp\python-venv\venv01\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01
collected 2 items                                                                                                                                                                                                                     

tests/core/test_main.py::test_greet PASSED                                                                                                                                                                                      [ 50%]
tests/utils/test_utility.py::test_hello PASSED                                                                                                                                                                                  [100%]

========================================================================================================= 2 passed in 0.03s ==========================================================================================================
```

- Failure

```commandline
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01> pytest -v
======================================================================================================== test session starts =========================================================================================================
platform win32 -- Python 3.8.8, pytest-7.1.2, pluggy-1.0.0 -- c:\users\hp\python-venv\venv01\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01
collected 2 items                                                                                                                                                                                                                     

tests/core/test_main.py::test_greet PASSED                                                                                                                                                                                      [ 50%]
tests/utils/test_utility.py::test_hello FAILED                                                                                                                                                                                  [100%]

============================================================================================================== FAILURES ==============================================================================================================
_____________________________________________________________________________________________________________ test_hello _____________________________________________________________________________________________________________

    def test_hello():
>       assert False
E       assert False

tests\utils\test_utility.py:3: AssertionError
====================================================================================================== short test summary info =======================================================================================================
FAILED tests/utils/test_utility.py::test_hello - assert False
==================================================================================================== 1 failed, 1 passed in 0.11s =====================================================================================================
```

> Note how it details about the failure

## Deep drive asserts

```commandline
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01> pytest .\tests\test_asserts.py
======================================================================================================== test session starts =========================================================================================================
platform win32 -- Python 3.8.8, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01
collected 7 items                                                                                                                                                                                                                     

tests\test_asserts.py F.FFFF.                                                                                                                                                                                                   [100%]

============================================================================================================== FAILURES ==============================================================================================================
__________________________________________________________________________________________________________ test_asserts_01 ___________________________________________________________________________________________________________

    def test_asserts_01():
>       assert 0
E       assert 0

tests\test_asserts.py:3: AssertionError
__________________________________________________________________________________________________________ test_asserts_03 ___________________________________________________________________________________________________________

    def test_asserts_03():
>       assert ""
E       AssertionError: assert ''

tests\test_asserts.py:11: AssertionError
__________________________________________________________________________________________________________ test_asserts_04 ___________________________________________________________________________________________________________

    def test_asserts_04():
>       assert None
E       assert None

tests\test_asserts.py:15: AssertionError
__________________________________________________________________________________________________________ test_asserts_05 ___________________________________________________________________________________________________________

    def test_asserts_05():
>       assert {}
E       assert {}

tests\test_asserts.py:19: AssertionError
__________________________________________________________________________________________________________ test_asserts_06 ___________________________________________________________________________________________________________

    def test_asserts_06():
>       assert []
E       assert []

tests\test_asserts.py:23: AssertionError
====================================================================================================== short test summary info =======================================================================================================
FAILED tests/test_asserts.py::test_asserts_01 - assert 0
FAILED tests/test_asserts.py::test_asserts_03 - AssertionError: assert ''
FAILED tests/test_asserts.py::test_asserts_04 - assert None
FAILED tests/test_asserts.py::test_asserts_05 - assert {}
FAILED tests/test_asserts.py::test_asserts_06 - assert []
==================================================================================================== 5 failed, 2 passed in 0.11s =====================================================================================================
```

> From example above you can see assert is plain old asset from Python but Pytest is working around it.

## Pytest Verbosity

- Increasing v's will increase verbosity.

```commandline
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01> pytest -v .\tests\test_verbosity.py
======================================================================================================== test session starts =========================================================================================================
platform win32 -- Python 3.8.8, pytest-7.1.2, pluggy-1.0.0 -- c:\users\hp\python-venv\venv01\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01
collected 1 item                                                                                                                                                                                                                      

tests/test_verbosity.py::test_verbosity FAILED                                                                                                                                                                                  [100%]

============================================================================================================== FAILURES ==============================================================================================================
___________________________________________________________________________________________________________ test_verbosity ___________________________________________________________________________________________________________

    def test_verbosity():
        command01 = "Hello all how are you. I am fine. How about others. And others. And others!!!!!!"+\
                    "And what a nice day"
        command02 = "Hello all how are you. I am fine. How about others. And others. And others!!!!!!"+\
                    "And, what a nice day"
>       assert command01 == command02
E       AssertionError: assert 'Hello all ho...at a nice day' == 'Hello all ho...at a nice day'
E         - Hello all how are you. I am fine. How about others. And others. And others!!!!!!And, what a nice day
E         ?                                                                                    -
E         + Hello all how are you. I am fine. How about others. And others. And others!!!!!!And what a nice day

tests\test_verbosity.py:7: AssertionError
====================================================================================================== short test summary info =======================================================================================================
FAILED tests/test_verbosity.py::test_verbosity - AssertionError: assert 'Hello all ho...at a nice day' == 'Hello all ho...at a nice day'
========================================================================================================= 1 failed in 0.10s ==========================================================================================================
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01> pytest -vvv .\tests\test_verbosity.py
======================================================================================================== test session starts =========================================================================================================
platform win32 -- Python 3.8.8, pytest-7.1.2, pluggy-1.0.0 -- c:\users\hp\python-venv\venv01\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Testing\31\proj_01
collected 1 item                                                                                                                                                                                                                      

tests/test_verbosity.py::test_verbosity FAILED                                                                                                                                                                                  [100%]

============================================================================================================== FAILURES ==============================================================================================================
___________________________________________________________________________________________________________ test_verbosity ___________________________________________________________________________________________________________

    def test_verbosity():
        command01 = "Hello all how are you. I am fine. How about others. And others. And others!!!!!!"+\
                    "And what a nice day"
        command02 = "Hello all how are you. I am fine. How about others. And others. And others!!!!!!"+\
                    "And, what a nice day"
>       assert command01 == command02
E       AssertionError: assert ('Hello all how are you. I am fine. How about others. And others. And '\n 'others!!!!!!And what a nice day') == ('Hello all how are you. I am fine. How about others. And others. And '\n 'others!!!!!!A
nd, what a nice day')
E         - Hello all how are you. I am fine. How about others. And others. And others!!!!!!And, what a nice day
E         ?                                                                                    -
E         + Hello all how are you. I am fine. How about others. And others. And others!!!!!!And what a nice day

tests\test_verbosity.py:7: AssertionError
====================================================================================================== short test summary info =======================================================================================================
FAILED tests/test_verbosity.py::test_verbosity - AssertionError: assert ('Hello all how are you. I am fine. How about others. And others. And '\n 'others!!!!!!And what a nice day') == ('Hello all how are you. I am fine. How abou...

========================================================================================================= 1 failed in 0.09s ==========================================================================================================
```

