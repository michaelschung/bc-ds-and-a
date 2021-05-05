'''
Mr. Chung
4/7: Counting Letters
'''

words = []

with open('txt/tiny.txt', 'r') as f:
    for line in f:
        # Remove whitespace from the ends
        stripped_line = line.strip()
        # Split the line into a list of words
        line_words = stripped_line.split()
        # Add each word to our master list
        words.extend(line_words)

counts = {}

for word in words:
    # Loop through every letter in the word
    for letter in word:
        # If this letter has not been seen before
        if letter not in counts:
        # Put it into counts with value of 1
            counts[letter] = 1
        # Otherwise, bump current value up by 1
        else:
            counts[letter] += 1

print(counts)
