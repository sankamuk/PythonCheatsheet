
```
(mypython) apples-MacBook-Air:~ apple$ python -V
Python 3.7.0
```

###1. REPL

```
(mypython) apples-MacBook-Air:~ apple$ python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>

>>> print('Hello World!')
Hello World!
```

- Help

```
>>> help(os.getcwd)
Help on built-in function getcwd in module posix:

getcwd()
    Return a unicode string representing the current working directory.


>>> file = open('mypackage/mypackage.py')
>>> lineone = file.readline()
>>> help(lineone.split)

Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the words in the string, using sep as the delimiter string.
    
    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit.
```

- Strings

```
>>> print("-"+" sankar "+"-")
- sankar -
>>> print("-"+" sankar ".strip()+"-")
-sankar-
```

###2. List

```
>>> my_list = ["item1", "item2"]
>>> my_list[1]
'item2'
>>> print(my_list)
['item1', 'item2']
>>> len(my_list)
2
>>> print(my_list[0])
item1
>>> my_list.append("item4")
>>> print(my_list)
['item1', 'item2', 'item4']
>>> my_list.pop()
'item4'
>>> print(my_list)
['item1', 'item2']
>>> my_list.extend(["item5", "item6"])
>>> print(my_list)
['item1', 'item2', 'item5', 'item6']
>>> my_list.remove("item5")
>>> print(my_list)
['item1', 'item2', 'item6']
>>> my_list.insert(1, "item3")
>>> print(my_list)
['item1', 'item3', 'item2', 'item6']
>>> my_list.append(4)
>>> print(my_list)
['item1', 'item3', 'item2', 'item6', 4]
>>>

>>> for i in my_list:
...   print(i)
... 
item1
item3
item2
item6
4

>>> c = 0
>>> while c < len(my_list) :
...   print(my_list[c])
...   c = c+1
... 
item1
item3
item2
item6
4
```

> Notice

```
>>> my_list[11]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

>>> type('string 1')
<class 'str'>
>>> type("string 2")
<class 'str'>
>>> type("string 2')
  File "<stdin>", line 1
    type("string 2')
                   ^
SyntaxError: EOL while scanning string literal

>>> name = 1
>>> Name = 'one'
>>> print(name)
1
>>> print(Name)
one

>>> my_list.append([3, 5])
>>> print(my_list)
['item1', 'item3', 'item2', 'item6', 4, [3, 5]]

>>> for i in my_list:
...   if isinstance(i, list) :
...     for e in i :
...       print(e)
...   else :
...     print(i)
... 
item1
item3
item2
item6
4
3
5
```

> Note
```
>>> dir(__builtins__) # List all build in functions
```

###3. Package & Module

- List python path

```
import sys
print(sys.path)
```

- Building custom package


mypackage.py

```
'''
This is a module to print list
'''
def print_nested_list(a_list):
  '''
  This function recursively print a nested list.
  '''
  for e in a_list :
    if isinstance(e, list):
      print_nested_list(e) # Recursive function call
    else:
      print(e)
```

cat setup.py 
```
from distutils.core import setup

setup (
  name = 'mypackage',
  version = '1.0.0',
  py_modules = ['mypackage'],
  author = 'Sankar',
  author_email = 'sanmuk21@gmail.com',
  url = 'https://mukherjeesankar.com',
  description = 'Simple List Printer',
)


(mypython) apples-MacBook-Air:mypackage apple$ ls -ltr
total 16
-rw-r--r--  1 apple  staff  257 Feb  5 21:52 mypackage.py
-rw-r--r--  1 apple  staff  254 Feb  5 21:57 setup.py
```

- Run build

