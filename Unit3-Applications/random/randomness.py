'''
Mr. Chung
4/19: Using randomness
'''

import random

# =====Integer values=====
# Random int in range [0, stop)
print(random.randrange(10))
# Random int in range [start, stop)
print(random.randrange(5, 10))
# Random int in range [start, stop, step)
print(random.randrange(10, 20, 2))

# Random int in range [start, stop]
print(random.randint(15, 20))

# =====Real values=====
# Random float in range [0.0, 1.0)
print(random.random())
# Random float in range [0.0, 10.0)
print(random.random() * 10)

# =====Random values from sequences=====
lst = ['hello', 'goodbye', 'water', 'bottle', 'cork']
word = 'november'

print(random.choice(lst))
print(random.choice(word))

print(random.sample(lst, 3))
print(random.sample(word, 2))

random.shuffle(lst)
print(lst)
