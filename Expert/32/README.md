
# Profiling & Performance Tuning 

## Measuring time for Python Code

- Basic measure
In 3.X we use perf_counter to measure time statistics for a code block.

```commandline
>>> from time import perf_counter
>>> start = perf_counter()
>>> max(range(50))
49
>>> print("Time: {}".format(perf_counter() - start))
Time: 6.4402126
```

> Note the time will be in seconds

- Advance measure
Some time you need an average time over multiple execution. In such cases it is timeit.

```commandline
>>> timeit('max(range(500))')
10.633684399999993
```

## CPU Profiler

### CProfiler

We can use CProfile module to profile our code. As an example we profile a sample code.

```commandline
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Expert\32> python.exe .\profile_code_example.py
Running application.
Try login for user 0.
Success
Try login for user 1.
Success
         18 function calls in 6.020 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    6.020    6.020 <string>:1(<module>)
        2    0.000    0.000    6.020    3.010 profile_code_example.py:14(login_user)
        1    0.000    0.000    6.020    6.020 profile_code_example.py:26(main_app)
        2    0.000    0.000    2.002    1.001 profile_code_example.py:8(fetch_user_password)
        1    0.000    0.000    6.020    6.020 {built-in method builtins.exec}
        4    0.002    0.000    0.002    0.000 {built-in method builtins.print}
        4    6.019    1.505    6.019    1.505 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
```

> We can even same profile result to a separate file by running run method as: 
>           cProfile.run('main_app()', filename=prof.out)
> Now we can view the file as below:
>           python -m pstats prof.out

- From IPython or Jupyter we can do profiling as below.

```commandline
# Load python module
%run -n profile_code_example.py

# Run profiler
%prun main_app()

# Profile output sorted by cummilitive time
%prun -s cumulative main_app()
```

### Verify the overheads of common programing constructs

- Dictionary lookup

```python
>>> timeit.timeit(lambda: ({'a': 1, 'b': 3, 'c': 8}).get('b'), number=5)
3.9000005926936865e-06
>>> timeit.timeit(lambda: 3, number=5)
1.7000002117129043e-06
```

- Function call

```python
>>> def lkup(n):
...   return 3
...
>>> timeit.timeit(lambda: lkup('b'), number=5)
3.099999958067201e-06
>>> timeit.timeit(lambda: 3, number=5)
1.99999976757681e-06
```

- List comprehension

```python
>>> timeit.timeit('[0 for _ in range(1000)]', number=5)
0.0014392999999017775
>>> timeit.timeit('[0]*1000', number=5)
2.9799999992974335e-05
>>> [0]*3
[0, 0, 0]
```

> Thus, be careful about unnecessary usage of these constructs.


### Line Profiler (Line by line profiling for a function)

- Line profiler is not in standard library thus we need to import.

```commandline
pip install line_profiler
```

- Now you need to decorate your method which you want to profile with @profile.

```python
@profile
def login_user(user_name, user_secret):
    """Validate a users user & password"""
```

- Then run profiler:

```commandline
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Expert\32> kernprof.exe -l .\line_profile_code_example.py
Running application.
Try login for user 0.
Success
Try login for user 1.
Success
Wrote profile results to line_profile_code_example.py.lprof
```

- View result

```commandline
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Expert\32> python -m line_profiler line_profile_code_example.py.lprof
Timer unit: 1e-06 s

Total time: 6.053 s
File: .\line_profile_code_example.py
Function: login_user at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           @profile
    13                                           def login_user(user_name, user_secret):
    14                                               """Validate a users user & password"""
    15         2       1521.7    760.9      0.0      print("Try login for user {}.".format(user_name))
    16         2    4022648.2 2011324.1     66.5      time.sleep(2)
    17         2    2028320.6 1014160.3     33.5      if fetch_user_password(user_name) == user_secret:
    18         2        508.5    254.2      0.0          print("Success")
    19         2          5.5      2.8      0.0          return 0
    20                                               else:
    21                                                   print("Failed")
    22                                                   return 1
```

