
## Python Introspection

- Example 01 - Type

```commandline
>>> type(4)
<class 'int'>
>>> int
<class 'int'>
>>> type(4) is int
True

>>> type(type)
<class 'type'>
>>> type.__class__
<class 'type'>

>>> issubclass(type, object)
True
>>> issubclass(object, type)
False
>>> type(object)
<class 'type'>

>>> isinstance(7, int)
True

```

> Its always advised to use `isinstance` programmatically rather than `type`

- Example 02 - Get attribute

```commandline
>>> v = 7
>>> dir(v)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__',
 '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__
', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__'
, '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> v.numerator
7
>>> getattr(v, 'numerator')
7
>>> hasattr(v, 'numerator')
True
>>> hasattr(v, 'numeratorrrrr')
False


>>> callable(getattr(v, 'conjugate'))
True
>>> callable(getattr(v, 'numerator'))
False

```

- Example 02 - Scopes

```commandline
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
>>> a = 22
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 22}
>>> globals()['b'] = 33
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 22, 'b': 33}

>>> def f():
...   l = 88
...   print(globals())
...   print(locals())
...
>>> f()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 22, 'b': 33, 'f': <
function f at 0x00000229DCB86310>}
{'l': 88}

>>> v = 22
>>> k = 11
>>> "v = {v} k = {k}".format(**locals())
'v = 22 k = 11'

```

- Example 02 - Inspect

```commandline
>>> import inspect
>>> import sample_01
>>>
>>> inspect.ismodule(sample_01)
True
>>> inspect.getmenbers(sample_01)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'inspect' has no attribute 'getmenbers'
>>> inspect.getmembers(sample_01)
[('__builtins__', {'__name__': 'builtins', ...


>>> inspect.getmembers(sample_01, inspect.isclass)
[]
>>> inspect.getmembers(sample_01, inspect.isfunction)
[('f1', <function f1 at 0x000001CFE41E7D30>)]

```