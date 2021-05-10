# Decorators
### What is it?
These can be considered reusable wrappers around callables which can provide useful utilities such as logging, rate limiting, caching and timing, or changing the behavior of the code without modifying the code inside the callable itself.

Suppose we want to time every function in our code and output the execution times. Take the following example function:

```py
from time import sleep
from datetime import datetime

def some_stuff():
    before = datetime.now()
    
    something = []
    for i in range(10):
        something.append(i)
        sleep(0.1)
```

### Unpythonic
One approach would be to simply edit each function like so.

```py
def some_stuff():
    before = datetime.now()
    
    something = []
    for i in range(10):
        something.append(i)
        sleep(0.1)
        
    
    after = datetime.now()
    print(f"Function took {(after-before).total_seconds()} seconds.")
>>> "Function took 1.006231 seconds."
```

However, adding this code to every function can quickly become time consuming and tedious.

### Pythonic

```py
def timer(function):
  def new_function():
    start_time = datetime.now()
    function()
    elapsed = (datetime.now() - start_time).total_seconds()
    print(f'Function took {elapsed} seconds to complete.')
  return new_function

@timer
def some_stuff():
    something = []
    for i in range(10):
        something.append(i)
        sleep(0.1)
```

Now, we can simply add `@timer` in front of every function and calling the function will give us the timer output just as before.

### References
[1] [Python docs -- decorators](https://wiki.python.org/moin/PythonDecorators)
[2] [PEP 318 -- Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)

#### Books that mention this topic:
[4] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[5] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[6] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
