
## Function Returning Functions

- Example 1 - Returning function

```python
>>> def outer():
...   def inner():
...     print("From inner...")
...   return inner
...
>>> fuc = outer()
>>> fuc()
From inner...
>>>
```

- This ability of treating function as any other object is key feature of Python being a ***Functional Programming*** language where function treated as first class citizen

## Closures

> It is basically the ability of holding on (reference to object) to its enclosing scope (earlier scope) even if one does not exist and not in scope

- Example 2 - Closure usage

```python
>>> def closure_eg():
...   x = "Jade"
...   def greet():
...     print("Hello {}!!!".format(x))
...   return greet
...
>>> g = closure_eg()
>>> g()
Hello Jade!!!
>>> g.__closure__
(<cell at 0x000001D028C30AF0: str object at 0x000001D02931F6B0>,)
```

> The value returned by '__closure__' is the actual earlier reference object held but the function

## Function Factory with Closures

- Example 3 - Using function factory

```python
>>> def power_of(x):
...   def result(y):
...     return pow(y, x)
...   return result
...
>>> sq = power_of(2)
>>> sq(2)
4
>>> sq(4)
16
>>> cb = power_of(3)
>>> cb(2)
8
>>> cb(3)
27
>>> cb.__closure__
(<cell at 0x00000189E48A28E0: int object at 0x00007FFBFC5E2770>,)

```

> Note using closure how result instance preserves the value (i.e. x) from enclosing scope

- Example 4 - Revisiting scopes

```python
>>> val = "global"
>>> def enc_func():
...   val = "enclosing"
...   def loc_func():
...     val = "local"
...     print("loc_func: "+ val)
...   print("enc_func: "+ val)
...   loc_func()
...   print("enc_func: "+ val)
...
>>> print("global: "+ val)
global: global
>>> enc_func()
enc_func: enclosing
loc_func: local
enc_func: enclosing
>>> print("global: "+ val)
global: global
>>>
```

> You should also be clear of how to override the natural scope

```python
>>> val = "global"
>>> def enc_func():
...   val = "enclosing"
...   def loc_func():
...     global val
...     print("local (global): "+ val)
...     val = "local"
...     print("local (global): "+ val)
...   print("enc_func: "+ val)
...   loc_func()
...   print("enc_func: "+ val)
...
>>> print("global: "+ val)
global: global
>>> enc_func()
enc_func: enclosing
local (global): global
local (global): local
enc_func: enclosing
>>> print("global: "+ val)
global: local
```

## Non-Local binding

> Bind names from immediate enclosing namespace into local namespace

```python
>>> val = "global"
>>> def enc_func():
...   val = "enclosing"
...   def loc_func():
...     nonlocal val
...     print("local (non-local): "+ val)
...     val = "local"
...     print("local (non-local): "+ val)
...   print("enc_func: "+ val)
...   loc_func()
...   print("enc_func: "+ val)
...
>>> print("global: "+ val)
global: global
>>> enc_func()
enc_func: enclosing
local (non-local): enclosing
local (non-local): local
enc_func: local
>>> print("global: "+ val)
global: global
```

> Note it will be a SyntaxError if no such name exist in any enclosing namespace when using 'nonlocal'

***Challange*** Shopping Bucket

```python
>>> def shop():
...   b = []
...   def add(i):
...     nonlocal b
...     b.append(i)
...     print(b)
...   return add
...
>>> s1 = shop()
>>> s2 = shop()
>>> s1("apple")
['apple']
>>> s1("orange")
['apple', 'orange']
>>> s2("potato")
['potato']
>>> s2("ginger")
['potato', 'ginger']
>>> s1("banana")
['apple', 'orange', 'banana']
>>> s2("chilli")
['potato', 'ginger', 'chilli']
```

## Decorator

- Allow enhancement of an existing function without modifying the existing function
- Its implemented as a callable which takes a callable and returns a callable

> Below is how a decorated function works in Python

- Python takes the original function and compiles to create a function object (F1)
- Compiles the decorator with the compiled base function object (F1) to create a new function object (F2)
- Binds the name of the base function to F2

```python
>>> def currency_2_value(f):
...   def wrap(*args, **kargs):
...     r = f(*args, **kargs)
...     return int(r[1:])
...   return wrap
...
>>> def print_currency(v):
...   return v
...
>>> print_currency('R10')
'R10'
>>> @currency_2_value
... def print_currency(v):
...   return v
...
>>> print_currency('R10')
10
```

