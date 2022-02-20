
## File Handling

- Example 1 - Get current system default encoding 

```python
>>> import sys
>>> sys.getdefaultencoding()
'utf-8'
```

- Example 2 - Encoding & Modes

    - https://docs.python.org/3/library/codecs.html#standard-encodings

    - Modes
      - r = Read
      - w = Write
      - x = Open for write but if already present throw error
      - a = Append
      - b = Binary
      - t = Text
      - U = Universal new line (for old codes)

```python
>>> f = open('first.txt', mode='wt', encoding='utf-8')
>>> f.write("Line 1")
6
>>> f.write("Line 2\n")
7
>>> f.write("Line 3\n")
7
>>> f.close()
```

Result

```commandline
PS C:\Users\HP\Desktop\work\PythonCheatsheet> cat .\first.txt
Line 1Line 2
Line 3

```

> File data is actually written to disk (flushed) when you close the file handle
> Note 'write' method does not add new line character
> Note the total character in the file is 6+7+7 = 20 + 2 (universal newline conversion, 2 newline in windows table two byte each '\n\r') = 22

```commandline
PS C:\Users\HP\Desktop\work\PythonCheatsheet> dir .\first.txt


    Directory: C:\Users\HP\Desktop\work\PythonCheatsheet


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        20-02-2022     21:41             22 first.txt

```

- Example 3 - Read

```python
>>> fr = open('first.txt', mode='rt', encoding='utf-8')
>>> fr.read(4)
'Line'
>>> fr.read()
' 1Line 2\nLine 3\n'
>>> fr.read()
''

```

> Note the read pointer already proceeded in the second read

```python
>>> fr.seek(0)
0
>>> fr.read()
'Line 1Line 2\nLine 3\n'
>>> fr.seek(5)
5
>>> fr.read()
'1Line 2\nLine 3\n'
```

- Example 3 - Read line by line

```python
>>> fr.seek(0)
0
>>> fr.readline()
'Line 1Line 2\n'
>>> fr.readline()
'Line 3\n'
>>> fr.readline()
''
>>> fr.seek(0)
0
>>> fr.readlines()
['Line 1Line 2\n', 'Line 3\n']

```

- Example 4 - Close file handles

```python
>>> fr.close()

```

- Example 5 - Append mode

```python
>>> f = open('first.txt', mode='at', encoding='utf-8')
>>> f.writelines( ['line 4', 'Line 5\n', 'Line 6\n'] )
>>> f.close()

```

Result

```commandline
PS C:\Users\HP\Desktop\work\PythonCheatsheet> cat .\first.txt
Line 1Line 2
Line 3
line 4Line 5
Line 6

```

> Note there is no 'writeline' for writing line by line

- Example 6 - Simple read

```python
>>> fr = open('first.txt', mode='rt', encoding='utf-8')
>>> for l in fr:
...   print(l)
...
Line 1Line 2

Line 3

line 4Line 5

Line 6
```

> Note the additional next line character coming from print statement

```python
>>> fr = open('first.txt', mode='rt', encoding='utf-8')
>>> for l in fr:
...   print(l.strip())
...
Line 1Line 2
Line 3
line 4Line 5
Line 6

>>> fr = open('first.txt', mode='rt', encoding='utf-8')
>>> for l in fr:
...   sys.stdout.write(l)
...
Line 1Line 2
13
Line 3
7
line 4Line 5
13
Line 6
7
```

> Using sys.stdout you see characters written as return from write method will not appear if you run in non-interactive mode

- Example 7 - Closing file handle

```python
>>> try:
...   f = open('first.txt', mode='rt', encoding='utf-8')
...   raise Exception("dummy issue")
... finally:
...   f.close()
...
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
Exception: dummy issue

```

> Closing of file is important as without that there is a possibility of loosing data becasuse of miscommunication between your program and OS

## Context Manager

- Example 8 - Closing file handles

````python
>>> with open('first.txt', mode='rt', encoding='utf-8') as f:
...   print(f.read())
...   raise Exception("dummy issue")
...
Line 1Line 2
Line 3
line 4Line 5
Line 6

Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
Exception: dummy issue
````

## Bitwise operator

```python
>>> 0 & 0xff
0
>>> 0 | 0xff
255
>>> 1 >> 1
0
>>> 1 << 1
2

```