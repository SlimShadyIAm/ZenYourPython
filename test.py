from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

if __name__ == '__main__':
    from itertools import takewhile
    the_list = ["a", "b", "x", "y", "fin", "z"]
    print(list(takewhile(lambda x: x != "fin", the_list)))