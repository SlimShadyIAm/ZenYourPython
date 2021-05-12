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
---

### References
