# Special class decorations [Readability]

### A brief introduction
Normally, methods in classes, known as *instance methods*, implicitly receive the instance of the class (`self`) as the first argument. You will be familiar with the following syntax:

```py
def some_method(self, arg1, arg2):
    raise NotImplementedError
```

## `@classmethod`
### What is this?
This is a decorator that when added to a method in a class, it turns the method into a *class method*. That is, instead of receiving an *instance* of the class (`self`) as the implicit first argument, it receives the class itself.

### Example
This example comes from the Python docs [1].

```py
class C:
    @classmethod
    def f(cls, arg1, arg2, ...): ...
    ...

    C.f() # does something
```

## `@staticmethod`
### What is this?
This is a decorator that when added to a method in a class, it turns the method into a *static method*. That is, it doesn't receive any implicit first argument.

### Example
```py
class D:
    @staticmethod
    def f(arg1, arg2, ...): ...
    ...

    D.f() # does something
```

## `@property`
### What is this?
This is a pythonic way of adding getters and setters to a class. Note that where possible, it is preferred to use plain attributes over getters and setters. As *Anti-Idioms* says, Python is not Java [7]. Regardless, it may be necessary in some places to avoid adding checks in the wrong places or repetitive code, for example.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not 0 < new_age < 120:
            raise ValueError("Invalid age.")
        
        self._age = new_age

>>> p = Person("aamir", -1)
ValueError: Invalid age.

>>> p2 = Person("Adarsh", 20)
>>> p2.age = 121
ValueError: Invalid age.    
```

---

### References
[1] [Python docs -- classmethod](https://docs.python.org/3/library/functions.html#classmethod)
[2] [Python docs -- staticmethod](https://docs.python.org/3/library/functions.html#staticmethod)
[3] [Python docs -- property](https://docs.python.org/3/library/functions.html#property)

#### Books that mention this topic
[4] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[5] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[6] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones    
[7] *The Little Book of Python Anti-Patterns* by QuantifiedCode  