'''
Mr. Chung
4/5: Turn a file into a list of words
'''

words = []

with open('txt/tswift.txt', 'r') as f:
    for line in f:
        # Remove whitespace from the ends
        stripped_line = line.strip()
        # Split the line into a list of words
        line_words = stripped_line.split()
        # Add each word to our master list
        words.extend(line_words)

print(words)
