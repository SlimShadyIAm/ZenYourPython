# Pythonic `for` loops

## for loops

### What is this?
If you're coming from another programming language, you may be used to using indexes to loop through an iterable such as an array. In Java, for example:

```java
for (int i = 0; i < items.length; i++) {
    System.out.println(items[i]);
}
```

### Not pythonic
A new Python programmer may be inclined to use the same approach in Python, as follows:

```py
for i in range(len(items)):
    print(items[i])
```

### Pythonic
However, the above approach is not pythonic! In Python, one should use the following approach, which is cleaner and more readable!

```py
for item in items:
    print(item)
```

If you need the indexes of the items as well as the item itself, then you should use `enumerate`, as explained below.

?> Note: if you have a large array which may contain duplicate values, then QuantifiedCode claims that it would be more efficient to turn the `list` into a `set` [5], the reasons for which are described better in [set](/set.md).

## enumerate
### What is this?
The way of looping through iterables as explained in [for-loops](forloops.md) doesn't give you a way to get the indexes of the elements. The `enumerate` function turns a list of objects into a list of tuples, with the first element being the index and the second being the object itself.

### Not pythonic
```py
leaderboard = ["Aamir", "Abdullah", "Adarsh", "Frans", "Vadim"]
for i in range(len(leaderboard)):
    print(f"{i+1}. {leaderboard[i]}")

# Output
## 1. Aamir
## 2. Abdullah
## 3. Adarsh
## 4. Frans
## 5. Vadim
```

### Pythonic
This is a much more concise way to write the same for-loop.
```py
for i, name in enumerate(leaderboard):
    print(f"{i+1}. {name}")
```

### References
[1] [Python docs -- enumerate](https://docs.python.org/3/library/functions.html#enumerate)  
[2] [PEP 279 -- The enumerate() built-in function](https://www.python.org/dev/peps/pep-0279/)  
#### Books that mention this topic:
[3] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[4] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[5] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
[6] *Writing Idiomatic Python 3* by Jeff Knupp  
[7] *The Little Book of Python Anti-Patterns* by QuantifiedCode  