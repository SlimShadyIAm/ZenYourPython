# List slicing [Readability]
### What is this?
This is how to interface with a sequence in order to access subsets of the sequence. This would work, for example, on lists, strings or classes that have implemented `__getitem__` and `__setitem__`. Knowing how to use this operation can be very powerful and useful and can prevent using unnecessary for loops.

### Examples
```py
items = [1, 2, 3, 4, 5, 6, 7]

>>> items[:]
[1, 2, 3, 4, 5, 6, 7] # all items in the list
>>> items[5:] # from the 5th index onwards
[6, 7]
>>> items[:2] # everything up till the 2nd index
[1, 2]
>>> items[:-1] # everything except the last element
[1, 2, 3, 4, 5, 6]
>>> items[-4:-1] # the last 3 elements except for the final one
[4, 5, 6]
>>> items[-3:] # the last 3 elements
[5, 6, 7]
```

### References
[1] [Python docs -- Lists](https://docs.python.org/3/tutorial/introduction.html#lists)  
[2] [PEP 204 -- Range Literals](https://www.python.org/dev/peps/pep-0204/)  

#### Books that mention this topic:
[3] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[4] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[5] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
[6] *Writing Idiomatic Python 3* by Jeff Knupp 