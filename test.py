class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"<{self.name}, age {self.age}>"
    
    def __str__(self):
        return f"{self.name}, {self.age}"

import timeit

def timer(function):
  def new_function():
    start_time = datetime.now()
    function()
    elapsed = (datetime.now() - start_time).total_seconds()
    print(f'Function took {elapsed} seconds to complete.')
  return new_function
    
@timer
def unpythonic_function():
    numbers = range(100000000)
    even = []
    
    for num in numbers:
        if num % 2 == 0:
            even.append(num)

    return even

@timer
def pythonic_function():
    numbers = range(100000000)
    even = [ num for num in numbers if num % 2 == 0 ]

    return even

from time import sleep
from datetime import datetime

@timer
def some_stuff():
    something = []
    for i in range(10):
        something.append(i)
        sleep(0.1)

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

if __name__ == '__main__':
    names = ["Aamir", "Adarsh", "Abdullah", "Frans"]
    ages = [21, 20, 19, 21]

    for i in range(len(names)):
        print(f"{names[i]}, age {ages[i]}")