- Example 5 - Decorator class

```python
>>> class CallCounter:
...   def __init__(self, f):
...     self.f = f
...     self.c = 0
...   def __call__(self, *args, **kwargs):
...     self.c = self.c + 1
...     return self.f(*args, **kwargs)
...
>>> @CallCounter
... def greet(nm):
...   print("Hello {}!".format(nm))
...
>>> greet("dabli")
Hello dabli!
>>> greet("alif")
Hello alif!
>>> greet.c
2
```

> Note the '__call__' function which made the class callable
> Note you can use multiple decorators, only point to note is its executed bottom to top

```commandline
@decorator2 <- Handled second
@decorator1 <- Hanlded first
def func(): <- Hanlded last, actual function
```


> Note decorators can also be used as ***class method***

## Issue with Decorators

All Python function have its metadata like below:

```python
>>> def greet(nm):
...   """Simple greeting"""
...   print("Hello {}!".format(nm))
...
>>> greet("sankar")
Hello sankar!
>>> greet.__name__
'greet'
>>> greet.__doc__
'Simple greeting'
>>> help(greet)
Help on function greet in module __main__:

greet(nm)
    Simple greeting


```

Lets now see effect of Decorator

```python
>>> def add_greet(f):
...   def wrap_greet(*args, **kwargs):
...     r = f(*args, **kwargs)
...     return r
...   return wrap_greet
...
>>> @add_greet
... def greet(nm):
...   """Simple Greeting"""
...   return "Hello {}!".format(nm)
...
>>> greet("sankar")
'Hello sankar!'
>>> greet.__name__
'wrap_greet'
>>> greet.__doc__
>>> help(greet)
Help on function wrap_greet in module __main__:

wrap_greet(*args, **kwargs)


```

> OOP's sure not what we wanted

- Example 6 - Solution 1

```python
>>> def add_greet(f):
...   def wrap_greet(*args, **kwargs):
...     return f(*args, **kwargs)
...   wrap_greet.__name__ = f.__name__
...   wrap_greet.__doc__ = f.__doc__
...   return wrap_greet
...
>>> @add_greet
... def greet(nm):
...   """Simple greet"""
...   return "Hello {}!".format(nm)
...
>>> greet('sankar')
'Hello sankar!'
>>> greet.__name__
'greet'
>>> greet.__doc__
'Simple greet'
>>> help(greet)
Help on function greet in module __main__:

greet(*args, **kwargs)
    Simple greet


```

## Functools - A better approach to use Decorator

- Example 6 - Decorator with functools

```python
>>> from functools import wraps
>>> def add_greet(f):
...   @wraps(f)
...   def wrap_greet(*args, **kwargs):
...     return f(*args, **kwargs)
...   return wrap_greet
...
>>> @add_greet
... def greet(nm):
...   """Simple greet"""
...   return "Hello {}!".format(nm)
...
>>> greet("sankar")
'Hello sankar!'
>>> greet.__name__
'greet'
>>> greet.__doc__
'Simple greet'
>>> help(greet)
Help on function greet in module __main__:

greet(nm)
    Simple greet

```

## Decorator with Argument

- Example 8 - A simple argument validator

```python
>>> def check_argument(i):
...   def validator(f):
...     def wrap_func(*args, **kwargs):
...       if args[i] < 0:
...         raise Exception("Invalid argument {0} at index {1}, should be positive number".format(args[i], i))
...       return f(*args, **kwargs)
...     return wrap_func
...   return validator
...
>>> @check_argument(0)
... @check_argument(1)
... def special_operation(a1, a2):
...   print("Addition: {}".format(a1+a2))
...
>>> special_operation(1,3)
Addition: 4
>>> special_operation(1,-3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in wrap_func
  File "<stdin>", line 5, in wrap_func
Exception: Invalid argument -3 at index 1, should be positive number
>>> special_operation(-1,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in wrap_func
Exception: Invalid argument -1 at index 0, should be positive number

```

> Note
> - 'check_argument' is not a decorator, but a simple function which returns a decorator 'validator'.
> - 'wrap_func' is a closure holding on a reference of 'i'

