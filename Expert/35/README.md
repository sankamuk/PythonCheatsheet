
# Python Library

## Numpy

- Writen in C which provide speed.
- Build to perform super fast computation with number.
- Mostly suited for vectorized computation.
- One drawback is since in Numpy numbers are more native and not objects like plain Python thus there is limitation in size (overflow will happen).

```
>>> import numpy as np
>>> vec1 = np.array(range(100000))
>>> type(vec1)
<class 'numpy.ndarray'>
```

## Numba

- Python loose lot of speed because it is interpreted and dynamically typed.
- Numba solves the issue by converting Python code into efficient machine code.

```python
>>> import numba
>>> @numba.jit
... def numba_multiply(a: int):
...   return a**a
...
>>> numba_multiply(2)
4
```

> Note numba is not part of standard library and need installation.
> Note type hint make Numba more efficient.
> Also do explore parallel execution feature of Numba.

