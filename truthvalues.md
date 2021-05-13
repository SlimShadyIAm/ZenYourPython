# Truth values for conditions [Readbility, Programming Efficiency]
The following are part of the PEP 8 Python Style Guide, which gives some guidelines on the preferred way to write conditions for `if` statements.

## Comparing things to `True`
### Not pythonic
```py
something = True

if something == True:
    pass

if something is True:
    pass
```
### Pythonic
```py
if something:
    print("This is good!")

## for False:
something = False
if not something:
    print("Yay!")
```

## Comparing things to `None`
```py
something = None

if something == None:
    pass

# Also bad
if not something is None:
    pass

```
### Pythonic
```py
if something is None:
    print("This is good!")

if something is not None:
    print("Yay!")
```

## Checking for empty sequences (i.e strings, lists, tuples)
### Not pythonic
```py
some_list = []

if len(some_list) == 0:
    pass

if not len(some_list):
    pass

```

### Pythonic
```py
if some_list:
    print("This is good!")

if not some_list:
    print("Yay!")
```

## Unnecessary `ors`
### Unpythonic
```py
something = "Hello"
if something == "Hello" or something == "Hi" or something = "Hey":
    print("This is pretty noisy!")
```

```py
greetings = ["Hello", "Hi", "Hey"]
if something in greetings:
    print("Better!")

value = 3
if value in [1, 2, 3, 4, 5]:
    print("Good too!")
```
--- 

### References
[1] [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

#### Books that mention this topic:
[2] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[3] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[4] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
[5] *Writing Idiomatic Python 3* by Jeff Knupp  
[6] *The Little Book of Python Anti-Patterns* by QuantifiedCode  