class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"<{self.name}, age {self.age}>"
    
    def __str__(self):
        return f"{self.name}, {self.age}"
    
if __name__ == '__main__':
    person = Person("Aamir", 21)
    print(person)