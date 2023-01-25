
# Improved Datastructures 

## Bisect

- Binary Search, allows searching element in a `sorted` list in O(log(n)) complexity.

```python
>>> import bisect
>>> l1 = [2, 7, 3, 11, 10]
>>> sorted(l1)
[2, 3, 7, 10, 11]
>>> bisect.bisect(sorted(l1), 9)
3
```

> As you see bisect find the location where you need to insert new element to keep the final list still sorted.

- If you just want to search element then you use bisect accordingly.

```python
>>> True if sorted(l1)[bisect.bisect(sorted(l1), 3)-1] == 22 else False
False
>>> True if sorted(l1)[bisect.bisect(sorted(l1), 3)-1] == 3 else False
True
```

## Deque

- First in first out structure. But Python's implementation in deque is of a double ended queue.

```python
>>> from collections import deque
>>> dq = deque()
>>> dq.append(3)
>>> dq.append(9)
>>> dq.popleft()
3
>>> dq.popleft()
9
>>> dq
deque([])
```

> Note Python list is optimized for append and remove from end. i.e. `STACK` structure. Deque implements queue.
> Note deque could have item access time compromised for FIFO optimization.

## Heapq

- Priority Queue. Python's implementation would be using `HEAP`. Note priority should be numerical sorted in descending.

```python
>>> from heapq import heappush, heappop
>>> hp = []
>>> heappush(hp, 51)
>>> heappush(hp, 2)
>>> heappush(hp, 33)
>>> heappush(hp, 33)
>>> heappush(hp, 19)
>>> print(hp)
[2, 19, 33, 51, 33]
>>> print(heappop(hp))
2
>>> print(heappop(hp))
19
>>> print(heappop(hp))
33
```

> When you print the list you do not see list to be sorted. 
> What might make you mad the list is not even preserving insert order.
> The order is actually representing heap in flattened state.


