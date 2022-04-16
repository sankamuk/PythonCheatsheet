
## Implementing a Custom Collection

- Example 01 - Handling collection initiation

```commandline
>>> from my_collection_v01 import MyCollection
>>> l1 = MyCollection([1, 4])
>>> l1 = MyCollection([1, 4, 4])
>>> l1 = MyCollection([])
>>> l1 = MyCollection()
>>> def gn():
...   yield 1
...   yield 4
...   yield 5
...
>>> g = gn()
>>> l1 = MyCollection(g)

```

- Example 02 - Handling container protocol

```commandline
>>> from my_collection_v02 import MyCollection
>>> l1 = MyCollection([1, 4, 4])
>>> 1 in l1
True
>>> 2 in l1
False
```

- Example 03 - Handling size protocol

```commandline
>>> from my_collection_v03 import MyCollection
>>> l1 = MyCollection([1, 4, 4])
>>> len(l1)
2
>>> l1 = MyCollection([])
>>> len(l1)
0
>>> l1 = MyCollection()
>>> len(l1)
0
```

- Example 04 - Handling iterable protocol

```commandline
>>> from my_collection_v04 import MyCollection
>>> l1 = MyCollection([1, 4, 4])
>>> i = iter(l1)
>>> next(i)
1
>>> next(i)
4
>>> next(i)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> for v in l1:
...   print(v)
...
1
4
```

- Example 05 - Handling sequence protocol

```commandline
>>> from my_collection_v05 import MyCollection
>>> l1 = MyCollection([1, 4, 4])
>>> l1[1]
4
>>> l1[-1]
4
>>> l1[0:1]
[1]
>>> l1[0:2]
[1, 4]
```

- Example 06 - Handling equality protocol

```commandline
>>> from my_collection_v05 import MyCollection
>>> MyCollection([1, 4, 4]) == MyCollection([1, 4, 4])
False
>>> MyCollection([1, 4, 4]) is MyCollection([1, 4, 4])
False

>>> from my_collection_v06 import MyCollection
>>> MyCollection([1, 4, 4]) is MyCollection([1, 4, 4])
False
>>> MyCollection([1, 4, 4]) == MyCollection([1, 4, 4])
True
>>> MyCollection([1, 4, 4]) == [1, 4, 4]
False
```

- Example 07 - Handling index and count protocol

```commandline
>>> from my_collection_v07 import MyCollection
>>> l1 = MyCollection([1, 4, 4])
>>> l1.index(4)
1
>>> l1.count(4)
1

```

> Note both above `count` and `index` does not take into consideration, that the structure being sorted and a Set. But you can add good implementation.

- Example 08 - Handling reverse protocol

```commandline
>>> from my_collection_v08 import MyCollection
>>> l1 = MyCollection([1, 4, 2, 99])
>>> list(reversed(l1))
[99, 4, 2, 1]
```

- Example 09 - Handling concatenation/replication protocol


```commandline
>>> from my_collection_v09 import MyCollection
>>> l1 = MyCollection([1, 4, 2, 99])
>>> l2 = MyCollection([19, 22])
>>> list(l1 + l2)
[1, 2, 4, 19, 22, 99]
>>> list(l1  * 2)
[1, 2, 4, 99]
>>> list(3 * l1)
[1, 2, 4, 99]
```

- Example 09 - Handling concatenation/replication protocol

```commandline
>>> from my_collection_v10 import MyCollection
>>> l1 = MyCollection([1, 4, 2, 99])
>>> l2 = MyCollection([1])
>>> l1 < l2
False
>>>
>>> l2 = MyCollection([18])
>>> l1 & l2
set()
>>> l1 | l2
{1, 2, 99, 4, 18}

```

