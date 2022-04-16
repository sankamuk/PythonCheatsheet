
## Context Manager

- Used with `with` statement, `with context-namager: body`
- It helps the context managed object (resource) is properly managed with enter() and exit().

- Example 01 - File handling

```commandline
>>> with open('README.md') as f:
...   f.readlines()
...
['\n', '## Context Manager\n', '\n', '- Used with `with` statement, `with context-namager: body`\n']

```

- Context manager used `__enter__()` method to initialize the object and if returns value assigns to the variable defined by `as`.
- On completion of the with block `__exit__()` is executed, if the blocks throw exception, the exception object is passed to it.

```commandline
>>> from context_manager_01 import *
>>> with LoggingContext() as l:
...   l.info("Hello")
...   l.error("World")
...
Initializing logging context
INFO - Hello
ERROR - World
Cleaning logging context
Exception details: None, None, None

>>> with LoggingContext() as l:
...   l.info("Before error")
...   raise Exception("Issue")
...
Initializing logging context
INFO - Before error
Cleaning logging context
Exception details: <class 'Exception'>, Issue, <traceback object at 0x0000025BB4B4A8C0>
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
Exception: Issue

```

> How error printed twice as with flows the Exception throw and does not handle it
> If you want `__exit__` to ***swallow the Exception you should return True***

```commandline
>>> from context_manager_02 import *
>>> with LoggingContext() as l:
...   l.info("Before error")
...   raise Exception("Issue")
...
Initializing logging context
INFO - Before error
Cleaning logging context
Exception details: <class 'Exception'>, Issue, <traceback object at 0x0000025BB4B4AE00>

```

> Note the contextlib.contextmanager decorator allows converting simple plan functions as context managed object.
> Multiple context manager can be used in same context

```commandline
>>> with LoggingContext() as l1, LoggingContext() as l2:
...   l1.info("something")
...   l2.info("another thing")
...
Initializing logging context
Initializing logging context
INFO - something
INFO - another thing
Cleaning logging context
Exception details: None, None, None
Cleaning logging context
Exception details: None, None, None

```
