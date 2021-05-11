# `dicts`

## `dict.get()`
### What is this?
Normally one can access keys of a dict using the `dict["key"]` syntax, however if the key is nonexistent, it will throw a `KeyError` which if not appropriately handled, will crash the program.

### Not pythonic

```py
something = {'a': 1, 'b': 2}
if 'a' in something:
    print(something['a'])
something['c']
# KeyError as 'c' doesn't exist.
```

### Pythonic
Instead, what you can do is use the `.get()` method. This will simply return `None` if the key is not found and you no longer need to check if a key is in the dict beforehand.

```py
>>> print(something.get('a'))
1
>>> print(something.get('c'))
None
```

## collections.defaultdict

This is another improvement to the standard `dict` and is discussed in [collections](collections.md)

---

### References
[1] [Python docs -- `dict.get()`](https://docs.python.org/3/library/stdtypes.html#dict.get)

#### Books that mention this topic
[2] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[3] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[4] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
[5] *Writing Idiomatic Python 3* by Jeff Knupp  
[6] *The Little Book of Python Anti-Patterns* by QuantifiedCode  