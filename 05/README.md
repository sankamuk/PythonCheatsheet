
## Collections

### Tuples

Immutable sequence of items.

- Example 1 - Tuples 

```python
>>> t3 = ()
>>> type(t3)
<class 'tuple'>
>>> t4 = 2, 4
>>> type(t4)
<class 'tuple'>

>>> t1 = (1, 'sankar', 3.4)
>>> type(t1)
<class 'tuple'>
>>> t1[0]
1
>>> t1[-1]
3.4
>>> len(t1)
3
>>> 'sankar' in t1
True
>>> 'jade' in t1
False
>>> for i in t1:
...   print(i)
...
1
sankar
3.4
>>> t1 + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "int") to tuple
>>> t1 + (1,)
(1, 'sankar', 3.4, 1)
>>> t1 * 2
(1, 'sankar', 3.4, 1, 'sankar', 3.4)
>>> t2 = ((2, 3.0), ('sankar',))
>>> t2[1][0]
'sankar'
>>> type(tuple([1, 2]))
<class 'tuple'>
>>> type(tuple("sankar"))
<class 'tuple'>
>>> tuple("sankar")
('s', 'a', 'n', 'k', 'a', 'r')

```

> Note (1) is not a tuple as Python parses it as int(1).

- Example 2 - Unpacking

```python
>>> v1, v2 = (1, 33)
>>> v1
1
>>> v2
33

```

> Thus we can use this feature for swapping variable.

```python
>>> a = 1
>>> b = 2
>>> b, a = a, b
>>> a
2
>>> b
1

```

### String

- Example 3 - String

```python
>>> len("Hello")
5
>>> "Hello" + "World"
'HelloWorld'
>>>
>>> "Hello" * 2
'HelloHello'
>>>
>>> " ".join(["hello", "world", "!"])
'hello world !'

>>> " ".join(["hello", "world", "!"]).split(" ")
['hello', 'world', '!']

>>> "name,age".partition(",")
('name', ',', 'age')
>>> n, _, a = "name,age".partition(",")
>>> n
'name'
>>> a
'age'
```

> Note, '_' in Python is a placeholder.

- Example 4 - Formatting and Format Specifier

```python
>>> "My name is {}, i am {} yrs of age".format('kun', 35)
'My name is kun, i am 35 yrs of age'
>>> "My name is {1}, i am {0} yrs of age".format(35, 'xun')
'My name is xun, i am 35 yrs of age'
>>> "My name is {name}".format(name='dabli')
'My name is dabli'
>>> "My name is {name[1]}".format(name=['dabli', 'alif'])
'My name is alif'

>>> "My name is {name:10}".format(name='dabli')
'My name is dabli     '
>>> "My name is {name:10}.".format(name='dabli')
'My name is dabli     .'
>>> "My name is {name:>10}.".format(name='dabli')
'My name is      dabli.'
>>> "My name is {name:^10}.".format(name='dabli')
'My name is   dabli   .'
>>> "My name is {name:.>10}.".format(name='dabli')
'My name is .....dabli.'
>>> "My name is {name:.3}.".format(name='dabli')
'My name is dab.'
>>> "number: {:5d}".format(1)
'number:     1'
>>> '{:6.2f}'.format(3.141592653589793)
'  3.14'
>>> '{:{align}{width}}'.format('test', align='^', width='10')
'   test   '
>>> '{:{dfmt} {tfmt}}'.format(datetime(2001, 2, 3, 4, 5), dfmt='%Y-%m-%d', tfmt='%H:%M')
'2001-02-03 04:05'

```

### Range

- Example 5 - Range

```python
>>> for i in range(3):
...   print(i)
...
0
1
2
>>> list(range(3))
[0, 1, 2]
>>> list(range(3, 9))
[3, 4, 5, 6, 7, 8]
>>> list(range(3, 9, 2))
[3, 5, 7]
```

> Note enumeration semantics.

```python
>>> for k, v in enumerate(list(range(3, 9, 2))):
...   print("key {}, value {}".format(k, v))
...
key 0, value 3
key 1, value 5
key 2, value 7

```

### List Operations

- Example 6 - Slicing

```python
>>> l = [23, 66, 3, 98, 56]
>>> l[2:]
[3, 98, 56]
>>> l[2:-2]
[3]
>>> l[2:3]
[3]
>>> l[:3]
[23, 66, 3]
>>> l[:]
[23, 66, 3, 98, 56]

```

> Note the process to clone a list. ***Shallow Copy***

```python
>>> p = l[:]
>>> p
[23, 66, 3, 98, 56]
>>> p[0] = 11
>>> p
[11, 66, 3, 98, 56]
>>> l
[23, 66, 3, 98, 56]

>>> l
[23, 66, 3, 98, 56]
>>> l1 = l[:]
>>> l1 is l
False
>>> l1 == l
True

```

> Other options for list copy.

```python
>>> l2 = l.copy()
>>> l2
[23, 66, 3, 98, 56]
>>> l3 = list(l)
>>> l3
[23, 66, 3, 98, 56]

```

***Shallow Copy***

Note the shallow copy though not just creating new alias to same array object but still does not handle issue of nested 
object, thus if you have list of list, shallow copy could lead to unexpected surprises in the future.
Note this issue also apply for things like list repetitions with nested list.

```python
>>> l = [ [1,2], [43, 5] ]
>>> nl = l * 3
>>> nl
[[1, 2], [43, 5], [1, 2], [43, 5], [1, 2], [43, 5]]
>>> nl[0][1] = 99
>>> nl
[[1, 99], [43, 5], [1, 99], [43, 5], [1, 99], [43, 5]]

```

