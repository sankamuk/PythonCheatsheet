
## Exception

- You should be always as specific as possible when handling exception. Else it will lead to new issues in the future.
- You can handle Exception or any derived type from one specified in except clause.
- If you do not remember exception hierarchy use mro() method to identify inheritance chain.
- Full hierarchy [LINK](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
- When processing exception as an object `args` attribute will give the detail of the error. But better use casting to string `str()` instead.
- You can define your new exception type, always inherit Exception and leave all default implementation. Next you can throw with raise and catch by except.
- Remember when inheriting you can override the initialization but never forget to pass message to super class Exception, also do update `__str__` and `__repr__` else makes no sense.
- While handling one exception you get another exception Python is smart enough and reports the details. You can access this with context.

- Example 1 - Exceptions

```commandline
>>> IndexError.mro()
[<class 'IndexError'>, <class 'LookupError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]

>>> try:
...   l1 = [1, 4]
...   print(l1[5])
... except IndexError as e:
...   print("Error: {}".format(e.args))
...   print("Error: {}".format(str(e)))
...
Error: ('list index out of range',)
Error: list index out of range

>>> class MyNewException(Exception):
...   pass
...
>>> MyNewException.mro()
[<class '__main__.MyNewException'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]

>>> class MyNewException(Exception):
...   def __init__(self, mssg, add_argument):
...     super().__init__(mssg)
...     self._add_args = add_argument
...
>>> e = MyNewException("Any error", 3)
>>> e.args
('Any error',)
>>> str(e)
'Any error'


>>> try:
...   l[3]
... except:
...   raise ValueError("Bad value in index")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
ValueError: Bad value in index

>>> try:
...   l[23]
... except Exception as e:
...   try:
...     raise ValueError("New error")
...   except Exception as f:
...     print(str(f))
...     print(f.__context__)
...
New error
list index out of range

```

## Assertion

- Allow you to assert, format `assert <CONDITION>[, MESSAGE]`
- Good use is to document as they are inexpensive and provide pointers for users
- In case you don't want the assertion to be in place, you can disable with python option `-O`
- Assertion are large targeted to the implementor not user.

```commandline
>>> assert False, "Sample Assertion Failure"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Sample Assertion Failure
>>> assert True, "Sample Assertion Failure"

```