# Context Managers

### What is it?
Context managers in Python are a way of managing resources where we expressly need to do something before and after a block of code, and make sure this is done cleanly. An example is anything to do with I/O, such as writing to a file. First we need to open the file, do some stuff with it and then write to and close the file. This is a pattern where it is easy to forget to close the file, or an exception happens during the write operation in which case resources are not properly unallocated as the file doesn't get closed. Context managers can implicitly abstract this for you.

## `with`

One of the context managers is the `with` keyword. Let's continue with the example of writing to a file.

### Unpythonic
In the following situation, if there is an exception while writing, the file will not be closed as the `f.close()` line will not be reached by the interpreter.

```py
f = open('file.txt', 'w')
f.write("Hello, World!")
f.close()
```

### Pythonic
However in the following code, the file is closed regardless of what happens inside the indented block of code. 

```py
with open('file.txt', 'w') as f:
    f.write("Hello, World!")
```

Clearly, the second method is superior.

The behavior of what happens before and after the indented block can be defined by implementing the `__enter__` and `__exit__` methods (more details can be found in the docs). There is also the `contextlib` library which allows you to implement `with` support using a decorator and generator-iterator, which would be superior. An example of this is shown below.

## `finally`
Similar to `with`, `finally` is a block of code that is always run every time in a `try...except...finally` code block. This is useful for any cleanup that may need to be done. 

### Unpythonic
We continue with the I/O example from before, so we can use the same unpythonic code as before.

### Pythonic
Here is an example that makes use of both `with` and `finally`. The example comes from *Python Tricks: The Book* [5]. This is how we could implement our own `with` context manager.

```py
from contextlib import contextmanager

@contextmanager
    def managed_file(name):
        try:
            f = open(name, 'w')
            yield f
        finally:
            f.close()
>>> with managed_file('hello.txt') as f:
        f.write('hello, world!')
        f.write('bye now')
```

## References
[1] [Python docs -- context managers](https://docs.python.org/3/library/stdtypes.html#typecontextmanager)  
[2] [Python docs -- contextlib](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager)  
[3] [Python docs -- The try statement](https://docs.python.org/3/reference/compound_stmts.html#finally)  
[4] [PEP 343 -- The "with" Statement](https://www.python.org/dev/peps/pep-0343/)  

#### Books that mention this topic:
[5] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[6] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[7] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
[8] *Writing Idiomatic Python 3* by Jeff Knupp  
[9] *The Little Book of Python Anti-Patterns* by QuantifiedCode  