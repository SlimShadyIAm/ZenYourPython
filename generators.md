# Generators and generator expressions

## Generators
### What is this?
In some cases, as opposed to returning a list of items, a generator can be used as well. Generators are essentially a function that produces a sequence of items, aka an iterator. The reason we want this is because when building a list, you must allocate the memory and resources to produce the entire list when creating it. In some cases though we can get away with lazily building the list, and instead only building parts when we need it.

### Not pythonic
The following example comes from *Effective Python* [citation]. This piece of code finds the index of every word in a given input string. Notice that there is not only a lot oof visual noise that comes from needing to initialize and build the list, but also the fact that when this function is called, it needs to build the entire list before returning. If we want, say, the first 10 elements only, then we wasted resources unnecessarily to build the entire rest of the list.

```py
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            sleep(0.1)
            result.append(index + 1)
    return result
```

```py
>>> address = 'Four score and seven years ago...'
>>> result = index_words(address)
>>> print(result[:10])
[0, 5, 11, 15, 21, 27, 31, 35, 43, 51]
```

### Pythonic
A better approach is to use a generator here. When we call `next()`, we use the next `yield` statement.t6

```py
def index_words_iter(text):
    if text:
        sleep(0.1)
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            sleep(0.1)
            yield index + 1
```

Here is how we would use it in practice, or with a for loop.

```py
>>> it = index_words_iter(address)
>>> print(next(it))
0
>>> print(next(it))
5
```

If we time the two different functions, we notice that the generator expression is faster since it doesn't build the entire list before returning.

```py
    for _ in index_words(input_string):
        pass
    # Function took 6.917019 seconds to complete.

    for _ in index_words_iter(input_string):
        pass
    # Function took 1.1e-05 seconds to complete.
```

## Generator expressions
### What is this?

Similar to generators, this is a special syntax that can create a generator using the same syntax as a list comprehension. However as with generators, this is more efficient than a list comprehension as the entire list doesn't need to be built at runtime.

### Example

```py
>>> words = ["breathe", "sunflower", "rainbow", "three to the right", "four to the left"]
>>> capitals = (word.upper() for word in words)
>>> print(next(capitals))
"BREATHE"
>>> print(next(capitals))
"SUNFLOWER"
```

---

### References
[1] [PEP 255 -- Simple Generators](https://www.python.org/dev/peps/pep-0255/)
[2] [Python docs -- Generators](https://wiki.python.org/moin/Generators)
[3] [PEP 289 -- Generator Expressions](https://www.python.org/dev/peps/pep-0289/)
[3] [Python docs -- Generator Expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions)

#### Books that mention this topic
[4] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[5] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[6] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
[7] *Writing Idiomatic Python 3* by Jeff Knupp  
