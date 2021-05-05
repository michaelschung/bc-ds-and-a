'''
Mr. Chung
4/7: Counting Unigrams
'''

words = []

with open('txt/small1.txt', 'r') as f:
    for line in f:
        # Remove whitespace from the ends
        stripped_line = line.strip()
        # Split the line into a list of words
        line_words = stripped_line.split()
        # Add each word to our master list
        words.extend(line_words)

counts = {}

for word in words:
    # If the word hasn't been seen before,
    if word not in counts:
    # Put it into counts with a value of 1
        counts[word] = 1
    # Otherwise, if we have seen the word,
    else:
    # Bump up the current count by 1
        counts[word] += 1

print(counts)
# {'to': 3, 'be': 4, 'or': 2, 'not': 2, 'just': 1, 'who': 1, 'you': 2, 'want': 2, 'okay': 2}
