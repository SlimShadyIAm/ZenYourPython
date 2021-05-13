# `heapq`
### What is this?
A built-in priority queue implementation in Python

### Example
This example is taken from *Python Tricks* [2].

```py
import heapq
q = []
heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))

while q:
    next_item = heapq.heappop(q)
    print(next_item)
# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')```
```

### References
[1] [Python docs -- heapq](https://docs.python.org/3/library/heapq.html)

#### Books that mention this topic:
[2] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[3] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[4] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
