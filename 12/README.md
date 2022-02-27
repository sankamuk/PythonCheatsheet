
## Callable Instance

```commandline
PS C:\Users\HP\Desktop\work\PythonCheatsheet\12> cat .\test_class_callable.py

class ASimpleClass:

    def __init__(self):
        self._some_container = []

    def __call__(self, *args, **kwargs):
        print(self._some_container)

    def add_to_container(self, e):
        self._some_container.append(e)
```

- Example 1 - Using callable instance

```python
>>> from test_class_callable import ASimpleClass
>>> c = ASimpleClass()
>>> c.add_to_container("sankar")
>>> c()
['sankar']

```

> Note '__call__' is just a syntactic sugar for invoking function explicitly.
> Also note calling object() and class() is not same, class() (i.e. ASimpleClass()) invokes constructor while calling object(), (i.e. c()) invokes the method, i.e. c.__call__()

- Example 2 - Class invocation

```python
>>> def type_selector(bin_opt):
...   if bin_opt:
...     return list
...   else:
...     return tuple
...
>>> t = type_selector(True)
>>> t
<class 'list'>
>>> t("Hello")
['H', 'e', 'l', 'l', 'o']
>>> t = type_selector(False)
>>> t
<class 'tuple'>
>>> t("Hello")
('H', 'e', 'l', 'l', 'o')
```

## Identifying Callable

- Example 3 - Callable method

```python
>>> def second_letter(x):
...   return x[2]
...
>>> second_l = lambda x: x[2]
>>>
>>> callable(second_l)
True
>>> callable(second_letter)
True
>>> callable(list)
True
>>> callable(list.append)
True
>>> callable("Sankar")
False
>>> callable(1)
False
```

## Conditional Expression

    true_value if condition_expression else false_value

- Example 4 - Single line condition

```python
>>> r =( True if 1 == 2 else False )
>>> r
False
>>> r =( True if 1 != 2 else False )
>>> r
True
```

## Lambda

- Example 5 - Lambda usage

```python
>>> l = ['dabli', 'alif', 'jade', 'kun']
>>> sorted(l, key=lambda x: x[2])
['dabli', 'jade', 'alif', 'kun']
```

> Note without lambda we could have done something like below

```python
>>> def second_letter(x):
...   return x[2]
...
>>> sorted(l, key=second_letter)
['dabli', 'jade', 'alif', 'kun']

```

- Example 6 - Lambda is just a callable

```python
>>> second_l = lambda x: x[2]
>>> second_l
<function <lambda> at 0x00000147E36764C0>
>>> second_l("jade")
'd'

```

|Lambda|Function|
|------|--------|
|Expression|Function with a name|
|No name|Name that binds the function object|
|Arguments separated by comma and ending with colon|Arguments separated by comma and surrounded by parenthesis|
|Zero argument -> Lamda: |Zero argument -> () |
|Body is single expression|Body is block of code|
|No return, expression evaluated to return|Return can be be or not present|
|No testing or documentation support|Support for testing and documentation|


## Function Arguments

- Example 7 - Normal function argument

```python
>>> def print_my_style(x, y):
...   print(x+', '+y)
...
>>> print_my_style('dabli', 'alif')
dabli, alif
>>>
>>> print_my_style('dabli', 'alif', 'jade')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: print_my_style() takes 2 positional arguments but 3 were given
```

- Example 7 - Variable number argument

```python
>>> def print_my_style(*args):
...   print(type(args))
...   print(len(args))
...   print(', '.join(args))
...   print(args)
...
>>> print_my_style('dabli', 'alif', 'jade')
<class 'tuple'>
3
dabli, alif, jade
('dabli', 'alif', 'jade')
>>> print_my_style('dabli', 'alif', 'jade', 'kun')
<class 'tuple'>
4
dabli, alif, jade, kun
('dabli', 'alif', 'jade', 'kun')
>>> print_my_style()
<class 'tuple'>
0

()
```

- Example 8 - Mixed type argument

```python
>>> def min_one_arg(arg_1, *args):
...   print(arg_1+ ", "+ ", ".join(args))
...
>>> min_one_arg("dabli")
dabli,
>>> min_one_arg("dabli", "alif")
dabli, alif
>>> min_one_arg("dabli", "alif", "jade")
dabli, alif, jade
>>> min_one_arg()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: min_one_arg() missing 1 required positional argument: 'arg_1'
```

> Note the variable number argument should come at the end

- Example 9 - Key Valued argument

```python
>>> def arg_dict(**kwargs):
...   print(type(kwargs))
...   print(kwargs)
...   print(kwargs.keys())
...   print(kwargs.values())
...
>>> arg_dict(k1='v1', k2='v2')
<class 'dict'>
{'k1': 'v1', 'k2': 'v2'}
dict_keys(['k1', 'k2'])
dict_values(['v1', 'v2'])
>>> arg_dict(k2='v2', k1='v1')
<class 'dict'>
{'k2': 'v2', 'k1': 'v1'}
dict_keys(['k2', 'k1'])
dict_values(['v2', 'v1'])

```

- Example 10 - Mixed type argument

```python
>>> def mix_arg(nm, **kwargs):
...   print(nm)
...   print(kwargs)
...
>>> mix_arg('dabli', k1='alif', k2='jade')
dabli
{'k1': 'alif', 'k2': 'jade'}

```

***RULES of ARGUMENTS***

- '*' should preceded '**'
- normal positional argument should preceed '*'
- Note a tricky example below
```python
>>> def mix_1(a, b, *c, d):
...   print(a+b+d)
...   print(c)
...
>>> mix_1("dabli", "alif", "kun", d="jade")
dablialifjade
('kun',)
>>> mix_1("dabli", "alif", "kun")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: mix_1() missing 1 required keyword-only argument: 'd'
>>> mix_1("dabli", "alif", "kun", "xun", d="jade")
dablialifjade
('kun', 'xun')

```
- ALso note keyword argument should be the last
```python
>>> def max_2(a, **b, c):
  File "<stdin>", line 1
    def max_2(a, **b, c):
                      ^
SyntaxError: invalid syntax
>>>
```
- Finally all the rules for argument apply for ***Lambda*** and any ***Callable***


## Dynamic Argument

- Example 11 - Dynamic argument function

```python
>>> def mix_3(a, *b):
...   print(a)
...   print(b)
...
>>> l1 = ["dabli", "alif", "kun"]
>>> mix_3(*l1)
dabli
('alif', 'kun')
>>> def mix_4(a, **b):
...   print(a)
...   print(b)
...
>>> d1 = {'a': 'dabli', 'b': 'alif', 'c': 'kun'}
>>> mix_4(**d1)
dabli
{'b': 'alif', 'c': 'kun'}
```

- Example 12 - Usage

```python
>>> l1 = [23, 45, 77]
>>> l2 = [47, 64, 95]
>>> l = [l1, l2]
>>> list(zip(*l))
[(23, 47), (45, 64), (77, 95)]
>>> l3 = [16, 86, 53]
>>> l = [l1, l2, l3]
>>> list(zip(*l))
[(23, 47, 16), (45, 64, 86), (77, 95, 53)]
```