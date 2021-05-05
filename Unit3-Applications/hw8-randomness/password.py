'''
Mr. Chung
HW 8: Randomness
#1: Password
'''

import random

# Get 6 random lowercase letters
lLetters = 'abcdefghijklmnopqrstuvwxyz'
lower = random.sample(lLetters, 6)

# Get 2 random uppercase letters
uLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
upper = random.sample(uLetters, 2)

# Get 1 random digit
digits = '0123456789'
digit = random.sample(digits, 1)

# Get 1 random symbol
symbols = ',.?!@#$%^&*'
symbol = random.sample(symbols, 1)

# Combine lists
total = lower + upper + digit + symbol

# Randomize order within total
random.shuffle(total)

# Turn list into a single string
password = ''.join(total)
print(password)
