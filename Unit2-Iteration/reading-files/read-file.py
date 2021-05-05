'''
Mr. Chung
3/17: Reading files
'''

import re

all_words = []

with open('words.txt', 'r') as f:
    for line in f:
        # Removes whitespace from ends of string
        stripped_line = line.strip()
        # Remove punctuation from the line
        no_punc = re.sub('[,.;!]', '', stripped_line)
        # Splits string into array of words
        line_words = no_punc.split()
        # Add each line word to all_words
        all_words.extend(line_words)

print(all_words)
