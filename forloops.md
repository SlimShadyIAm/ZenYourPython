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

If you need the indexes of the items as well as the item itself, then you should use [`enumerate`](/for/enumerate.md)

?> Note: if you have a large array which may contain duplicate values, then QuantifiedCode claims that it would be more efficient to turn the `list` into a `set` [5], the reasons for which are described better in [set](/set.md).

### References 
#### Books that mention this topic:

[1] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[2] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[3] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
[4] *Writing Idiomatic Python 3* by Jeff Knupp  
[5] *The Little Book of Python Anti-Patterns* by QuantifiedCode  