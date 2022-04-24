
# Creation

## Factory

- Used when the nature of object to be used is not clear
- Also during runtime we need to decide the type/nature of object to be created

***Implementation***

A sample factory which produce beings of different types, like Male and Woman

```commandline
>>> from factory_example import *
>>> m = get_being("man")
>>> m.walk()
Walking
>>> m.sex()
Male
>>> f = get_being("woman")
>>> f.sex()
Woman
>>> f.walk()
Walking
```

> Python is a ***dynamically typed language we could have implemented without inheritance*** but I did it to save coding.
> Note user of the factory method does not bother with Object creation process and different types.


## Abstract Factory

- Its build on factory pattern
- It deals with family of related object without bothering exact type

***Implementation***

We create Factory of being and there profession
    - Abstract Factory - Human
    - Concrete Factory - Man & Woman
    - Concrete Products - 
        - Man & Man Profession
        - Woman & Woman Profession

```commandline
>>> from abstract_factory_example import *
>>> h = HumanFactory(ManFactory())
>>> h.return_being_details("manly")
Name: Man - manly
Works: banking
>>> h = HumanFactory(WomanFactory())
>>> h.return_being_details("femalely")
Name: Man - femalely
Works: house making
```

## Singleton

It's the object-oriented way of creating Global variable, or process to create only a single object of a class.

***Implementation***

Create a Cache (Singleton Object) that can be accessed by different object and preserve and share states among them.


```commandline
>>> from singleton_example import *
>>> d1 = {"key1": "value1", "key2": "value2"}
>>> o1 = Singleton(d1)
>>> print(o1)
{'key1': 'value1', 'key2': 'value2'}
>>>
>>> d2 = {"key3": "value3"}
>>> o2 = Singleton(d2)
>>> print(o2)
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

```

## Builder

Solves the problem of creating a complex object which can be of large number of different types leading to large number of init function implementations.
Builder solves this by partitioning the object creation into sub steps (helpers) and use them to build the object. It doesn't rely on polymorphism for the object building.

It consists of the below:
    - Director is in charge of actual building the object
    - Abstract Builders are interfaces required in building process
    - Concrete Implementation of the Abstract Builders
    - Product is the actual object being build

```commandline
>>> from builder_example import *
>>> w1 = Builder()
>>> d1 = Director(w1)
>>> d1.construct_working_professional()
>>> print(d1.get_working_professional())
Sankar is male and good in IT

```

> As you can see by implementing a Concrete Builder you can handle the different type of object creation easily.


## Prototype

Cloning from a common template. Helps in individually creating large number of identical object separately.

***Implementation***

Use Abstruct Fractory pattern to build a typical object and then clone new objects from it when needed.