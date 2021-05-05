'''
Mr. Chung
4/7: Counting Bigrams
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

counts = {}

for i in range(len(words)-1):
    bigram = (words[i], words[i+1])
    if bigram not in counts:
        counts[bigram] = 1
    else:
        counts[bigram] += 1

print(counts)







#
