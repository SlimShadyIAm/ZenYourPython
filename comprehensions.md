# Comprehensions

### What is it?
In Python, comprehensions are a block of code that can generate a sequence or filter/apply an operation to an existing sequence. These are considered pythonic, as opposed to using for loops to generate lists. Comprehensions are preferred over for-loops and `map`/`filter`, where possible and feasible. There are 3 types of comprehensions. 

## List comprehension

### Not pythonic
Here is a piece of code that takes a list of numbers and filters out odd numbers. 

```py
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

>>> [2, 4, 6]
```

While this may be accepted in other languages, in Python this is considered not pythonic. There is a more concise way to do this.

### Pythonic


```py
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [ num for num in numbers if num % 2 == 0 ]

>>> [2, 4, 6]
```

The list comprehension saved ~3 lines of code in this context, and it is also more readable and concise. We could also do this in-place if we wanted to (i.e not create a separate even_numbers variable).

In fact, if we make the input size bigger we notice that list comprehension is faster as well.

```py
@timer
def unpythonic_function():
    numbers = range(100000000)
    even = []
    
    for num in numbers:
        if num % 2 == 0:
            even.append(num)

    return even

>>> "Function 'unpythonic_function' took 6.257403173000057 seconds to complete."

@timer
def pythonic_function():
    numbers = range(100000000)
    even = [ num for num in numbers if num % 2 == 0 ]

    return even

>>> "Function 'pythonic_function' took 5.190925324001 seconds to complete."
```

Here is another example where we want to square every number in a list.

```py
# Unpythonic
numbers = [1, 2, 3, 4, 5, 6]
numbers_squared = []

for num in numbers:
    numbers_squared.append(num**2)

# pythonic
numbers_squared = [num**2 for num in numbers]

```

## Dict comprehension

This is similar to list comprehensions, except the data structure is a dict. The syntax is familiar as well.

```py
numbers_squared = { x: x**2 for x in numbers }
```

## Set comprehension
This is also similar to list comprehensions, except the resulting data structure is a set. The advantage of sets is the [set operations](sets.md) as well as the property that sets can only have unique elements.

```py
numbers_squared = { x**2 for x in numbers }
```
[1] [PEP 202 -- List Comprehensions](https://www.python.org/dev/peps/pep-0202/)
[2] [Python docs -- List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
[3] [PEP 274 -- Dict Comprehensions](https://www.python.org/dev/peps/pep-0274/)
[4] [Python docs -- Dict Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
[5] [Python docs -- Set Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

## References

### Books that mention this topic:
[6] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[7] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[8] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
[9] *Writing Idiomatic Python 3* by Jeff Knupp  
[10] *The Little Book of Python Anti-Patterns* by QuantifiedCode  