```
(mypython) apples-MacBook-Air:mypackage apple$ python setup.py sdist
running sdist
running check
warning: sdist: manifest template 'MANIFEST.in' does not exist (using default file list)

warning: sdist: standard file not found: should have one of README, README.txt, README.rst

writing manifest file 'MANIFEST'
creating mypackage-1.0.0
making hard links in mypackage-1.0.0...
hard linking mypackage.py -> mypackage-1.0.0
hard linking setup.py -> mypackage-1.0.0
creating dist
Creating tar archive
removing 'mypackage-1.0.0' (and everything under it)

(mypython) apples-MacBook-Air:mypackage apple$ ls -ltR
total 24
drwxr-xr-x  3 apple  staff   96 Feb  5 21:58 dist
-rw-r--r--  1 apple  staff   65 Feb  5 21:58 MANIFEST
-rw-r--r--  1 apple  staff  255 Feb  5 21:58 setup.py
-rw-r--r--  1 apple  staff  257 Feb  5 21:52 mypackage.py

./dist:
total 8
-rw-r--r--  1 apple  staff  633 Feb  5 21:58 mypackage-1.0.0.tar.gz
```

- Upload your pakage to PiPy.

python setup,py register
(Give your PiPy use name and password)

```
python setup.py sdist upload
```

- Install

```
(mypython) apples-MacBook-Air:mypackage apple$ python setup.py install 
running install
running build
running build_py
creating build
creating build/lib
copying mypackage.py -> build/lib
running install_lib
copying build/lib/mypackage.py -> /Users/apple/TEST/mypython/lib/python3.7/site-packages
byte-compiling /Users/apple/TEST/mypython/lib/python3.7/site-packages/mypackage.py to mypackage.cpython-37.pyc
running install_egg_info
Writing /Users/apple/TEST/mypython/lib/python3.7/site-packages/mypackage-1.0.0-py3.7.egg-info
```

- Use your package

```
(mypython) apples-MacBook-Air:mypackage apple$ python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import mypackage
>>> list_test = [ 3, 5, 'Sankar', [ 7, 't'], 8 ]
>>> mypackage.print_nested_list(list_test)
3
5
Sankar
7
t
8
>>> 
```

- Namespace

	1. All function are bound to name space.
	2. Module name of function becomes its name space.
	3. By default a code
	4. Your module of execution is automatically assigned to __main__ namespace.
	5. All Build In Functions are auto imported and tagged to __buildin__ namespacee.

> Note .pyc files are just run time optimised version of your python program.

- Build In Function

```
>>> for i in range(4):
...   print(i)
... 
0
1
2
3


>>> l = [ 2 ]
>>> l.append(3)
>>> l
[2, 3]
>>> if len(l) == 1:
...   print('one')
... elif len(l) == 2:
...   print('two')
... else:
...   print('more than two')
... 
two
```


###4. Functions and prarameter

- Update previous function to print element with differnt indentation.

```
def print_nested_list(a_list, indent_level=0):
  '''
  This function recursively print a nested list.
  '''
  for e in a_list :
    if isinstance(e, list):
      print_nested_list(e, indent_level+1) # Recursive function call
    else:
      print_str = ' '
      for i in range(indent_level):
        print_str = ' '+print_str
      print_str = print_str+str(e)
      print(print_str)
```

- Now you can use one or two parameter, for former the value of indent_level will be 0.

```
>>> import mypackage
>>> list_test = [ 3, 5, 'Sankar', [ 7, 't'], 8 ]
>>> mypackage.print_nested_list(list_test)
```


###5. OS Module

- Working with system path

```
>>> import os
>>> os.getcwd()
'/Users/apple'
>>> os.chdir('TEST/python_tutorial/')
>>> os.getcwd()
'/Users/apple/TEST/python_tutorial'
>>> os.listdir()
['mypackage']
```

- List imported module

```
>>> dir()
['NamedList', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '__warningregistry__', 'a', 'cleaned_time_list', 'd', 'f', 'first_class', 'hdata', 'health', 'line', 'num_list', 'runner', 'san', 'sort_list', 'time_list', 'two_times']
```

- Working with files

```
>>> file = open('mypackage/mypackage.py')
>>> print(file.readline())
'''

>>> print(file.readline(), end=' ')
This is a module to print list
 >>> file.seek(0)
0
>>> print(file.readline(), end=' ')
'''
 >>> 
>>> for line in file:
...   print(line, end=' ')
... 
This is a module to print list
'''
```

> Note always close file handles - file.close()


