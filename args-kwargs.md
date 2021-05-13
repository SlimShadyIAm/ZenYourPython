# `*args` and `**kwargs` [Readability, Maintainability]
### What is this?

With this, it's possible to catch all the arguments and keyword-arguments passed into a function call and forward them into another function call. This is useful, for example, for flexible APIs with optional arguments, and calling constructors when subclassing a class from a third-party module. In the latter case, for example, it's possible that the API changes in a future update so rather than hardcoding the order of arguments, `*args*` and `**kwargs**` abstracts this for you.

### Example

```py
def some_function(*args, **kwargs):
    print(args)
    print(kwargs)

>>> some_function("hi", 1, key="sunny")
# ('hi', 1)
# {'key': 'sunny'}

class SomeClass(SuperClass):
    def __init__(something, something_else, *args, **kwargs):
        self.something = something
        self.something_else = something else

        super(*args, **kwargs)
```