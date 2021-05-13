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
    from collections import Counter
    pokemon_cards = Counter()
    new_cards = { 'charizard': 3, 'squirtle': 4 }
    pokemon_cards.update(new_cards)
    print(pokemon_cards)
    new_cards = { 'charizard': 1, 'pikachu': 3 }
    pokemon_cards.update(new_cards)
    print(pokemon_cards)