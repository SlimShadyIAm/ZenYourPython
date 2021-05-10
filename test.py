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

if __name__ == '__main__':
    # the_list = [1, 2, 2, 1, 2, 3, 4, 2, 3, 6, 2]
    # the_sum = 0

    # for x in set(the_list):
    #     the_sum += x

    # print(the_sum)
    some_stuff()