```
>>> for employee in open('sample.txt'):
...   (cars, name) = employee.split(':')
...   print("Cars: {0}, Name: {1}".format(cars, name))
... 
Cars: 23, Name: Sankar

Cars: 20, Name: Jade

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: too many values to unpack (expected 2)
```

> Note the target of Split method is not List but its immutable version called ***Tuple***.

- Fix max split

```
>>> print(lineone.split(' '))
['This', 'is', 'a', 'module', 'to', 'print', 'list\n']
>>> print(lineone.split(' ', 2))
['This', 'is', 'a module to print list\n']
```

- Confirm charater in string

```
>>> greet = "Hi all, how are you"
>>> greet.find(',')
6
>>> greet.find(':')
-1
>>> greet.find('all')
3
```

- Import with alias

```
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)
```

###6. Exception & Handling

```
>>> for employee in open('sample.txt'):
...   try:
...     (cars, name) = employee.split(':')
...     print("Cars: {0}, Name: {1}".format(cars, name))
...   except:
...     print("Bad record: "+str(employee))
... 
Cars: 23, Name: Sankar

Cars: 20, Name: Jade

Bad record: 29::Xun

>>> for employee in open('sample.txt'):
...   try:
...     (cars, name) = employee.split(':')
...     print("Cars: {0}, Name: {1}".format(cars, name))
...   except:
...     pass
... 
Cars: 23, Name: Sankar

Cars: 20, Name: Jade
```

> Note ***pass*** replaces a empty block of python code, just a do nothing block.

- Additional code to Error

```
>>> if os.path.exists('sample1.txt') :
...   for employee in open('sample.txt'):
...     try:
...       (cars, name) = employee.split(':')
...       print("Cars: {0}, Name: {1}".format(cars, name))
...     except:
...       print("Bad record: "+str(employee))
... else:
...   print('No such file')
... 
No such file
```

- Specific Exception handling

```
>>> try
...   data = open('sample1.txt')
...   for employee in data :
...     try:
...       (cars, name) = employee.split(':')
...       print("Cars: {0}, Name: {1}".format(cars, name))
...     except:
...       print("Bad record: "+str(employee))
... except IOError:
...   print('No such file')
... 
No such file
```

Excersise: Find from the list of quotes made by individual who say how many negation quote.

Input: quote.txt 
```
Swami said all man can pray.
Doctor says man cannot enjoy alone.
Doctor say try to laugh.
Swami says do not cry alone.
Teacher said people are always a student.
```

Solution:
```
>>> try :
...   negative_quote = {}
...   positive_quote = {}
...   lines = open('quote.txt')
...   for line in lines :
...     ch = line.split(" ")[0]
...     act = line.split(" ")[1]
...     sy = " ".join(e for e in line.split(" ")[2:])
...     if 'no' in sy.lower() :
...       if ch in negative_quote.keys() :
...         negative_quote[ch] = negative_quote[ch] + 1
...       else :
...         negative_quote[ch] = 1
...     else :
...       if ch in positive_quote.keys() :
...         positive_quote[ch] = positive_quote[ch] + 1
...       else :
...         positive_quote[ch] = 1   
...   print('Negative')
...   print(negative_quote)
...   print('Positive')
...   print(positive_quote) 
... except IOError:
...   pass
... 
Negative
{'Doctor': 1, 'Swami': 1}
Positive
{'Swami': 1, 'Doctor': 1, 'Teacher': 1}
```

