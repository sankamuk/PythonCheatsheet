
## Strings (str)

Immutable sequence of unicode characters, to represent a string you can use single quote(') or doube quote(") but cannot
mix it. Using any one allow you to incorporate other in the string.

Example 1 - String constants

```python
>>> "hello world!"
'hello world!'
>>> 'hello world!'
'hello world!'
>>> 'hello world!"
  File "<stdin>", line 1
    'hello world!"
                 ^
SyntaxError: EOL while scanning string literal
>>> "It's my world!"
"It's my world!"
>>> 'I quote "hello world!"'
'I quote "hello world!"'
```

Example 2 - Breaking string

```python
>>> "hello" "world" "!"
'helloworld!'
>>> """hello
...  world
...   !"""
'hello\n world\n  !'
>>> print('hello\n world\n  !')
hello
 world
  !
>>>
>>> v = "hello \
... world \
... !"
>>> print(v)
hello world !

```

> Note the use of '\n' for new line even in Windows (when Windows system use \n\r as new line) system, 
> this is because Python converts it according to the platform automatically.

- Example 3 - Escaping special characters

```python
>>> "I quote \"hello world!\""
'I quote "hello world!"'
>>> print("escaping escape \\")
escaping escape \

```

- Example 4 - Raw String

When you do not need any string replacement or escape sequent to be applied, we use raw string.

```python
>>> v = r'this should not be \n escaped'
>>> print(v)
this should not be \n escaped
>>> v = 'this should not be \n escaped'
>>> print(v)
this should not be
 escaped

```

- Example 5 - String conventions

```python
>>> str(True)
'True'
>>> str(1)
'1'
>>> str(1.0546)
'1.0546'
```

String being just a ***sequence*** we can extract individual letters, which are also strings (hope you expected that).

- Example 6 - String conventions

```python
>>> "hello"[2]
'l'
>>> type("hello"[2])
<class 'str'>

```


Also since string are ***Unicode*** characters you can incorporate characters from other language.

- Example 7 - String conventions

```python
>>> "অ"
'অ'
>>> "\u0985"
'অ'

```

Since string are objects it comes with a lot of helper functions.

- Example 8 - String functions

```python
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
 '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
 '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 
 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 
 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
 'translate', 'upper', 'zfill']
>>>
>>> 'lower'.upper()
'LOWER'

```

## Bytes 

Like String Bytes are immutable sequence of byte-s.

- Example 9 - Bytes

```python
>>> b'this is not string'
b'this is not string'
>>> type(b'byte')
<class 'bytes'>
>>> b'byte'.upper()
b'BYTE'
```

> Note Bytes support same functions as string.


### Convert Byte to String and vice-versa

- Example 9 - Conversion between Bytes String 

```python
>>> b'byte'.decode()
'byte'
>>> type(b'byte'.decode())
<class 'str'>
>>>

>>> 'byte'.encode()
b'byte'
>>> type('byte'.encode())
<class 'bytes'>

```

> Note when you encode a string into byte it's important to provide the encoding in case there non default characters.

```python
>>> "অ - This is bengali letter".encode('utf-8')
b'\xe0\xa6\x85 - This is bengali letter'
>>> "অ - This is bengali letter".encode('utf-8').decode('utf-8')
'অ - This is bengali letter'
```

***NOTES:*** Remember files, network streams, etc are handled as a Bytes stream, thus you will need to convert it to
String (decode with proper encoding type) before using for no confusion or else you might end up with errors.


## List 

List are sequence of objects and are mutable.


- Example 10 - List usage

```python
>>> nl = []
>>> type(nl)
<class 'list'>

>>> l = [ 65, 7, 100]
>>> l[2]
100
>>> l[2] = 'something'
>>> l
[65, 7, 'something']
>>> list("characters")
['c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', 's']

```

> Note the list are 0-indexed and are heterogeneous

- Example 11 - List functions

```python
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
 '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
 '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
 '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
 '__subclasshook__','append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 
 'sort']
>>> l.append("new")
>>> l
[65, 7, 100, 'new']

```


## Dictionary (dict)

Key value pair as a mutable collection

- Example 12 - Dictionary usage

```python
>>> nd = {}
>>> type(nd)
<class 'dict'>

>>> d = {'jad': 38, 'dab': 37, 'alif': 36 }
>>> d['alif']
36
>>> d['alif'] = 37
>>> d
{'jad': 38, 'dab': 37, 'alif': 37}
>>> d['kun'] = 37
>>> d
{'jad': 38, 'dab': 37, 'alif': 37, 'kun': 37}

```

## Collection Itterator (for-loop)

- Example 13 - For each loop usage

```python
>>> l = [ 2, 'san', 1.76 ]
>>> for i in l:
...   print("item - "+ str(i))
...
item - 2
item - san
item - 1.76
>>> d = { 'k1': 43, 'k2': 'some' }
>>> for k in d:
...   print('key - '+ str(k) +', value: '+ str(d[k]))
...
key - k1, value: 43
key - k2, value: some
>>>
```


### Challenge

- Example 14 - Count words in text of few lines

```python
>>> sample_text = """hello world
... how are you today
... how is life for the world"""
>>> word_count = {}

>>> for l in sample_text.split('\n'):
...   for w in l.split():
...     if w in word_count:
...       word_count[w] = word_count[w] + 1
...     else:
...       word_count[w] = 1
...
>>> word_count
{'hello': 1, 'world': 2, 'how': 2, 'are': 1, 'you': 1, 'today': 1, 'is': 1, 'life': 1, 'for': 1, 'the': 1}
>>>
```