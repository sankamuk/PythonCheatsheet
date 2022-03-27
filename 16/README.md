
## Numeric Type Revisited

- ***int***: Unlimited size, limited by only by memory
- ***float***: Basically 4 bytes or 64 bits (equivalent to double in Java) with
  - sign - 1 bit
  - exponent - 11 bits
  - fraction - 52 bits
  ```commandline
    >>> sys.float_info
    sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
    ```
  - The most important thing to understand though float rage in Python is fairly large but not all *int* can be mapped to *float* without loss of information

- Example 1 - Issue with float, cause of conversion of base 10 to base 2 for storage

```commandline
>>> a = 0.8
>>> b = 0.7
>>> a - b
0.10000000000000009

```

## Decimals

- Example 2 - Configuration

```commandline
>>> import decimal
>>> decimal.getcontext()
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

```

- Example 3 - Use of decimal in resolving issues with float

```commandline
>>> from decimal import Decimal
>>> a = Decimal('0.8')
>>> type(a)
<class 'decimal.Decimal'>
>>> a
Decimal('0.8')
>>> b = Decimal('0.7')
>>> a - b
Decimal('0.1')

```

> Note we used string with decimal constructor, else we may face the same problem with float, reason without string representation based construction decimal use same float internally

- Example 4 - Avoid pitfalls with Decimal

```commandline
>>> a = Decimal(0.8)
>>> b = Decimal(0.7)
>>> a - b
Decimal('0.1000000000000000888178419700')

```

- Example 5 - Precision maintenance and usage

```commandline
>>> decimal.getcontext().prec = 5
>>> c = Decimal('2.76878965')
>>> c
Decimal('2.76878965')
>>> c + 5
Decimal('7.7688')

>>> a = Decimal("5.00")
>>> a
Decimal('5.00')
>>> b = Decimal("5")
>>> b
Decimal('5')
>>> a + 2
Decimal('7.00')

```

- Example 6 - Special Values

```commandline
>>> Decimal('-Infinity')
Decimal('-Infinity')
>>> Decimal('Infinity')
Decimal('Infinity')
>>> Decimal('NaN')
Decimal('NaN')
>>>
>>> Decimal('Infinity') + 1
Decimal('Infinity')

```

- Example 7 - Tricky differences

```commandline
>>> -10 % 3
2
>>> Decimal("-10") % Decimal("3")
Decimal('-1')

>>> -7 // 3
-3
>>> Decimal("-7") // Decimal("3")
Decimal('-2')

>>> Decimal("-3") % Decimal("2")
Decimal('-1')
>>> -3 % 2
1
```

> None is wrong just they choose different implementation standards, so careful about specially negative computations

- Example 7 - Calling functions on decimals

```commandline
>>> Decimal("0.2").sqrt()
Decimal('0.44721')
>>> Decimal("0.2").log10()
Decimal('-0.69897')

```

## Fractions

- Example 8 - Explore fractions

```commandline
>>> from fractions import Fraction
>>> Fraction(2,4)
Fraction(1, 2)
>>> Fraction(2,4) + Fraction(1, 4)
Fraction(3, 4)
>>> Fraction("2/4")
Fraction(1, 2)
>>>
>>> from math import floor
>>> floor(Fraction("1/4"))
0

```

# Complex Number

- Example 9 - Explore complex

```commandline
>>> 5j
5j
>>> type(5j)
<class 'complex'>
>>> 2 + 4j
(2+4j)
>>> type(2 + 4j)
<class 'complex'>
>>> complex(1)
(1+0j)
>>> complex(1, 3)
(1+3j)
>>> complex('1+3j')
(1+3j)
>>> complex('1 + 3j')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: complex() arg is a malformed string
>>> complex('1+3j').real
1.0
>>> complex('1+3j').imag
3.0

```

- Example 10 - Dedicated module for complex functions, takes complex and return complex

```commandline
>>> import cmath
>>> cmath.sqrt(complex('1+3j'))
(1.442615274452683+1.0397782600555705j)

```

## Absolute Function

- Example 11 - Distance of the number from zero 

```commandline
>>> abs(2)
2
>>> abs(-2)
2
>>> abs(3.6)
3.6
>>> abs(Decimal('3.6'))
Decimal('3.6')

```

## Round Function

- Example 12 - Round method usage 

```commandline
>>> round(2.567, 1)
2.6
>>> round(2.567, 2)
2.57
>>> round(2.567, 5)
2.567
>>> round(2.5)
2
>>> round(1.5)
2
```

> Note rounds bias toward even number

## Different Base-d Number

- Example 13 - Binary, Octal & Hexa-Decimal

```commandline
>>> bin(5)
'0b101'
>>> 0b100
4
>>> oct(5)
'0o5'
>>> 0o10
8
>>> hex(12)
'0xc'
>>> 0xd
13

>>> hex(12)
'0xc'
>>> hex(12)[2:]
'c'

```

- Example 14 - Conversion to Binary, Octal & Hexa-Decimal

```commandline
>>> int(hex(12)[2:], base=16)
12
```

## Date Time

