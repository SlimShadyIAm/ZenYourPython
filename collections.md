# `collections` module

## `defaultdict`
A subclass of the `dict` class. It is instantiated with the desired default type of keys, such as `int`, `list`. It doesn't throw a `KeyError` when trying to access a non-existant key, instead it creates a new key with the supplied factory function.

### Example:
```py
>>> from collections import defaultdict
>>> people = defaultdict(list)
>>> people["American"].append("Nick")
>>> print(people["American"])
["Nick"]
>>> print(people["Dutch"])
[]
```

## `namedtuple`
`namedtuples` are like regular tuples where each attribute has a unique identifier, so you don't need to remember the indexes of elements.

```py
>>> from collections import namedtuple
>>> Person = namedtuple('Person', 'name age')
>>> p1 = Person("Aamir", 21)
>>> p1 
Person(name='Aamir', age=21)
```

## `deque`

## `counter`