- Example 7 - List as sting

```python
>>> str = "hello all in the world"
>>> wd = str.split(" ")
>>> wd
['hello', 'all', 'in', 'the', 'world']
>>> "hello" in wd
True
>>> "worldly" in wd
False
>>> wd.index("all")
1
>>> wd.index("none")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'none' is not in list
>>> wd.count("in")
1
>>> del wd[1]
>>> wd
['hello', 'in', 'the', 'world']
>>> wd.remove("the")
>>> wd
['hello', 'in', 'world']
>>> wd.insert(1, "there")
>>> wd
['hello', 'there', 'in', 'world']
>>> " ".join(wd)
'hello there in world'
>>> wd.extend(["!"])
>>> wd
['hello', 'there', 'in', 'world', '!']
>>> wd += ["!"]
>>> wd
['hello', 'there', 'in', 'world', '!', '!']

```

- Example 7 - List sort and reverse (In place)

```python
>>> l1 = [ 55, 76, 34 ]
>>> l1.reverse()
>>> l1
[34, 76, 55]
>>> l1.sort()
>>> l1
[34, 55, 76]
>>> l1 = [ 55, 76, 34 ]
>>> l1.sort(reverse=True)
>>> l1
[76, 55, 34]

```

> You can define the sorting logic.

```python
>>> str = "hello all world also universe"
>>> str_l = str.split(" ")
>>> str_l.sort()
>>> str_l
['all', 'also', 'hello', 'universe', 'world']
>>> str_l = str.split(" ")
>>> str_l
['hello', 'all', 'world', 'also', 'universe']
>>> str_l.sort(key=len)
>>> str_l
['all', 'also', 'hello', 'world', 'universe']

```

> Note len is a function which calculates length of a string

- Example 7 - List sort and reverse (Not in place)

```python
>>> l1 = [ 55, 76, 34 ]
>>> l2 = sorted(l1)
>>> l1
[55, 76, 34]
>>> l2
[34, 55, 76]
>>> l3 = reversed(l1)
>>> list(l3)
[34, 76, 55]

```

> Note revered returns a iterator.


# Dictionary

- Note keys need to be mutable but not values.
- Orders in key are not fixed
- List of tuple can be directly converted to a list with dict constructor, i.e. dict([('a', 23), ('b': 44)])
- Another way of using dict constructor

```python
>>> c = dict(a=32, b=44)
>>> c
{'a': 32, 'b': 44}

```

- Example 8 - Dictionary also suffer from shallow copy issue

```python
>>> l1 = [34, 22]
>>> l2 = [39, 24]
>>> d = dict(a=l1, b=l2)
>>> d
{'a': [34, 22], 'b': [39, 24]}
>>> l1[0] = 99
>>> d
{'a': [99, 22], 'b': [39, 24]}

```

- Example 9 - Dictionary can be appended with

```python
>>> d.update(dict(c=6))
>>> d
{'a': [99, 22], 'b': [39, 24], 'c': 6}

```

> Note the important behaviour of dictionary update, which can update existing values.

```python
>>> d
{'a': [99, 22], 'b': [39, 24], 'c': 6}
>>> d.update(dict(a='new'))
>>> d
{'a': 'new', 'b': [39, 24], 'c': 6}

```

- Example 10 - Dictionary keys are iterable, thus can be loped on

```python
>>> for i in d:
...   print(i)
...
a
b
c
>>> for i in d.keys():
...   print(i)
...
a
b
c
>>> for i in d.values():
...   print(i)
...
new
[39, 24]
6
>>> for _, i in d.items():
...   print(i)
...
new
[39, 24]
6
```

## Set

Mutable collection of unique unordered immutable objects.

- Example 11 - Creation 

```python
>>> s = set([1, 66, 32, 1])
>>> s
{32, 1, 66}
>>> for i in s:
...   print(i)
...
32
1
66

```

- Example 12 - Update and membership

```python
>>> 1 in s
True
>>> 22 in s
False
>>> s.add(45)
>>> s
{32, 1, 66, 45}
>>> s.update([3, 45])
>>> s
{32, 1, 66, 3, 45}
>>> s.remove(3)
>>> s
{32, 1, 66, 45}
>>> s.remove(99)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 99
>>> s.discard(99)
>>> s.discard(32)
>>> s
{1, 66, 45}
```

- Example 12 - Set theory

```python
>>> s1 = set([1, 55, 75])
>>> s2 = set([14, 55, 75])
>>> s1.union(s2)
{1, 55, 75, 14}
>>> s1.intersection(s2)
{75, 55}
>>> s1.difference(s2)
{1}
>>> s1.symmetric_difference(s2)
{1, 14}
>>> s1.issuperset(s1.difference(s2))
True
>>> (s1.difference(s2)).issubset(s2)
False
>>> (s1.difference(s2)).issubset(s1)
True
>>> (s1.difference(s2)).isdisjoint(s2)
True
```


## Collection Protocols

- Container - str, list, ranger, tuple, byte, set, dict

```python
"is" in "he is great!"
```

- Size - str, list, ranger, tuple, byte, set, dict

```python
len("hello")
```

- Itterable - str, list, ranger, tuple, byte, set, dict

```python
for i in [1, 2, 44]:
  print(i)
```

- Sequence - str, list, ranger, tuple, byte

```python
l = [1, 2, 44]
l[1]
```

- Mutable sequence - list

- Mutable set - set

- Mutable mapping - dict