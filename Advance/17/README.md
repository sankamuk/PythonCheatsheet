
## Understanding Comprehensions

- Example 01 - Nested comprehension

```commandline
>>> [ (x, y) for x in range(2) for y in range(2) ]
[(0, 0), (0, 1), (1, 0), (1, 1)]

>>> [ (x, y) for x in range(4) if x > 2 for y in range(2) ]
[(3, 0), (3, 1)]

>>> [ (x, y) for x in range(4) if x <= 2 for y in range(2) if y == x ]
[(0, 0), (1, 1)]

>>> [ (x, y) for x in range(3) for y in range(x) ]
[(1, 0), (2, 0), (2, 1)]

>>> [[ y for y in range(x) ] for x in range(3)]
[[], [0], [0, 1]]

```

> Note from output you can understand its equivalent to a nested for loop

## Functional Style of Programming

- Example 02 - `map` function

```commandline
>>> def double_it(x):
...   return x * 2
...
>>> map(double_it, [3, 65, 28])
<map object at 0x0000017442C7BB80>
>>> list(map(double_it, [3, 65, 28]))
[6, 130, 56]

>>> list(map(lambda x: '_' if x > 'k' else x, "sankar"))
['_', 'a', '_', 'k', 'a', '_']

>>> list(map(lambda x, y: x+y, [1, 5, 7], [3, 98, 2]))
[4, 103, 9]

>>> list(map(lambda x, y: x+y, [1, 5, 7], [3, 2]))
[4, 7]

```

> Note the map function return map object because it is lazy evaluation (***Python 3***)
> You need to provide as many input sequence as the functions needs argument, if not then the output number will be length of the smallest sequent thus allowing even infinite sequence to be passed


- Example 03 - `filter` function

```commandline
>>> list(filter( lambda x: x>0, [4, -7, 23, -6]))
[4, 23]

>>> list(filter(None, [0, False, "", "jh", 56, True]))
['jh', 56, True]

```

> Note if `None` is passed as first element of filter function then it will allow non-false element to pass through

- Example 04 - `reduce` function

```commandline
>>> import operator
>>> import functools
>>> functools.reduce(lambda x,y: x+y, [3, 65, 28])
96
>>> functools.reduce(operator.add, [3, 65, 28])
96

>>> functools.reduce(operator.add, [])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: reduce() of empty sequence with no initial value
>>> functools.reduce(operator.add, [], 0)
0
>>> functools.reduce(operator.add, [1], 0)
1
>>> functools.reduce(operator.add, [3, 65, 28], 10)
106

>>> functools.reduce(operator.mul, [1, 2, 3], 0)
0
>>> functools.reduce(operator.mul, [1, 2, 3], 1)
6

```

> Note if you call reduce with list without element it will throw error also with 1 element it will pass the element
> The third element is the initial value

## Custom Iterator Object

- Example 05 - My custom iterator object

```commandline
>>> from sample_iterable import SampleStructure
>>> l1 = SampleStructure("List 1", [65, 9, 83])
>>> l1
<List:List 1>
>>> next(l1)
65
>>> next(l1)
9
>>> next(l1)
83
>>> next(l1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\HP\Desktop\work\PythonCheatsheet\17\sample_iterable.py", line 13, in __next__
    raise StopIteration()
StopIteration

>>> l2 = SampleStructure("List 1", [65, 9, 83])
>>> for i in l2:
...   print(i)
...
65
9
83
```

> Another alternative to creating iterator with `__iter__` and `__next__` is by implementing `__getitem__` applicable for datastructures supporting integer indexing starting 0

- Example 06 - The `iter` function

> Takes two argument first is a function without argument returning value and second a value that will stop iteration

```commandline
>>> from random import randint
>>> i1 = iter(lambda: randint(1, 2), 2)
>>> next(i1)
1
>>> next(i1)
1
>>> next(i1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```