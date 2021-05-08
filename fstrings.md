# f-strings and string formatting

### What is this?
We need a way to dynamically combine data from variables and other data structures into a readable string output, or in other words, string interpolation. In Python, the preferred way, according to Brett Slatkin [4] (as of Python 3.6) is to use f-strings. Another option is the `str.format()` method.

### Not Pythonic
This is considered the old "C-style" method of formatting strings. A Pythonic developer should not use this approach.

```py
animal_one = "fox"
animal_two = "dog"

print("The quick brown %s jumped over the lazy sleeping %s" % (animal_one, animal_two))
```

### Pythonic
The following string interpolation method is more readable and more maintainable, as you don't need to compare the order of variables in a tuple -- you can simply read it.
```py
print(f"The quick brown {animal_one} jumped over the lazy sleeping {animal_two}")
```

Expressions can also be evaluated inside the brackets.

```py
print(f"1+2 is {1+2}")
```

Another option is the `str.format()` method. Through this, it is possible to create a reusable template string and format different data into it. 

```py
the_string = "The quick brown {one} jumped over the lazy sleeping {two}"

print(the_string.format(one=animal_one, two=animal_two))
print(the_string.format(one="monkey", two="cow"))
print("{0} is {1}".format("foo", "bar"))
```

### References
[1] [PEP 498 -- Literal String Interpolation ](https://www.python.org/dev/peps/pep-0498/)  
[2] [PEP 3101 -- Advanced String Formatting](https://www.python.org/dev/peps/pep-3101/)  
[3] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[4] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin