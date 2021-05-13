# Pythonic assignment
## Assigning the same value to multiple variables
This is a straightforward Python feature.

### Not pythonic
```py
a = 1
b = 1
```

### Pythonic
```py
a = b = 1

>>> print(a, b)
1 1
>>> b = 2
>>> print(a, b)
1 2
```

## Conditional assignment
A pythonic way to assign values to a variable when the value depends on a condition, or when one variable has the possibility of being `None`, an empty list or empty string.

### Not pythonic
```py
a = 1
b = 2 

if a != b:
    x = "Not equal"
else:
    x = "Equal"

c = None
if c is None:
    c = "Value"

```

### Pythonic
```py
x = "Equal" if a == b else "Not equal"

>>> print(x)
"Not equal"

c = None
d = "Value"
y = c or d

>>> print(y)
"Value"
```

## tuple and list unpacking
### What is this?
Tuple and list elements can be accessed using indexes as in lists, however Python supports unpacking, a much cleaner approach.

### Not pythonic
```py
person = ("Aamir", 21) # also works if this is a list
name = person[0]
age = person[1]
```

### Pythonic
This is not only more readable, but saves space as well.
```py
name, age = person
```

## catch-all unpacking
### What is this?
Also known as asterisk unpacking, this is a sort of pattern matching where you can access some elements of a list or tuple individually, and store the "rest" in a list. The syntax is similar to tuple unpacking. This is also a much cleaner approach as opposed to, for example, list slicing.

### Not pythonic
```py
some_numbers = [1, 2, 3, 4, 5]
fst = some_numbers[0]
# 1
snd = some_numbers[1]
# 2
rest = some_numbers[2:]
# [3, 4, 5]
```

### Pythonic
```py
fst, snd, *rest = some_numbers
print(fst, snd, *rest)
# 1 2 [3, 4, 5]

fst, *mid, last = some_numbers
print(fst, *mid, last)
# 1 [2, 3, 4] 5
```

## ignored variables
### What is this?
When unpacking a list or tuple, you may want to ignore certain elements and not store then. In Python, this is what the `_` variable is for. This variable is generally used as an "ignored" variable.

### Example
```py
fst, _, trd = (1, 2, 3)
# 2 is ignored 
```
```py
the_list = [(1,2,3), (4,5,6), (7.8,9)]
for x, _, z in the_list:
    print(x, z)
```

## Swapping two variables
Rather than using a temporary variable to swap values, Python has a simpler syntax to achieve the same result.
### Not pythonic
```py
a = 1
b = 2

# Swapping
temp = a
b = a
a = temp
```

### Pythonic
```py
a, b = b, a
```

Note that this can also work with more than 2 variables.

---

### References
[1] [PEP 308 -- Conditional Expressions](https://www.python.org/dev/peps/pep-0308/)
[2] [Python docs -- unpacking](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)  
[3] [PEP 3132 -- Extended Iterable Unpacking
](https://www.python.org/dev/peps/pep-3132/)  

#### Books that mention this topic
[4] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[5] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[6] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
[7] *Writing Idiomatic Python 3* by Jeff Knupp  
[8] *The Little Book of Python Anti-Patterns* by QuantifiedCode  