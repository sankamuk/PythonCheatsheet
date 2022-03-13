
## String representation

- Example 1 - String representation of object [CODE](string_representation_01.py)

```commandline
>>> from string_representation_01 import *
>>> h1 = Human('sankar', 36, 'male')
>>> h1
I am a male of age 36 called as sankar
>>> print(h1)
Human- Name: sankar, Age: 36, Sex: male
>>> str(h1)
'Human- Name: sankar, Age: 36, Sex: male'
>>> repr(h1)
'I am a male of age 36 called as sankar'

```

> Note how *__str__* and *__repr__* used, lets check what are these?

## REPR

- '__repr__' is an unambiguous representation of the string object
- It should clearly identify type and attribute value defining the object
- Note '__repr__' need not be readable for human rather more used for debugging
- '__repr__' is mostly used function for logging
- All Python class has a default repr method which is generic always need override

- Example 2 - More correct representation [CODE](string_representation_02.py)

```commandline
>>> from string_representation_02 import *
>>> h1 = Human('sankar', 36, 'male')
>>> repr(h1)
'Human<name=sankar,age=36,sex=male>'

```

> Since its the more descriptive and informative its used in debugging

```commandline
>>> import pdb
>>> pdb.set_trace()
--Return--
> <stdin>(1)<module>()->None
(Pdb) h1
Human<name=sankar,age=36,sex=male>

```

## STR

- It's the readable and human friendly representation of object
- ***NOTE*** str is also constructor and cast function for String type
- Default implementation of *str* calls internally *repr* function only
- For ***collections*** for contained object *repr* is used

- Example 3 - More correct representation [CODE](string_representation_03.py)

```commandline
>>> from string_representation_03 import *
>>> h1 = Human('sankar', 36, 'male')
>>> str(h1)
'I am an Human male with name sankar of age 36'
>>> l = [Human('sankar', 36, 'male'), Human('alif', 35, 'male')]
>>> str(l)
'[Human<name=sankar,age=36,sex=male>, Human<name=alif,age=35,sex=male>]'

```

## Format

- Its is another representation which can be customized also
- It allows runtime customization with formatted string

- Example 4 - More correct representation [CODE](string_representation_04.py)

```commandline
>>> from string_representation_04 import *
>>> h1 = Human('sankar', 36, 'male')
>>> "Object {}".format(h1)
'Object Human Class - Name sankar, Age 36, Sex male.'
>>> "Object {:s}".format(h1)
'Object I am an Human male with name sankar of age 36'

```

> Note the use of format string to customize the output

## Smart REPR 

- Sometime printing a large object could be meaningless in every sense thus we can use the below library to make it meaningful

- Example 5 - reprlib.repr

```commandline
>>> l = [Human('sankar', 36, 'male'), Human('sankar', 36, 'male'), Human('sankar', 36, 'male'), Human('sankar', 36, 'male'), Human('sankar', 36, 'male'), Human('sankar', 36, 'male')]
>>> import reprlib
>>> reprlib.repr(l)
'[Human<name=sa...e=36,sex=male>, Human<name=sa...e=36,sex=male>, Human<name=sa...e=36,sex=male>, Human<name=sa...e=36,sex=male>, Human<name=sa...e=36,sex=male>, Human<name=sa...e=36,sex=male>]'

```


## Other String Representation Functions

- Example 6 - 'ascii' converts any non ASCII characters in Unicode string with Unicode representation with escape sequence

```commandline
>>> s1 = "भारत"
>>> ascii(s1)
"'\\u092d\\u093e\\u0930\\u0924'"
>>> type(s1)
<class 'str'>
>>> type(ascii(s1))
<class 'str'>

```