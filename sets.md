# Sets
According to the Python docs, `sets` are a data structure that contains unordered elements with no duplicates. These are useful for easily ensuring there are no duplicates in a list of items as well as the various membership mathematical operations such as union, intersection, etc. Membership tests in sets are O(1) and subset operations should be O(n) [3].

## Set comprehension
This is already discussed in [comprehensions](comprehensions.md)

## Get rid of duplicate elements
This can be done very easily by turning the list into a set, as sets can only have unique elements. Beware though, that this operation does not preserve order.

```py
the_list = [1, 2, 2, 1, 2, 3, 4, 2, 3, 6, 2]
set(the_list)
>>> {1, 2, 3, 4, 6}
```

## Loops
As was described in [for-loops](forloops.md), for-loops can be made more efficient by using a set in the case of a large list where there may be many duplicate elements. 

If we don't want to process the same element more than one time, sets can come in handy. 

```py
the_list = [1, 2, 2, 1, 2, 3, 4, 2, 3, 6, 2]
the_sum = 0

for x in set(the_list):
    the_sum += x

print(the_sum)
>>> 16

```

## Set operations
Another advantage of sets are the mathematical operations. These include, but are not limited to union, intersect and differences. This could be useful, for example, in the context of comparing two dictionaries. The keys of dictionaries are sets. The following example is from *Python Cookbook* [4]

```py
a = {
'x' : 1,
'y' : 2,
'z' : 3
}

b = {
'w' : 10,
'x' : 11,
'y' : 2
}

# Find keys in common
a.keys() & b.keys()
>>> { 'x', 'y' }

# Find keys in a that are not in b
a.keys() - b.keys()
>>> { 'z' }

# Find (key,value) pairs in common
a.items() & b.items() 
>>> { ('y', 2) }
```

## References
[1] [Python docs -- sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
[2] [PEP 218 -- Adding a Built-In Set Object Type
](https://www.python.org/dev/peps/pep-0218/)

### Books that mention sets:
[3] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[4] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
[5] *Writing Idiomatic Python 3* by Jeff Knupp  
