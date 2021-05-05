'''
Mr. Chung
3/3: Human template class

Characteristics: name, hobbies, height, weight, emo_state, age

Actions/Experiences: birthday, grow, have_fun, try_new_thing, quarantine
'''

import random

class Human:
    # Constructor: set defaults, declare characteristics
    def __init__(self, name):
        self.name = name
        self.hobbies = []
        self.height = 53
        self.weight = 3
        self.emo_state = 'upset'
        self.age = 0

    def introduce(self):
        print('='*20)
        print('Hi, my name is', self.name)
        print('I am', self.age, 'years old.')
        print('I am currently', self.emo_state)
        print('My hobbies are:', self.hobbies)

    def birthday(self):
        self.age += 1
        self.grow()

    def grow(self):
        self.height += 2
        self.weight += 8

    def have_fun(self):
        self.emo_state = 'sad'

    def try_new_thing(self, new_thing):
        self.hobbies.append(new_thing)

    def talk_to(self, other_human):
        print(f'{self.name} says, "Hello, {other_human.name}!"')

    def quarantine(self):
        choice = random.randint(0, 1)
        if choice == 1:
            self.hobbies.append('bread baking')
            self.hobbies.append('dalgona coffee')
            self.hobbies.append('jigsaw puzzles')
        else:
            self.hobbies = []




#
