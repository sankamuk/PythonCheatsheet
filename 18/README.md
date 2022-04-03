
## Inheritance

- The subclass initialized should call base class initializer. If subclass initializer not present the base class initializer automatically called.

- Example 01 - Simple single inheritance

```commandline
>>> from inherit_01 import *
>>> b = Base()
Base Class - Init
>>> b.func()
Base Class - func
>>> c = Child()
Base Class - Init
Child Class - Init
>>> c.func()
Child Class - func
```

- Example 02 - Concrete example

```commandline
>>> from inherit_02 import *
>>> l = GenericList([3, 88, 12])
>>> l.add_2_list(44)
>>> l
<GenericList = [3, 88, 12, 44]>
>>>
>>> sl = SortedList([3, 88, 12])
>>> sl
<SortedList = [3, 12, 88]>
>>> sl.add_2_list(44)
>>> sl
<SortedList = [3, 12, 44, 88]>

>>> from inherit_02 import *
>>> sl = SortedList([3, 88, 12])
>>> isinstance(sl, GenericList)
True
>>> isinstance(sl, SortedList)
True
>>> isinstance(sl, (SortedList, list, int))
True
>>> isinstance(sl, (list, int))
False

>>> issubclass(SortedList, GenericList)
True

>>> issubclass(GenericList, SortedList)
False

```

> Note `isinstance` can accept a tuple as second argument, it returns True if the first argument is an element of any one type in tuple
> Function `issubclass` is capable to detect the complete inheritance hierarchy not only direct parent relationship

## Multiple Inheritance

- In Python you can have as many parent class to a child class as you want, you do it just by adding the class names in parentheses after child class name declaration
- The resolution of the correct method to invoked when there is same method implemented in multiple base class is done by protocol defined in MRO (Method Resolution Order)
- If the child class defines no initializer only the initializer of first base class is invoked
- The MRO for a function can be identified by checking the `__mro__` attribute
- Algorithm for MRO is [C3](https://en.wikipedia.org/wiki/C3_linearization)
- Note `super` is not a call to base class but for MRO, so it is just a proxy rather than reference to a single class
- Though `super` can be called with argument but it is better to leave it to Python to put in the correct arguments
- 

- Example 03 - Multiple inheritance

```commandline
>>> class B1:
...   def __init__(self):
...     print("Hello B1")
...
>>> class B2:
...   def __init__(self):
...     print("Hello B2")
...
>>> class C1(B1, B2):
...   pass
...
>>> c1 = C1()
Hello B1
>>>

>>> class B2:
...   def __init__(self):
...     print("Hello B2")
...
>>> class B1:
...   pass
...
>>> class C1(B1, B2):
...   pass
...
>>> c1 = C1()
Hello B2

>>> C1.__bases__
(<class '__main__.B1'>, <class '__main__.B2'>)
>>> B1.__bases__
(<class 'object'>,)


>>> C1.__mro__
(<class '__main__.C1'>, <class '__main__.B1'>, <class '__main__.B2'>, <class 'object'>)

>>> class A:
...   def f1(self):
...     print("A")
...
>>> class B1(A):
...   def f1(self):
...     print("B1")
...
>>> class B2(A):
...   def f1(self):
...     print("B2")
...
>>> class C(B1, B2):
...   pass
...
>>> c1 = C()
>>> C.__mro__
(<class '__main__.C'>, <class '__main__.B1'>, <class '__main__.B2'>, <class '__main__.A'>, <class 'object'>)
>>> C.mro()
[<class '__main__.C'>, <class '__main__.B1'>, <class '__main__.B2'>, <class '__main__.A'>, <class 'object'>]
>>> c1.f1()
B1

>>> super(A, B1)
<super: <class 'A'>, <B1 object>>

```

> Note the use of initializer called when it is absent in different levels
> Also check the use of `__bases__` to identify bases
> Also note the MRO order using attribute `__mro__`
> Note the super proxy creation for two class in inheritance hierarchy


## Python object class

- It is the ultimate base class for all object, starting point of Python's object model
- It provides (using `__[]__` methods) implementation of the basic functionality of all datastructure in Python which are Objects

```commandline
>>> dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__
repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```