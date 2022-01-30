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

