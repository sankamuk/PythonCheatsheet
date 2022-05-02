
# Behavioural

## Observer Pattern

Map cases where there is a Subject and multiple Observers. Note the nature of Subject to Observer relationship is One-Many.

***Implementation***

A subject need to be monitored and observer need to be notified once there is a change in subject's property.
- Subject is an Abstract Class with interfaces of attach, detach and notify along others.
- Concrete implementation of the Abstract subject.

```commandline
>>> from observer_example import *
>>> o1 = Core("Object 1")
>>> t1 = Observer("Observer-1")
>>> t2 = Observer("Observer-2")
>>> o1.attach(t1)
>>> o1.attach(t2)
>>> o1.trait = 22
Observer -> Observer-1, Viewed -> Core<Object 1>
Observer -> Observer-2, Viewed -> Core<Object 1>

```

## Visitor

Allow adding new feature to class without changing it.

***Implementation***

Allow new operations on the class attributes without modification of existing implementation.
- There will be a Class (Host) which will be visited (and add functionality).
- Then there will be actual visitors' (Visitor) implementation of different type.
- With this Host can host visitors of different type.

```commandline
>>> from visitor_example import *
>>> v1 = Visitor1("Vistor 1")
>>> v2 = Visitor2("Vistor 2")
>>> h = Host("Host")
>>> h.host(v1)
Host -> Host<Host>, Visitor -> Visitor<Vistor 1>
>>> h.host(v2)
Host -> Host<Host>, Visitor -> Visitor<Vistor 2>
```

## Iterator

Allow clients to have sequential access to attribute of an object without exposing the complete object. It internally keeps track of objects traversed.
Composite design pattern is related to iterators.

***Implementation***

We create a day of the week generator.

```commandline
>>> from iterator_example import *
>>> for d in day_counter(3):
...   print(d)
...
Monday
Tuesday
Wednesday
>>> for d in day_counter(6):
...   print(d)
...
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
```

> The simplicity of the implementation is due to the fact Python provides build in version.

## Strategy

It targets problem when you want the behaviour (member function) to vary based on context.

***Implementation***

We implement a Strategy implementation that allow us to change behaviour.

```commandline
>>> from strategy_example import *
>>> o1 = ChangeBehaviour("Object 1")
>>> o1.execute()
Default behaviour for object - Object 1
>>>
>>> o2 = ChangeBehaviour("Object 2", behaviour_type_1)
>>> o2.execute()
Type 1 behaviour for object - Object 2
>>>
>>> o3 = ChangeBehaviour("Object 3", behaviour_type_2)
>>> o3.execute()
Type 2 behaviour for object - Object 3
```

> Again the simplicity is due to feature rich Python language

## Chain of Responsibility

Decouple request and its processing. Various type of processing can be chained based on the request. Composite pattern implementation is related to this.

***Implementation***

We build a processing chain with specific processing for specific number range. Every point of chain pass processing to next task if it cannot handle.

```commandline
>>> from chain_responsibility_example import *
>>> c = Implementation1(Implementation2(None))
>>> c.handle_request(30)
Request less than 50 but more than 10, thus Implementation2 handles request
>>> c.handle_request(9)
Request less than 10, thus Implementation1 handles request

```
