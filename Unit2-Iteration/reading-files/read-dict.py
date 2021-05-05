'''
Mr. Chung
3/17: Reading from a one-word-per-line file
'''

import re

words = []

with open('tswift.txt', 'r') as f:
    for line in f:
        # Removes whitespace from ends of string
        stripped_line = line.strip()
        # Remove punctuation from the line
        no_punc = re.sub("[,.;!?']", '', stripped_line)
        # Splits string into array of words
        line_words = no_punc.split()
        # Add each line word to all_words
        words.extend(line_words)

counts = {}

for word in words:
    # If we haven't seen the word before
    if word not in counts:
        # Add it to the dictionary with count 1
        counts[word] = 1
    # Otherwise (if we've already seen the word)
    else:
        # Bump the count by 1
        counts[word] += 1

print(counts)
