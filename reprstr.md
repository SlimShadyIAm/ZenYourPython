# `__repr__` and `__str__` [Readability, Programming Efficiency]

### What is this?
Suppose we have the following class:
```py
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Not pythonic

Normally, when you try to `print()` an instance of the object, you would get the following output...

```py
>>> person = Person("Aamir", 21)
>>> person
<test.Person object at 0x7fa1fab83fa0>
```


..., which is obviously not very useful to us. 

### Pythonic
We would rather have some information about the object for debugging, such as...

```py
>>> person
"<Aamir, age 21>"
```
This is what the `__repr__` "magic method" is for, and according to  Dan Bader [3], every class should have this defined. The goal of `__repr__` is to create an easily identifiable representation for debugging. One may consider this analogous to the `toString()` method in Java.

This can be done by defining the behavior of `__repr__` as such:

```py
class Person():
    ... 
    def __repr__(self):
        return f"<{self.name}, age {self.age}>"
    
```

Similarly, we also have the `__str__` method, which has a similar approach, but the goal is to make the output readable.

```py
class Person():
    ...
    def __str__(self):
        return f"{self.name}, {self.age}"

```
We will now see the following output, and notice how the output is slightly different:
```py
>>> person
"<Aamir, age 21>"
>>> print(person)
"Aamir, 21"
```

?> The reason we say "every class should have `__repr__` defined is because if `__str__` is not defined, Python falls back to the implementation of `__repr__`.

### References
[1] [\_\_repr__ Official documentation](https://docs.python.org/3/library/functions.html#repr)  
[2] [\_\_str__ Official documentation](https://docs.python.org/3/library/stdtypes.html#str.format)
#### Books that mention this topic:
[3] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[4] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[5] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
[6] *Writing Idiomatic Python 3* by Jeff Knupp