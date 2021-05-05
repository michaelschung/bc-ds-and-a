'''
Mr. Chung
4/19: Pratice with Randomness
'''

import random

# 1) Generate a random number between 100 and 999 that's divisible by 5
print(random.randrange(100, 1000, 5))

# 2) Generate a 6-digit one-time password (OTP)
print(random.randint(100000, 999999))
print(random.randrange(100000, 1000000))

# 3) Generate 100 random lottery ticket numbers (each 6-digits long), and then pick two tickets as winners
tickets = []
for i in range(100):
    tickets.append(random.randrange(100000, 1000000))
print(random.sample(tickets, 2))

# 4) Generate a random string of 5 letters
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = random.sample(alphabet, 5)
word = ''
for letter in letters:
    word += letter
print(word)

# Fancy Python way to turn list into string
letters2 = random.sample(alphabet, 5)
word2 = ''.join(letters2)
print(word2)
