
## Comprehension

- Example 1 - List comprehension

    - [expr(item) for item in iterable]

```python
>>> sentnc = ['kun', 'jade', 'dabli']
>>> [{ w, len(w)} for w in sentnc]
[{'kun', 3}, {'jade', 4}, {5, 'dabli'}]
>>> [i*i for i in range(5)]
[0, 1, 4, 9, 16]

```

- Example 2 - Set comprehension

    - {expr(item) for item in iterable}

```python
>>> [i%2 for i in range(5)]
[0, 1, 0, 1, 0]
>>> {i%2 for i in range(5)}
{0, 1}

```

- Example 3 - Dictionary comprehension

    - {key_expr:value_expr for item in iterable}

```python
>>> sentnc = ['kun', 'jade', 'dabli']
>>> {w:len(w) for w in sentnc}
{'kun': 3, 'jade': 4, 'dabli': 5}

```

> Note using above we can reverse the mapping of a dictionary

```python
>>> sentnc = ['kun', 'jade', 'dabli']
>>> {w:len(w) for w in sentnc}
{'kun': 3, 'jade': 4, 'dabli': 5}
>>>
>>> nam2len = {w:len(w) for w in sentnc}
>>> {v:k for k, v in nam2len.items()}
{3: 'kun', 4: 'jade', 5: 'dabli'}

```

- Example 4 - Filtering with comprehension

    - [expr(item) for item in iterable if predicate(item)]

```python
>>> [i for i in range(9) if i%2 == 0]
[0, 2, 4, 6, 8]

```

> Note never use comprehension when there is side effect (printing to console), use for loop for such cases

## Iterator protocols

- Example 5 - Iterating

```python
>>> l = [1, 4]
>>> iter = iter(l)
>>> next(iter)
1
>>> next(iter)
4
>>> next(iter)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

## Generators

- Infinite stream of iterator
- Only next value is computed
- Basically are iterators (all generators are iterators)
- Can be plugged to another generator to build a stream of data pipeline
- They are build with the use of yield rather than return, but can have empty return as end marker

- Example 6 - Generators

```python
>>> def simple_gen():
...   yield 1
...   yield 2
...
>>> next(simple_gen())
1
>>> next(simple_gen())
1
>>> next(simple_gen())
1
>>> i = simple_gen()
>>> next(i)
1
>>> next(i)
2
>>> next(i)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> for i in simple_gen():
...   print(i)
...
1
2

```

> NOte every initialization of generator initiates a completely new sequence

```python
>>> i1 = simple_gen()
>>> i2 = simple_gen()
>>> i1 == i2
False
>>> i1 is i2
False
>>> i1
<generator object simple_gen at 0x000001C015AFBDD0>
>>> i2
<generator object simple_gen at 0x000001C015B53AC0>

```

- Example 7 - Anatomy of execution of Generators

```python
>>> def track_gen():
...   print("1")
...   yield 1
...   print("2")
...   yield 2
...   print("end")
...
>>> i = track_gen()
>>> next(i)
1
1
>>> next(i)
2
2
>>> next(i)
end
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

***Challenge - Fibonacci***

```python
>>> def fib():
...   yield 0
...   a = 0
...   b = 1
...   while True:
...     yield b
...     a, b = b, a+b
...
>>> for i in fib():
...   print(i)
...   if i > 10:
...     break
...
0
1
1
2
3
5
8
13
```

- Example 8 - Generator comprehension

```python
>>> sq = ( x*x for x in range(1000) )
>>> sq
<generator object <genexpr> at 0x0000016B377EBDD0>
>>> for s in sq:
...   print(s)
...   if s > 50:
...     break
...
0
1
4
9
16
25
36
49
64
>>> next(sq)
81
```

- Example 9 - Usage Generator comprehension (Sum of 100 integer squares)

```python
>>> sum( x*x for x in range(100) )
328350

```

> This will be extremely resource efficient

## Iterator Function

https://docs.python.org/3/library/itertools.html

- Example 10 - Zip & Chain & all/any

```python
>>> l1 = [ 2, 3, 5 ]
>>> l2 = [ 'san', 'kun', 'jad' ]
>>> for i in zip(l1, l2):
...   print(i)
...
(2, 'san')
(3, 'kun')
(5, 'jad')

>>> from itertools import chain
>>> list(chain(l1, l2))
[2, 3, 5, 'san', 'kun', 'jad']

>>> all([True, False, True])
False
>>> any([True, False, True])
True

```