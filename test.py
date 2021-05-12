from datetime import datetime
from time import sleep 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not 0 < new_age < 120:
            raise ValueError("Invalid age.")
        
        self._age = new_age
                        

def index_words_iter(text):
    if text:
        sleep(0.1)
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            sleep(0.1)
            yield index + 1

if __name__ == '__main__':
    p = Person("aamir", -1)
    # ValueError: Invalid age.
    p2 = Person("Adarsh", 20)
    p2.age = -1
    # ValueError: Invalid age.    