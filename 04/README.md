
## Object Model

Every literal created, land up being an object in memory. Like the below assignment creates an integer object of value 
1. If we make our variable to be assigned to 2 then another new object will be created with value 2 and x will 
be pointed to it. Now since object(1) is not being pointed to by anyone Python Garbage collector will clean it up 
sooner or later.

```python
x = 1
```

> Below we see identity of the same object return same identity. How Python reuses the object.

```python
>>> id(200)
140728870256656
>>> id(200)
140728870256656

```

> Note below how id function reveals the truth of variable assignment. Also, should be clear Python 
***assign object by name*** not by value.

```python
>>> a = 100
>>> id(a)
140728870253456
>>> b = 100
>>> id(b)
140728870253456
>>> b = 200
>>> id(b)
140728870256656
```

- Example 1 - Reference by Name Model

```python
>>> r = [2, 6]
>>> id(r)
1833489410624
>>> h = r
>>> h.append(4)
>>> id(h)
1833489410624

```

> Thus, we should look at variables as named label to object rather than box of value.


- Example 2 - Immutable and Mutability

We have both mutable and immutable version of object, thus when we create a numeric literal immutable object is created 
while creation of a list is mutable object creation. Immutable can be reused but not mutable version.

```python
>>> l1 = [ 2, 2 ]
>>> id(l1)
1833489411520
>>> l2 = [ 2, 2 ]
>>> id(l2)
1833489414848
>>> i1 = 22
>>> id(i1)
140728870250960
>>> i2 = 22
>>> id(i2)
140728870250960
```

> One critical implication is below, showing value equality and identity equality are different.

```python
>>> i1 is i2
True
>>> i1 == i2
True
>>> l1 is l2
False
>>> l1 == l2
True
```

- Example 3 - Pass by reference

```python
>>> org_lst = [ 2, 4, 99 ]
>>> def f1(l):
...   l.append(22)
...   print(l)
...
>>> org_lst
[2, 4, 99]
>>> f1(org_lst)
[2, 4, 99, 22]
>>> org_lst
[2, 4, 99, 22]

```

> Note the tricky part here, as the name is just a reference below should be clear.

```python
>>> org_lst = [ 2, 4, 99 ]
>>> def f1(l):
...   l = [1]
...   print(l)
...
>>> org_lst
[2, 4, 99]
>>> f1(org_lst)
[1]
>>> org_lst
[2, 4, 99]

>>> def f2(l):
...   return l
...
>>> org_lst = [ 2, 4, 99 ]
>>> id(org_lst)
1833489412736
>>> id(f2(org_lst))
1833489412736

```

## Function arguments

- Example 4 - Functional arguments

```python
>>> def f3(part1, part2):
...   print(part1+ ' ' +part2)
...
>>> f3("sankar", "mukherjee")
sankar mukherjee
>>>
>>> def f4(part1, part2="mukherjee"):
...   print(part1+ ' ' +part2)
...
>>> f4("sankar")
sankar mukherjee
>>>
>>> f4("sankar", "paul")
sankar paul
>>>
>>> f4("sankar", part2="banerjee")
sankar banerjee
>>>
>>> f4(part2="banerjee", part1="sankar")
sankar banerjee
```

> But the below does not work.

```python
>>> f3("sankar")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f3() missing 1 required positional argument: 'part2'
>>> f4(part2="banerjee", "sankar")
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument

```

*** Tricky ***- Example 5 - Default argument as function call or mutable object

```python
>>> def print_now(arg=datetime.now()):
...   print(arg)
...
>>> print_now()
2022-02-06 20:51:05.060590
>>> print_now()
2022-02-06 20:51:05.060590
>>> print_now()
2022-02-06 20:51:05.060590

```

> Note the time never proceeds. As the assignment happened when the function was loaded.

```python
>>> def print_list(l=[]):
...   l.append(1)
...   print(l)
...
>>> print_list()
[1]
>>> print_list()
[1, 1]
>>> print_list()
[1, 1, 1]

```

> Note the list keep growing, as the blank list was assigned at the function load time and every invocation keep 
> referring to the same list.

## Dynamic Strong Types

- Example 6 - Dynamic Type

```python
>>> a = 1
>>> print(a)
1
>>> a = "sankar"
>>> print(a)
sankar

```

- Example 6 - Strong Type (No implicit type conversion ***except for few default case, like boolean)

```python
>>> a = "sankar"
>>> a + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

```

## Python Scopes

- It consists of 'LEGB'
  - L = Local (Inside function)
  - E = Enclosing (Nested function)
  - G = Global (Inside module)
  - B = Buildin Python runtime

> Note there is no scope for code block.

- Example 7 - Global Scope

```python
>>> dir(mod_05)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'func01', 'main', 'sys']
```

- Example 8 - Local scope

  - Function arguments
  - All variables defined inside function


- Example 9 - Rebind scope

```python
PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> cat mod_01.py
"""Scope Demo

Usage:
    python mod_01.py
"""

g = 420


def print_g():
    """Print G"""
    print(g)


def set_lg(inp):
    """Set local G"""
    g = inp


def set_gg(inp):
    """Set global G"""
    global g
    g = inp

PS C:\Users\HP\Desktop\work\PythonCheatsheet\03> python
>>>
>>> from mod_01 import *
>>> print_g()
420
>>> set_lg(22)
>>> print_g()
420
>>> set_gg(22)
>>> print_g()
22
>>>
```

