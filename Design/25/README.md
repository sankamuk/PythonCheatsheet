# Structural 

## Decorator

Allows addition of features to object without changing structure. In Python its easy as the language supports decorator.

***Implementation***

We will add feature to a function using decorator. Note functions are also objet in Python.

```commandline
>>> from decorator_example import *
>>> greet()
'Hello sankar!'

```

## Proxy

Mostly used to create highly resource intensive object. In such cases we lazily defer the actual creation when it's invoked until that time use a proxy.

***Implementation***

We replicate a DB Handler who handles DB calls, it's a heavy object as it set up connection before performing action. We postpone its existence until required.

```commandline
>>> from proxy_example import *
>>> p = ProxyHandler()
>>> if not p.check_state():
...   p.wait_now()
...   p.change_state()
...
Handler is busy!
>>> if p.check_state():
...   p.perform_action()
...
Performing action
```

## Adapter

It converts the interface of a class to something client knows/expecting. Help in handing incompatibility issues.

***Implementation***

Our adapter addition method needs number to be added mathematically while concatenation(add) strings.

```commandline
>>> from adapter_example import *
>>> numadd = NumberAdd()
>>> adapter = Adapter(numadd, add=numadd.add_number)
>>> adapter.add(1, 2)
3
>>> stradd = StringAdd()
>>> adapter = Adapter(stradd, add=stradd.add_string)
>>> adapter.add("1", "2")
'12'
```

## Composite

Tree maintain got represent part-whole relationship. Helps in building element have sub element and so on, recursive structure.

***Implementation***

Menu with Sub Menu, which have Sub Menus and so on.

```commandline
>>> from composit_example import *
>>> sm1 = Composite("Sub Menu 1")
>>> sm1ch1 = Child("Sub Menu 1 - Child 1")
>>> sm1ch2 = Child("Sub Menu 1 - Child 2")
>>> sm1.add_child(sm1ch1)
>>> sm1.add_child(sm1ch2)
>>> m1 = Composite("Menu 1")
>>> m1ch1 = Child("Menu 1 - Child 1")
>>> m1.add_child(m1ch1)
>>> m1.add_child(sm1)
>>> m1.item_function()
Name - Menu 1
Name - Menu 1 - Child 1
Name - Sub Menu 1
Name - Sub Menu 1 - Child 1
Name - Sub Menu 1 - Child 2
```

## Bridge

It helps in mixing Implementation specific and Non Implementation specific requirement.

***Implementation***

Lets create human with Man specific and Woman specific walks.

```commandline
>>> from bridge_adapter import *
>>> h = Human("Sankar", ManAction())
>>> h.whoami()
Sankar
>>> h.walk()
Walking Man
>>> s = Human("Female", WomanAction())
>>> s.whoami()
Female
>>> s.walk()
Walking Woman
```

