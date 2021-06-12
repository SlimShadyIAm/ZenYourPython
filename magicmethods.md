# Magic Methods (dunder methods) [Readability, Programming Efficiency]

### Detectors
- [Github.com](https://github.com/SlimShadyIAm/DetectYourZen/blob/main/src/main/scala/slim/NewMagicMethodsAnalysis.scala)

### What is it?
These are considered special methods used to override default behavior in Python that, as the docs describe, are invoked by special syntax (such as +, -, >, <) [1].

### Example
```py
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

>>> p1 = Person("Aamir", 21)
>>> p2 = Person("Abdullah", 20)
>>> p1 > p2
True
>>> p1 == p2
False
```

## `functools.total_ordering
This is a decorator which, by definining one of the ``__lt__()`, `__le__()`, `__gt__()`, or `__ge__()`, in addition to the `__eq__()` magic methods, it can implicitly define all of the remaining comparison magic methods. We can improve the above example...

```py
from functools import total_ordering

@total_ordering
class Person:
    ...
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

>>> p1 = Person("Aamir", 21)
>>> p2 = Person("Abdullah", 20)
>>> p1 > p2
True
>>> p1 <= p2 # We didn't explicitly define this behavior
False
```
### References
[1] [Python docs -- Special method names](https://docs.python.org/3.3/reference/datamodel.html#special-method-names)  
[2] [Python docs -- Special method names](https://docs.python.org/3.3/reference/datamodel.html#special-method-names)

#### Books that mention this topic:
[3] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[4] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  