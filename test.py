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
    p1 = Person("Aamir", 21)
    p2 = Person("Abdullah", 20)
    
    print(p1 > p2)
    print(p1 <= p2)