'''
Mr. Chung
3/3: Putting Humans on a list
'''

from human import Human

names = ['Lauren', 'Weezie', 'Shreya', 'Chris', 'Johnny']
humans = []

for i in range(5):
    name = names[i]
    humans.append(Human(name))

for h in humans:
    h.introduce()
