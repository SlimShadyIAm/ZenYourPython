# Magic Methods (dunder methods)

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

### References
[1] [Python docs -- Special method names](https://docs.python.org/3.3/reference/datamodel.html#special-method-names)  
[2] [Python docs -- Special method names](https://docs.python.org/3.3/reference/datamodel.html#special-method-names)

#### Books that mention this topic:
[3] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[4] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  