```
>>> lines = open('quote.txt')
>>> swamiq = []
>>> for line in lines:
...   if line.lower().find("swami") != -1 :
...     swamiq.append(line)
... 
>>> 
>>> lines.close()


>>> try :
...   nlines = open('swami.txt', 'w')
...   print(swamiq, file=nlines)
... except :
...   print('Exception in writing files.')
... finally:
...   if nlines in locals() : 
...     nlines.close()

apples-MacBook-Air:python_tutorial apple$ cat swami.txt 
['Swami said all man can pray.\n', 'Swami says do not cry alone.\n']

 > Note locals build in function prints all variable in current scope
 >>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'os': <module 'os' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py'>, 'employee': '29::Xun\n', 'cars': '20', 'name': 'Jade\n', '__warningregistry__': {'version': 0}, 'positive_quote': {'Swami': 1, 'Doctor': 1, 'Teacher': 1}, 'negative_quote': {'Doctor': 1, 'Swami': 1}, 'lines': <_io.TextIOWrapper name='swami.txt' mode='w' encoding='UTF-8'>, 'line': 'Teacher said people are always a student.\n', 'character': 'Swami', 'action': 'said', 'ch': 'Teacher', 'act': 'said', 'sy': 'people are always a student.\n', 'd': {'sa': 2, 'ch': 2}, 'l': [2, 3], 'swami_quotes': <_io.TextIOWrapper name='swami.txt' mode='w' encoding='UTF-8'>, 'swamiq': ['Swami said all man can pray.\n', 'Swami says do not cry alone.\n']}


>>> try :
...   for l in open('no_such_file.txt') :
...     print(l)
... except IOError as err:
...   print("Error: "+str(err))
... 
Error: [Errno 2] No such file or directory: 'no_such_file.txt'
```


- Use with to forget finally and file close

```
>>> try :
...   with open('sample.txt') as f:
...     for l in f:
...       print(l)
... except :
...   print('Error in opening file.')
... 

>>> with open('health.txt') as f:
...   d = f.readline()
...   while d :
...     print(d)
...     d = f.readline()
...


>>> def print_nested_list(a_list, indent_level=0, fh=sys.stdout):
...   '''
...   This function recursively print a nested list.
...   '''
...   for e in a_list :
...     if isinstance(e, list):
...       print_nested_list(e, indent_level+1, fh) 
...     else:
...       print_str = ' '
...       for i in range(indent_level):
...         print_str = ' '+print_str
...       print_str = print_str+str(e)
...       print(print_str, file=fh)
```

- Pickle

```
>>> import pickle
>>> with open('result.txt', 'wb') as f:
...   pickle.dump([1, 2, 3], f)
>>> with open('result.txt', 'rb') as f:
...   l = pickle.load(f)
... 
>>> l
[1, 2, 3]

>>> try:
...   with open('result.txt', 'rb') as f1, open('output.txt', 'rb') as f2:
...     l1 = pickle.load(f1)
...     print(l1)
...     l2 = pickle.load(f2)
...     print(l2)
... except IOError as er:
...   print('Error'+str(er))
... except pickle.PickleError as per:
...   print('Error'+str(per))
... 
[1, 2, 3]
['sa', 'ja']
```

###7. Data Manupulation

- Sorting

```
>>> num_list = [ 3, 7, 1, 5 ]
>>> sort_list = sorted(num_list)
>>> sort_list
[1, 3, 5, 7]
>>> print(num_list)
[3, 7, 1, 5]
>>> num_list.sort()
>>> print(num_list)
[1, 3, 5, 7]
```

- List Comprehension

```
>>> two_times = [ num * 2 for num in num_list ]
>>> two_times
[2, 6, 10, 14]

>>> ' '.join([ str(n) for n in num_list ])
'1 3 5 7'


>>> ' '.join([ str(n) for n in num_list if ( n % 2 == 0 ) ])
'8'
>>> ' '.join([ str(n) for n in num_list if ( n % 2 != 0 ) ])
'3 7 1 5'
>>>

>>> time_list = [ '4.34', '5:64', '2-5' ]
>>> sorted([ int(nstr[0]) * 60 + int(nstr[2:]) for nstr in time_list ])[0:2]
[125, 274]

>>> time_list = [ '4.34', '5:64', '2-5' , '5=64' ]
>>> list(set(sorted([ int(nstr[0]) * 60 + int(nstr[2:]) for nstr in time_list ])))[0:2]
[274, 364]
```

- Poping list Item

```
>>> time_list.pop(3)
'5=64'
>>> time_list
['4.34', '5:64', '2-5']
```

###8. Complex Data Structures

- DICTIONARY a Key/Value Store

