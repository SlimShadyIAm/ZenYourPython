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
This is a double ended queue implementation that functions as a stack. Adding and removing items is O(1) in time complexity.

```py
from collections import deque
stack = deque()
stack.append("a")
item = stack.pop()
item_2 = stack.pop()
# IndexError: pop from an empty deque
```

## `Counter`
This is best explained with an example.

```py
>>> from collections import Counter
>>> pokemon_cards = Counter()
>>> new_cards = { 'charizard': 3, 'squirtle': 4 }
>>> pokemon_cards.update(new_cards)
>>> print(pokemon_cards)
Counter({'squirtle': 4, 'charizard': 3})

>>> new_cards = { 'charizard': 1, 'pikachu': 3 }
>>> pokemon_cards.update(new_cards)
Counter({'charizard': 4, 'squirtle': 4, 'pikachu': 3})
```