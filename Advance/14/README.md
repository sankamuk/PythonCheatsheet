
## Python Class Attributes

- Example 1 - Using class attribute

```python
>>> class SomeClass:
...   cls_attr = 0
...   def __init__(self, name):
...     SomeClass.cls_attr += 1
...     self.name = name
...     self.id = SomeClass.cls_attr
...   def greet(self):
...     print("I am Class {0} with id {1}".format(self.name, self.id))
...
>>> c1 = SomeClass("Class1")
>>> c2 = SomeClass("Class2")
>>> c3 = SomeClass("Class3")
>>> c1.greet
<bound method SomeClass.greet of <__main__.SomeClass object at 0x00000299EADC15E0>>
>>> c1.greet()
I am Class Class1 with id 1
>>> c2.greet()
I am Class Class2 with id 2
>>> c3.greet()
I am Class Class3 with id 3
>>> c1.cls_attr
3
>>> c2.cls_attr
3
>>> c3.cls_attr
3

```

## Static & Class Method

- Example 2 - Using static method

```python
>>> class SomeClass:
...   cls_counter = 0
...   @staticmethod
...   def incr_counter():
...     SomeClass.cls_counter += 1
...     return SomeClass.cls_counter
...   def __init__(self):
...     self.id = SomeClass.incr_counter()
...   def greet(self):
...     print("Class {}".format(self.id))
...
>>> c1 = SomeClass()
>>> c2 = SomeClass()
>>> c1.greet()
Class 1
>>> c2.greet()
Class 2

```

> Note
> - Method *incr_counter* doesnot need self as its static method
> - Note when calling *incr_counter* we use Class name rather than object (i.e. self)
> - Generally rather than using static method you should use module level function and use *classmethod* in case you need to refer to class scoped attribute


- Example 3 - Using class method

```python
>>> class SomeClass:
...   cls_counter = 0
...   @classmethod
...   def incr_counter(cls):
...     cls.cls_counter += 1
...     return cls.cls_counter
...   def __init__(self):
...     self.id = SomeClass.incr_counter()
...   def greet(self):
...     print("Class {}".format(self.id))
...
>>> c2 = SomeClass()
>>> c2.greet()
Class 1
```

***Note*** Generally Class Method is used to create custom class initializers

- Example 4 - Class initializer overloading

```python
>>> class SomeClass:
...   def __init__(self, name, age):
...     self.name = name
...     self.age = age
...   @classmethod
...   def no_name(cls):
...     return cls("Anonymous", 0)
...   @classmethod
...   def no_age(cls, name):
...     return cls(name, 0)
...   def greet(self):
...     print("Hello, i am {0}. I am {1} years old!".format(self.name, self.age))
...
>>> c1 = SomeClass("sankar", 18)
>>> c1.greet()
Hello, i am sankar. I am 18 years old!
>>> c2 = SomeClass.no_name()
>>> c2.greet()
Hello, i am Anonymous. I am 0 years old!
>>> c3 = SomeClass.no_age("alif")
>>> c3.greet()
Hello, i am alif. I am 0 years old!
```

***NOTE*** Both *staticmethod* and *classmethod* are inherited and can be overridden in derived class also, also the *cls* argument will be set accordingly
     Thus for base class *cls* will refer to Base class and for Derived class *cls* will refer to Derived class


## Class Attributes

- Example 5 - Getting and setting attribute of class [DEFINITION](class_sample.py)

```commandline
>>> from class_sample import Man
>>> m = Man('sankar')
>>> m.greet()
Hello World, i am a male named sankar with id 1 and working status yes
>>> m.working = "no"
>>> m.greet()
Hello World, i am a male named sankar with id 1 and working status no
>>> m.working = "noo"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\HP\Desktop\work\PythonCheatsheet\14\class_sample.py", line 27, in working
    raise Exception("Invalid Input - Could be only yes/no")
Exception: Invalid Input - Could be only yes/no
>>> m.name = "alif"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
```

> Note
> - property (Decorator) used to expose getter, while [getter].[setter] (Method on Decorator) used as setter
> - All internal class attribute and method uses ***_*** to signify internal class scope

***NOTE*** Property are also inherited as usual in derived class, also same property can be overridden if required in derived or subclass
     Also if required you can access Base class property by calling *super()* 

- Example 6 - Inheritance of setter attribute of class [DEFINITION](class_setter_inheritance.py)

```commandline
>>> from class_setter_inheritance import *
>>> h = Human("sankar")
>>> h.greet()
Hello World, i am sankar working status no-work
>>> h.working = "work"
>>> h.greet()
Hello World, i am sankar working status work
>>> m = Man("Alif")
>>> m.greet()
Hello World, i am Man: Alif working status no-work
>>> m.working = "man-work"
>>> m.greet()
Hello World, i am Man: Alif working status man-work
>>> m.working = "work"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\HP\Desktop\work\PythonCheatsheet\14\class_setter_inheritance.py", line 36, in working
    raise Exception("Invalid Input - Could be only man-work/no-work")
Exception: Invalid Input - Could be only man-work/no-work
```

> Note
> - A setter is inherited with a bit of subtlety

