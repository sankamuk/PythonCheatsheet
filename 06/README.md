
## Exception

- Raising Exception interrupts execution flow.
- Handle Exception resumes flow.
- Unhandled Exception will terminate the execution.
- Exception object contains all information about the Exception event.
- Exception travels several levels in call stack until it is handled or finally terminating the runtime.
- Never try to handle programming errors, i.e. SyntaxError, IndentationError, NameError
- In case you do not have anything in your handle code, use 'pass'
- Rather handling all possible exception , Python vote for clean code while let it fail for extreme cases by throwing exception
- Use final block for any cleanup action

- Example 1 - Sample exception

```python
>>> int("hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'hello'

```

> Note 'ValueError' is Exception type while 'invalid literal for int() with base 10: 'hello'' is the Exception message.

- Example 2 - Handling exception

```python
>>> try:
...   int("hello")
... except Exception:
...   print("Cannot convert to number")
...
Cannot convert to number
```

- Example 2 - Generic and Specific exception

```python
>>> try:
...   int("hello")
... except ValueError:
...   print("Cannot convert to number")
...
Cannot convert to number
>>> try:
...   int([1, 4, 5])
... except ValueError:
...   print("Cannot convert to number")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'


>>> try:
...   int([1, 4, 5])
... except ValueError:
...   print("Cannot convert to number")
... except TypeError:
...   print("Type of the object not compartible with number")
...
Type of the object not compartible with number

>>> try:
...   int([1, 4, 5])
... except (ValueError, TypeError):
...   print("Cannot convert to number")
...
Cannot convert to number

>>> try:
...   int([1, 4, 5])
... except (ValueError, TypeError):
...   pass
...
```

- Example 3 - Printing Exception

```python
>>> try:
...   int([1, 4, 5])
... except (ValueError, TypeError) as e:
...   print(str(e))
...
int() argument must be a string, a bytes-like object or a number, not 'list'
>>>
>>> try:
...   int([1, 4, 5])
... except (ValueError, TypeError) as e:
...   print(str(e), file=sys.stderr)
...
int() argument must be a string, a bytes-like object or a number, not 'list'
```

> Note in second example we put message in System Error.


- Example 4 - Handle code can re-raise the same error

```python
>>> try:
...   int([1, 4, 5])
... except (ValueError, TypeError):
...   print("i can do nothing")
...   raise
...
i can do nothing
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> try:
...   int([1, 4, 5])
... except (ValueError, TypeError) as e:
...   print("i can do nothing, but i will raise new error")
...   raise Exception("New error")
...
i can do nothing, but i will raise new error
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
Exception: New error
```

> Note in second case I raise a new error not related to original error.

- Example 5 - Finally finally block

```python
>>> try:
...   int([1, 4, 5])
... except (ValueError, TypeError) as e:
...   print("exception handled")
... finally:
...   print("done")
...
exception handled
done
>>> try:
...   int("3")
... except (ValueError, TypeError) as e:
...   print("exception handled")
... finally:
...   print("done")
...
3
done
>>>
```