> More on [Line Profiler](https://github.com/pyutils/line_profiler)


## Memory Profiler

### Python 3 Memory Profiler

- We need to add profiling code to allow profile module to collect data.

```python
tracemalloc.start()
...
snap = tracemalloc.take_snapshot()
```

- Execute the program to view profile data.

```commandline
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\Expert\32> python.exe .\memory_tracing.py
First list creation.
Second list creation.
1
2
.\memory_tracing.py:21: size=124 B, count=3, average=41 B
.\memory_tracing.py:9: size=80 B, count=2, average=40 B
.\memory_tracing.py:19: size=64 B, count=2, average=32 B
```

> Each line shows the line of code creating memory objects.


### Common Memory Issues

- To ***many small objects*** create unnecessary memory footprint.

- One such use case is Object attribute dictionary `__dict__` which allocated default size.

```python
>>> class NObj:
...   def __init__(self):
...     self._a = 1
...     self._b = 3
...
>>> o1 = NObj()
>>> o1.__dict__
{'_a': 1, '_b': 3}
>>> import sys
>>> sys.getsizeof(o1)
48

```

- Now the alternative of allocating specific memory for specific attribute is assigning `__slots__`.

```python
>>> o2 = SObj()
>>> o2.__dict__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SObj' object has no attribute '__dict__'
>>> o2.__slots__
['_a', '_b']
>>> sys.getsizeof(o2)
48
```

> Note here we do not see the difference as the return of getsize is just reference size.
> To get actual allocation we do profile as below:

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> o3 = SObj()
>>> snap = tracemalloc.take_snapshot()
>>> for s in snap.statistics('lineno'):
...   print(s)
...
<unknown>:0: size=8605 B, count=7, average=1229 B
<stdin>:1: size=48 B, count=1, average=48 B
>>> tracemalloc.start()
>>> o4 = SObj()
>>> snap = tracemalloc.take_snapshot()
>>> for s in snap.statistics('lineno'):
...   print(s)
...
<unknown>:0: size=9296 B, count=13, average=715 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:209: size=848 B, count=2, average=424 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:165: size=816 B, count=2, average=408 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:507: size=568 B, count=1, average=568 B
<stdin>:1: size=552 B, count=3, average=184 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:397: size=512 B, count=3, average=171 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:479: size=488 B, count=2, average=244 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:472: size=464 B, count=2, average=232 B
<stdin>:2: size=448 B, count=1, average=448 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:57: size=440 B, count=1, average=440 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:509: size=416 B, count=1, average=416 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:194: size=416 B, count=1, average=416 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:51: size=416 B, count=1, average=416 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:475: size=408 B, count=1, average=408 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:185: size=96 B, count=2, average=48 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:532: size=56 B, count=1, average=56 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:534: size=48 B, count=1, average=48 B
C:\ProgramData\Anaconda3\lib\tracemalloc.py:291: size=40 B, count=1, average=40 B
```

> The only issue in using __slots__ is you will ***not be able to add attribute*** on the fly to the object.

## Python Disassembler

- If you want to view how Python compiles your code to Byte code you can do it as below.

```python
>>> import dis
>>> from profile_code_example import fetch_user_password
>>> dis.dis(fetch_user_password)
 10           0 LOAD_GLOBAL              0 (time)
              2 LOAD_METHOD              1 (sleep)
              4 LOAD_CONST               1 (1)
              6 CALL_METHOD              1
              8 POP_TOP

 11          10 LOAD_CONST               2 ('DUMMY')
             12 RETURN_VALUE
>>>
```

## Cache

### Simple Cache

- Sometime algorithmic optimization might not be possible and you need other ways of optimization, e.g. Caching.

- Use Case: Fibonacci number generator.
  - Algorithm: f(n) = f(n-1) + f(n-2)
  - Notes:
    - As you can see its recursive and needs generation of smaller Fibonacci numbers.
    - Pattern can easily be deduced to have repetitive generation of a Fibonacci number, i.e. F(n-1) will need F(n-2).
    - Thus caching result could be one perfect optimization solution.

```python
>>> fibonacci_cache = { 0: 0, 1: 1}
>>> def nth_fibonacci(n):
...   if fibonacci_cache.get(n, -1) == -1:
...     fibonacci_cache[n] = nth_fibonacci(n-1) + nth_fibonacci(n-2)
...   return fibonacci_cache[n]
...
>>> nth_fibonacci(10)
55
>>> fibonacci_cache
{0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}
```

> Note this feature we already have library support in Python to use LRU Cache discussed later.

### Lookup Structure

- Sometime lookup Pre-Calculated result could be again an excellent optimization technique.

- Use Case: Number of 1 in a binary n digit number for a decimal number provided.
  - Algorithm: Convert the base10 number into a base2 number and count 1s.
  - Note:
    - Rather than running the algorithm every call we can calculate the numbers upfront and do lookup on every call.

```python
>>> class NumOf1For3DigBin:
...   def __init__(self):
...     self.lookup_cache = {0: 0, 1: 1, 2: 1, 3: 2, 4: 1, 5: 2, 6: 2, 7:3}
...   def get_1s(self, n):
...     if n > 7:
...       print("Input should be less than 8 as only 3 digit binary number supported.")
...     else:
...       print(self.lookup_cache[n])
...
>>> o = NumOf1For3DigBin()
>>> o.get_1s(2)
1
```

### LRU Cache

- Functools already have a module for you to define and use your own Cache with LRU eviction strategy.

```python
>>> import functools
>>> @functools.lru_cache
... def factorial(n):
...   return n * factorial(n-1) if n else 1
...
>>> factorial(10)
3628800
>>> def factorial_old(n):
...   return n * factorial_old(n-1) if n else 1
...
>>> factorial_old(10)
3628800
>>> import timeit
>>> timeit.timeit(lambda: factorial(10), number=5)
3.999999989900971e-06
>>> timeit.timeit(lambda: factorial_old(10), number=5)
1.5900000107649248e-05
```

> Note for LRU Cache you need to make your function arguments hashable.

## Joblib - Pythons native cache service

- Sometime we need a cache that can be used across job execution.
- In such cases either we use external cache service, e.g. Memcache/Redis or use Pythons native version.

```python
>>> from joblib import Memory
>>> memory = Memory('.cache', verbose=1)
>>> @memory.cache
... def factorial_cache(n):
...   return n * factorial_cache(n-1) if n else 1
...
>>> factorial_cache(10)
________________________________________________________________________________
[Memory] Calling __main__-C%3A-Users-HP-OneDrive-Desktop-work-PythonCheatsheet-%3Cstdin%3E.factorial_cache...
factorial_cache(10)
________________________________________________________________________________
[Memory] Calling __main__-C%3A-Users-HP-OneDrive-Desktop-work-PythonCheatsheet-%3Cstdin%3E.factorial_cache...
factorial_cache(9)
________________________________________________________________________________
[Memory] Calling __main__-C%3A-Users-HP-OneDrive-Desktop-work-PythonCheatsheet-%3Cstdin%3E.factorial_cache...
factorial_cache(8)
________________________________________________________________________________
[Memory] Calling __main__-C%3A-Users-HP-OneDrive-Desktop-work-PythonCheatsheet-%3Cstdin%3E.factorial_cache...
factorial_cache(7)
________________________________________________________________________________
[Memory] Calling __main__-C%3A-Users-HP-OneDrive-Desktop-work-PythonCheatsheet-%3Cstdin%3E.factorial_cache...
factorial_cache(6)
________________________________________________________________________________
[Memory] Calling __main__-C%3A-Users-HP-OneDrive-Desktop-work-PythonCheatsheet-%3Cstdin%3E.factorial_cache...
factorial_cache(5)
________________________________________________________________________________
[Memory] Calling __main__-C%3A-Users-HP-OneDrive-Desktop-work-PythonCheatsheet-%3Cstdin%3E.factorial_cache...
factorial_cache(4)
________________________________________________________________________________
[Memory] Calling __main__-C%3A-Users-HP-OneDrive-Desktop-work-PythonCheatsheet-%3Cstdin%3E.factorial_cache...
factorial_cache(3)
________________________________________________________________________________
[Memory] Calling __main__-C%3A-Users-HP-OneDrive-Desktop-work-PythonCheatsheet-%3Cstdin%3E.factorial_cache...
factorial_cache(2)
________________________________________________________________________________
[Memory] Calling __main__-C%3A-Users-HP-OneDrive-Desktop-work-PythonCheatsheet-%3Cstdin%3E.factorial_cache...
factorial_cache(1)
________________________________________________________________________________
[Memory] Calling __main__-C%3A-Users-HP-OneDrive-Desktop-work-PythonCheatsheet-%3Cstdin%3E.factorial_cache...
factorial_cache(0)
__________________________________________________factorial_cache - 0.0s, 0.0min
__________________________________________________factorial_cache - 0.0s, 0.0min
__________________________________________________factorial_cache - 0.0s, 0.0min
__________________________________________________factorial_cache - 0.0s, 0.0min
__________________________________________________factorial_cache - 0.0s, 0.0min
__________________________________________________factorial_cache - 0.0s, 0.0min
__________________________________________________factorial_cache - 0.0s, 0.0min
__________________________________________________factorial_cache - 0.0s, 0.0min
__________________________________________________factorial_cache - 0.0s, 0.0min
__________________________________________________factorial_cache - 0.0s, 0.0min
__________________________________________________factorial_cache - 0.0s, 0.0min
3628800
>>> factorial_cache(11)
________________________________________________________________________________
[Memory] Calling __main__-C%3A-Users-HP-OneDrive-Desktop-work-PythonCheatsheet-%3Cstdin%3E.factorial_cache...
factorial_cache(11)
__________________________________________________factorial_cache - 0.0s, 0.0min
39916800
```

> Note Joblib is not in standard library, and you need to install it.
> Library also supports clearing cache and much more.

- Local on disk cache directory:

```commandline
PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet> dir .cache


    Directory: C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\.cache


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
da---l        24-01-2023     12:41                joblib


PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet> dir .\.cache\joblib\


    Directory: C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet\.cache\joblib


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
da---l        24-01-2023     12:42                __main__-C%3A-Users-HP-OneDrive-Desktop-work-PythonCheatsheet-%3Cstdin%3E


PS C:\Users\HP\OneDrive\Desktop\work\PythonCheatsheet>
```