
## Command Line Interface (CLI)

- Python CLI is an REPL (Read Eval[alute] Print Loop)
- Example 1

```python

>>> 2 + 1
3

```

- Example 2 - Use variable
```python
>>> val = 32
>>> val
32
>>> _
32
>>> x = _
>>> x
32

```
> Note ***_*** is the most recently evaluated value (only in REPL).

- Example 3 - Print
```python
>>> print('Test')
Test

```

> Note in Python 3 Print is a function call and the invocation should be like a function call.

- Example 4 - Leading indentation
```python
>>> print('test')
test
>>>   print('test')
  File "<stdin>", line 1
    print('test')
    ^
IndentationError: unexpected indent


>>> if 1 == 1:
... print('1 is actually 1')
  File "<stdin>", line 2
    print('1 is actually 1')
    ^
IndentationError: expected an indented block
>>> if 1 == 1:
...  print('1 is actually 1')
...
1 is actually 1

```

> In Python ***leading indentation*** represents the structure of the logic(code blocks) and need to be respected. 
> This way of code block specification forces developer to follow indentation rules and makes code readable.
> Also the standard recommendation is ***4 spaces*** unit of code block indentation and ***not tab***.

- Example 5 - PEP

PEP (Python Enhancement Proposal) is protocol for Python language, and PEP 8 articulates is the guidelines for 
developing with Python. Most important guideline is explained (in a rather cryptic way) in something called the 
***Zen of Python***.

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>>
```

