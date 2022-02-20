
## Class

> Note Python Class names should be CamelCase

- Example 1 - First Class

```python
>>> class MyClass:
...   pass
...
>>> MyClass
<class '__main__.MyClass'>
>>> type(m)
<class '__main__.MyClass'>

```

- Example 2 - Instance method

```python
>>> class MyClass:
...   def intro(self):
...     print("I am Sankar")
...
>>> m = MyClass()
>>> m.intro()
I am Sankar
```

> Note instance method is just normal function in class, can only be invoked over object of class and while defining takes instance object `self` as mandatory first argument but not during call

- Example 3 - Instance initializer

> Python there is no explicit constructor but initializer which configures (initialize) already constructed object
> In Python constructor are provided by the runtime, it invokes initializer if present implicitly
> Python approach of Object property (variable) is handled by initializer, and it is all ***Public***

```python
>>> class MyClass:
...   def __init__(self, name):
...     self._name = name
...   def intro(self):
...     print("Hello {}!".format(self._name))
...
>>> m = MyClass('Jade')
>>> m.intro()
Hello Jade!

```

> Note the use of '_name', its just convention to use internal (no external) use variables with '_'
> Also we can do initialization validation accordingly

```python
>>> class MyClass:
...   def __init__(self, name):
...     if name.isdigit():
...       raise ValueError("Invalid name!")
...     self._name = name
...   def intro(self):
...     print("Hello {}!".format(self._name))
...
>>> m = MyClass("Dabli")
>>> m.intro()
Hello Dabli!
>>> m = MyClass("123")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in __init__
ValueError: Invalid name!
```

- Example 3 - Instance method invocation

```python
>>> class MyClass:
...   def __init__(self, name):
...     self._name = name
...   def intro(self):
...     print("Hello {}!".format(self._name))
...   def salut(self):
...     self.intro()
...     print("Have a great day, {0}" \
...           "Meet you soon {1}" \
...           "".format(self._name, "man"))
...
>>> m = MyClass("Dabli")
>>> m.salut()
Hello Dabli!
Have a great day, DabliMeet you soon man

```

> Note how we print multiline string




