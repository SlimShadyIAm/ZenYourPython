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

## zip
### What is this?
This function takes iterables as input and returns a tuple with an element from each of the objects. This is useful for looping through lists in parallel.

### Unpythonic
```py
names = ["Aamir", "Adarsh", "Abdullah", "Frans"]
ages = [21, 20, 19, 21]

for i in range(len(names)):
    print(f"{names[i]}, age {ages[i]}")

# Output
## Aamir, age 21
## Adarsh, age 20
## Abdullah, age 19
## Frans, age 21

```

### Pythonic
The advantage of using `zip` over the "unpythonic" approach is that, in addition to the syntax being cleaner, it also handles the case where one list is longer than the other. In this case it exhausts the shortest list and then simply terminates.


```py
for name, age in zip(names, ages):
    print(f"{name}, age {age}")
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