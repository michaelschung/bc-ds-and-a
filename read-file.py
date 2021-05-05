'''
Mr. Chung
3/17: Reading from a one-word-per-line file
'''

import random

n = 3
n_words = 50

######### READ FILE #########

words = []

with open('txt/short.txt', 'r') as f:
    for line in f:
        # Removes whitespace from ends of string
        stripped_line = line.strip()
        # Splits string into array of words
        line_words = stripped_line.split()
        # Add each line word to all_words
        words.extend(line_words)

######### CREATE MAP #########

map = {}

for i in range(len(words)):
    window_lst = []
    for j in range(n):
        window_lst.append(words[(i+j) % len(words)])

    next_word = words[(i+n) % len(words)]

    window = tuple(window_lst)

    if window in map:
        map[window].append(next_word)
    else:
        map[window] = [next_word]

# for key, val in map.items():
#     print(key, val)

######### GENERATE TEXT #########

print()

window = random.choice(list(map))

for word in window:
    print(word, end=' ')

for i in range(n_words - n):
    choices = map[window]
    next = random.choice(choices)
    window = (*window[1:], next)
    print(next, end=' ')

print('\n')