```
>>> health = {}
>>> for line in open('health.txt') :
...   hdata = {}
...   hdata['dob'] = line.split(',')[1]
...   hdata['stats'] = line.split(',')[2].strip().split(';')
...   health[line.split(',')[0]] = hdata
... 
>>> health
{'Sankar': {'dob': '10-10-1999', 'stats': ['9-34', '2:32', '4.3']}, 'Jade': {'dob': '2-4-1899', 'stats': ['8.34', '5.3']}}
>>> health.keys()
dict_keys(['Sankar', 'Jade'])
>>> type(health)
<class 'dict'>
```

- CLASS a Encapsulation of data and functionality

```
>>> class first_class() :
...   def __init__(self) :
...     print("An instance of first_class is created"+str(self))
...   def some_functn(self, name) :
...     print("Hi "+name)
... 
>>> a = first_class()
An instance of first_class is created<__main__.first_class object at 0x10bcf4898>
>>> a.some_functn("Kun")
Hi Kun

> The __init__ is the constructor for your class.
> All class method should have self as its first argument.
> 	a = first_class() 		~	first_class.__init__(a) 
>	a.some_functn("Kun") 	~	first_class.some_functn(a, "Kun")


>>> class runner() :
...   def __init__(self, nm) :
...     self.name = nm
...     print("An instance of first_class is created, with name "+ self.name +". Object is "+str(self))
...   def run(self) :
...     print("Run "+ self.name)
... 
>>> san = runner("Sanka")
An instance of first_class is created, with name Sanka. Object is <__main__.runner object at 0x10bee0438>
>>> san.run()
Run Sanka
```

- Inheritence

```
>>> class NamedList(list) :
...   def __init__(self, nm) :
...     list.__init__([])
...     self.name = nm
...   def saymyname(self) :
...     print(self.name)
... 
>>> a = NamedList('Sankar')
>>> a.saymyname()
Sankar
>>> a.append('2')
>>> a
['2']
>>> a[0]
'2'
```

> Above is an example of inheriting and buildin Python class, i.e. List.

```
>>> class NamedList(list) :
...   def __init__(self, nm) :
...     list.__init__([])
...     self.name = nm
...   @property
...   def saymyname(self) :
...     print(self.name)
... 
>>> a = NamedList('Sankar')
>>> a.saymyname 
```

> Function call treated as a class property with @property decorator 


###9. Web Technology


- Start pure python web endpoint

```
>>> from http.server import HTTPServer, CGIHTTPRequestHandler
>>> import cgitb
>>> port = 8888
>>> httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
>>> print("Starting simple_httpd on port: " + str(httpd.server_port))
Starting simple_httpd on port: 8888
>>> cgitb.enable()
>>> httpd.serve_forever()
```

> cgitb logs error in web page, good for development

- JSon

```
>>> import json
>>> alist = [ 'san', [ 3, 'jad' ], 6 ]
>>> 
>>> 
>>> ajson = json.dumps(alist)
>>> ajson
'["san", [3, "jad"], 6]'
>>> thelist = json.loads(ajson)
>>> thelist
['san', [3, 'jad'], 6]
```

> Note JSon dumps, loads cannot encode custom user defined datatype like Pickle.

- Generic HTTP Client

```
from urllib import urlencode 
from urllib2 import urlopen

def send_to_server(url, post_data=None): 
  if post_data:
    page = urlopen(url, urlencode(post_data)) 
  else:
    page = urlopen(url) 
  return(page.read().decode("utf8"))
```


###9. SQLite

- Python to RDDMS Flow

```
                                --> commit   --
                               |               |
connect -> create -> interact -|               |--> close
                               |               |
                                --> rollback --

```

- Import

import sqlite3

- Connect

```
conn = sqlite3.connect('my.db.sqllite')
```

- Create

```
cursor = conn.cursor()
```

- Interact

```
cursor.execute("""SELECT DATE('NOW')""")
```

- Commit

```
conn.commit()
```

- Close
```
conn.close()
```

