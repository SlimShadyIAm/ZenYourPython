# `itertools` [Readability, Programming Efficiency, Performance]

### Detectors
- [Github.com](https://github.com/SlimShadyIAm/DetectYourZen/blob/main/src/main/scala/slim/NewDecoratorAnalysis.scala)

### What is this?
This is a built-in module with a lot of useful methods to interface with iterables, which not only improves readability but can improve performance too.

Here are some examples of the built-in functions. More can be found in the docs [1].

### `zip_longest`
With the built-in `zip` command, when one list is longer than the other and the inputs are exhausted, the rest of the elements in the longer list are discarded. `ziplongest` can fill in the elements in the shorter list with either `None` or a specified default value.

```py
list_1 = [1, 2, 3]
list_2 = [4, 5, 6, 7]
print(list(zip(list_1, list_2)))
# [(1, 4), (2, 5), (3, 6)]

from itertools import zip_longest
print(list(zip_longest(list_1, list_2, fillvalue=-1)))
# [(1, 4), (2, 5), (3, 6), (-1, 7)]
```

### `cycle`
This repeats a given iterator's items forever, using a generator.

```py
from itertools import cycle
cycler = cycle(["a", "b"])
print([next(cycler) for _ in range(5)])
# ['a', 'b', 'a', 'b', 'a']
```

### `takewhile`
Return items from an iterator until a given condition evaluates to `False`.

```py
from itertools import takewhile
the_list = ["a", "b", "x", "y", "fin", "z"]
print(list(takewhile(lambda x: x != "fin", the_list)))
```

### References
[1] [Python docs -- itertools](https://docs.python.org/3/library/itertools.html)

#### Books that mention this topic:
[2] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[3] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
[4] *Writing Idiomatic Python 3* by Jeff Knupp  
