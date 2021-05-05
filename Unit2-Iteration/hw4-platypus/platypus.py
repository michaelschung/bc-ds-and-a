'''
Mr. Chung
3/8: Frankenstein's Platypus
'''

class Platypus:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.fur = 'brown'
        self.parts = []
        self.height = 3     # cm
        self.weight = 0.2   # lbs
        self.length = 10    # cm

    def report(self):
        print(f'name   = {self.name}')
        print(f'age    = {self.age} years old')
        print(f'fur    = {self.fur}')
        print(f'parts  = {self.parts}')
        print(f'length = {self.length} cm')

    def birthday(self):
        if self.age < 1:
            self.grow()
        self.age += 1

    def grow(self):
        self.height += 38
        self.weight += 1.5
        self.length += 35

    def fur_color(self, new_color):
        self.fur = new_color
