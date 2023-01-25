
# Parallelism & Concurrency

- Python support 3 different mechanism:
  - Thread
  - Process
  - AsyncIO

- Thread: Multiple execution sequence sharing same memory space (e.g.: Global Values). 
  - Remember all Python data structure are not thread safe, i.e. update from multiple thread can give Nondeterministic results
  - Now Python (because of Global Interpreter Lock, GIL) can use only one physical core thus with Thread-ing you only get advantage if IO bound actions performed
- Process: Multiple execution with complete different PCB (Process Control Block). Thus, it is heavy and share nothing.
  - As process are different PCB controlled you can use multiple physical cores, good for CPU bound process.
  - Since process does not share anything thus communication is expensive as serialization is added in picture.
- AsyncIO: Very dedicated for spanning large connections.
  - To use these feature you need dedicated driver for that connection.

## Thread

- Pythons concurrent.futures module is the process to go ahead if you think to use Threads.

```python
>>> import json
>>> import requests
>>> from concurrent.futures import ThreadPoolExecutor
>>>
>>> def get_time(continent, city):
...   return (json.loads(requests.get("http://worldtimeapi.org/api/timezone/{}/{}".format(continent, city)).content))['datetime']
...
>>> get_time("Asia", "Kolkata")
'2023-01-24T13:57:55.191068+05:30'
>>>
>>> with ThreadPoolExecutor() as pool:
...   print(list(pool.map(get_time, ["Asia", "Asia"], ["Kolkata", "Dhaka"])))
...
['2023-01-24T14:06:33.257031+05:30', '2023-01-24T14:36:33.256196+06:00']
```

> Note this goes deep so look in the module documentation to explore it fully.


## Process

- Note process based execution to achieve parallelism is great, but overhead for IPC(Inter Process Communication) is the biggest consideration.

```python
>>> from concurrent.futures import ProcessPoolExecutor
>>> with ProcessPoolExecutor() as pool:
...   print(list(pool.map(get_time, ["Asia", "Asia"], ["Kolkata", "Dhaka"])))
['2023-01-24T14:06:33.257031+05:30', '2023-01-24T14:36:33.256196+06:00']
```

## AsyncIO