- Sample
```
>>> import sqlite3       
>>> conn = sqlite3.connect('mydb.sqlite')
>>> cursor = conn.cursor()

>>> cursor.execute("""create table user (id integer primary key autoincrement unique not null,
...                                      name text not null)""")
<sqlite3.Cursor object at 0x10587eea0>
>>> cursor.execute("""create table score (user_id integer not null, 
...                                       score integer not null,
...                                       foreign key(user_id) references user )""")
<sqlite3.Cursor object at 0x10587eea0>

>>> conn.commit()
>>> conn.close()



apples-MacBook-Air:python_tutorial apple$ sqlite3 mydb.sqlite 
SQLite version 3.24.0 2018-06-04 14:10:15
Enter ".help" for usage hints.
sqlite> .tables
score  user 

sqlite> .schema user 
CREATE TABLE user (id integer primary key autoincrement unique not null,
                                     name text not null);
sqlite> .schema score
CREATE TABLE score (user_id integer not null,  
                                      score integer not null,
                                      foreign key(user_id) references user );



>>> conn = sqlite3.connect('mydb.sqlite')
>>> cursor = conn.cursor()
>>> nm = 'Sankar'
>>> cursor.execute("insert into user(name) values (?)", (nm,))
<sqlite3.Cursor object at 0x10587ef80>
>>> cursor.execute("insert into user(name) values (?)", ('Jade',))
<sqlite3.Cursor object at 0x10587ef80>
>>> conn.commit()

sqlite> select * from user ;
1|Sankar
2|Jade
sqlite>


>>> cursor.execute("select id from user where name = ?", ('Jade',))
<sqlite3.Cursor object at 0x10587ef80>
>>> cursor.fetchone()
(2,)
>>> cursor.fetchmany()
[]
>>> cursor.execute("select id from user where name = ?", ('Jade',))
<sqlite3.Cursor object at 0x10587ef80>
>>> cursor.fetchmany()
[(2,)]
>>> cursor.execute("select id from user where name = ?", ('Jade',))
<sqlite3.Cursor object at 0x10587ef80>
>>> cursor.fetchall()
[(2,)]
>>> cursor.execute("select id from user where name = ?", ('Jade',))
<sqlite3.Cursor object at 0x10587ef80>
>>> cursor.fetchone()[0]
2


>>> cursor.execute("select id from user where name = ?", ('Jade',))
<sqlite3.Cursor object at 0x10587ef80>
>>> uid = cursor.fetchone()[0]
>>> cursor.execute("insert into score (user_id, score) values (?, ?)", (uid, 3))
<sqlite3.Cursor object at 0x10587ef80>
>>> cursor.execute("insert into score (user_id, score) values (?, ?)", (uid, 9))
<sqlite3.Cursor object at 0x10587ef80>
>>> conn.commit()

sqlite> select * from score ;
2|3
2|9
sqlite>


>>> cursor.execute("select * from user, score where user_id = id and name = ?", ('Jade',))
<sqlite3.Cursor object at 0x10587ef80>
>>> cursor.fetchall()
[(2, 'Jade', 2, 3), (2, 'Jade', 2, 9)]
```

###10. Data Handling

- Input

```
>>> ch = input('Your name ? ')
Your name ? Sankar
>>> ch
'Sankar'

- Time

>>> import datetime

>>> dt = datetime.datetime.now()
>>> print(dt)
2020-02-10 00:44:36.370752
>>> dt.hour
0
>>> dt.day
10
>>> dt.year
2020

>>> dtnew = datetime.datetime.now()
>>> dtnew - dt
datetime.timedelta(seconds=74, microseconds=593577)
>>> dif = dtnew - dt
>>> dif.seconds
74

>>> dt_from_str = datetime.datetime.strptime("2020-02-01 00:10:00", "%Y-%m-%d %H:%M:%S")
>>> print(dt_from_str)
2020-02-01 00:10:00

>>> import pytz
>>> timezone = pytz.timezone('America/New_York')
>>> timezone_date_time_obj = timezone.localize(dt_from_str)
>>> print(timezone_date_time_obj)
2020-02-01 00:10:00-05:00
>>> print(timezone_date_time_obj.tzinfo)
America/New_York

>>> dt_delta = dt_from_str + datetime.timedelta(days=2)
>>> print(dt_delta)
2020-02-03 00:10:00
>>> dt_delta = dt_from_str + datetime.timedelta(days=-2)
>>> print(dt_delta)
2020-01-30 00:10:00
```
