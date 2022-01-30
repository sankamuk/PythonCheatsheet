
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

- Example 6 - Library Import

Python comes with a set of library already included with its distribution, this is called Standard Library. If you want 
to use it just import and start using it class and functions.

```python
>>> import math
>>> math.floor(3.2)
3

```

If you want to explore all the functions available in your imported module you can do 

```python
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs',
'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radia
ns', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

```

In case you want to get some detail about the functions, you do as below:

```python
>>> help(math)
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

```

> Note the help page will be displayed page wise, to move to next page type '<space>' and to exit type 'q'.

You can also dig deep in help.

```python
>>> help(math.floor)
Help on built-in function floor in module math:

floor(x, /)
    Return the floor of x as an Integral.

    This is the largest integer <= x.
```

- Example 7 - Import specific item from module

```python
>>> from math import floor
>>> floor(3.5)
3
>>> from math import floor as f
>>> f(3.5)
3

```

## Python Data Types

### Integer (int)

They are signed and ***unlimited precision*** 

- Example 8 - Integer representation in different format (Decimal, Binary, Octal, Hex-Decimal, String, Float)

```python
>>> 10
10
>>> 0b1010
10
>>> 0o12
10
>>> 0xA
10
>>> int('10')
10
>>> int(10.0)
10

```

### Floating point (float)

53 bit of binary precision and 15-16 bit of decimal precision

- Example 9 - Float representation

```python
>>> 3.5
3.5
>>> 4e3
4000.0
>>> float('1.2')
1.2
>>> float(1)
1.0

```

### Special Numerical Type

- Example 10 - Not a number (NaN), used to represent undefined value required to be numeric

```python
>>> math.isnan(float('nan'))
True
>>> math.isnan(float('1.0'))
False

```
- Example 11 - Infinity

```python
>>> math.isfinite(float('-inf'))
False
>>> math.isfinite(float('inf'))
False
>>> math.isfinite(float('100.0'))
True

```
> Note we have both positive and negative infinity separately


- Example 12 - No value None

```python
>>> None
>>>
>>> a = 1
>>> a is None
False
>>> a is not None
True

```

### Boolean Type (bool)

- Example 13 - Different representation

```python
>>> True
True
>>> False
False
>>> bool(0)
False
>>> bool(1)
True
>>> bool(-1)
True
>>> bool(0.0)
False
>>> bool(0.11)
True
>>> bool(-4.11)
True
>>> bool([])
False
>>> bool([1])
True
>>> bool("")
False
>>> bool("anything")
True
```

> Note bool cannot convert string to boolean

- Example 14

```python
>>> bool('False')
True

```

## Relational Operator

- Example 15 - Relational 

```python
>>> 1 == 1
True
>>> 1 < 1
False
>>> 1 <= 1
True
>>> 1 > 1
False
>>> 1 >= 1
True
>>> False != bool('Flase')
True

```

## Conditional Statement

Allows branching flow of execution. If statement only take boolean, so everything will be converted to one.

```python
>>> if True:
...   print('True')
...
True
>>> if False:
...   print('True')
...
>>>
>>> if False:
...   print('True')
... else:
...   print('False')
...
False
>>>
>>> a = 55
>>> if a > 100:
...   print('Greater than 100')
... elif a > 50:
...   print('Less than 100 but greater 50')
... else:
...   print('Less than 50')
...
Less than 100 but greater 50
```

## Iterations

Allows a block to be iterated, also called lopped. While is the operator which takes boolean to figure out whether to 
keep iterating.

```python
>>> c = 1
>>> while c < 5:
...   print("looping...")
...   c = c + 1
...
looping...
looping...
looping...
looping...
>>>

>>> c = 1
>>> while c < 5:
...   print("looping...")
...   c += 1
...
looping...
looping...
looping...
looping...
```

> Note the use of special operator '+=' signifies + and then assign result.

### Challenge

- Example - Implementing a REPL

```python
>>> while True:
...   n = input('Type a name(ENTER to exit):')
...   if n:
...     print("hello {}!".format(n))
...   else:
...     print('Good bye!')
...     break
...
Type a name(ENTER to exit):sankar
hello sankar!
Type a name(ENTER to exit):jewel
hello jewel!
Type a name(ENTER to exit):
Good bye!
>>>
```
