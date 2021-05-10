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
    start_time = timeit.default_timer()
    function()
    elapsed = timeit.default_timer() - start_time
    print('Function "{name}" took {time} seconds to complete.'.format(name=function.__name__, time=elapsed))
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

if __name__ == '__main__':
    unpythonic_function()
    pythonic_function()