- Note datetime is a module with date, time, timedelta and also datetime(complex type with date and time together)
- It is an immutable object representation
- Date type helps in tracking (day, hour, month)
- Time type helps in tracking (hour, minute, second, microsecond) - with or without timezone
- Datetime is a combination of both above
- Timezone is represented by timezone with utcoffset function
- Timedelta is duration between time (days, seconds, microseconds)

***Note since datatime is module and class inside it, so while importing class datetime we should follow below convention***

```commandline
from datetime import datetime as Datetime
```

- Example 15 - Date usage

```commandline
>>> import datetime

>>> datetime.date.min
datetime.date(1, 1, 1)
>>> datetime.date.max
datetime.date(9999, 12, 31)
>>> datetime.date.resolution
datetime.timedelta(days=1)

>>> datetime.date(year=2022, month=1, day=1)
datetime.date(2022, 1, 1)
>>> datetime.date(2022, 1, 1)
datetime.date(2022, 1, 1)
>>> datetime.date.today()
datetime.date(2022, 3, 22)
>>> datetime.date.fromtimestamp(10000000000)
datetime.date(2286, 11, 20)
>>> datetime.date.fromordinal(1000)
datetime.date(3, 9, 27)
>>>
>>> adate = datetime.date(year=2022, month=1, day=1)
>>> adate.year
2022
>>> adate.month
1
>>> adate.day
1
>>> adate.weekday()
5
>>> adate.isoformat()
'2022-01-01'
>>> adate.strftime('%A %B')
'Saturday January'
>>> "Date: {:%A %B}".format(adate)
'Date: Saturday January'
```

- Example 16 - Time usage

```commandline
>>> datetime.time.min
datetime.time(0, 0)
>>> datetime.time.max
datetime.time(23, 59, 59, 999999)
>>> datetime.time.resolution
datetime.timedelta(microseconds=1)

>>> datetime.time(hour=2, minute=12, second=45, microsecond=555)
datetime.time(2, 12, 45, 555)
>>> datetime.time(2, 12, 45, 555)
datetime.time(2, 12, 45, 555)
>>>
>>>
>>> atime = datetime.time(hour=2, minute=12, second=45, microsecond=555)
>>> atime.isoformat()
'02:12:45.000555'
>>> atime.strftime('%H')
'02'
>>> "{h.hour}".format(h=atime)
'2'
```

- Example 17 - Datetime usage

```commandline
>>> datetime.datetime(2022, 4, 27, 11, 5, 40, 000000)
datetime.datetime(2022, 4, 27, 11, 5, 40)
>>> datetime.datetime.now()
datetime.datetime(2022, 3, 27, 11, 7, 56, 243545)
>>> datetime.datetime.today()
datetime.datetime(2022, 3, 27, 11, 8, 1, 163513)
>>> datetime.datetime.utcnow()
datetime.datetime(2022, 3, 27, 5, 38, 27, 155332)
>>> datetime.datetime.fromtimestamp(5789852)
datetime.datetime(1970, 3, 9, 5, 47, 32)
>>> datetime.datetime.utcfromtimestamp(5789852)
datetime.datetime(1970, 3, 9, 0, 17, 32)
>>> datetime.datetime.now().isoformat()
'2022-03-27T11:19:13.358859'


>>> dt = datetime.date.today()
>>> tm = datetime.time(11, 5, 40, 344544)
>>> dt
datetime.date(2022, 3, 27)
>>> tm
datetime.time(11, 5, 40, 344544)
>>> datetime.datetime.combine(dt, tm)
datetime.datetime(2022, 3, 27, 11, 5, 40, 344544)

>>> datetime.datetime.strptime("Tuesday 3 March 2022, 11:06:40", "%A %d %B %Y, %H:%M:%S")
datetime.datetime(2022, 3, 3, 11, 6, 40)

```

> Note `today` give no mention of timezone while `now` given zone of current machine
> Also check how we can combine date and time object intuitively into a datetime object


- Example 18 - Timedelta usage

> Note the constructor uses days, seconds, microseconds, milliseconds, minutes, hours, weeks but it `stores` only days, seconds and microseconds

```commandline
>>> datetime.timedelta(weeks=2, days=1)
datetime.timedelta(days=15)
>>> str(datetime.timedelta(weeks=2, days=1))
'15 days, 0:00:00'

>>> datetime.datetime.now() - datetime.timedelta(weeks=2)
datetime.datetime(2022, 3, 13, 11, 35, 13, 960338)
>>> str(datetime.datetime.now() - datetime.timedelta(weeks=2))
'2022-03-13 11:35:26.399742'
>>>
>>> str((datetime.datetime.now() - datetime.timedelta(weeks=2)) + datetime.timedelta(weeks=2))
'2022-03-27 11:36:42.783492'

```

- Example 19 - Timezone usage

```commandline
>>> ist = datetime.timezone(datetime.timedelta(hours=5, minutes=30), "IST")
>>> d1 = datetime.datetime(year=2022, month=3, day=27, hour=11, minute=45, second=10, tzinfo=ist)
>>> str(d1)
'2022-03-27 11:45:10+05:30'
>>> d2 = datetime.datetime(year=2022, month=3, day=27, hour=11, minute=45, second=10, tzinfo=datetime.timezone.utc)
>>> str(d2)
'2022-03-27 11:45:10+00:00'

```

