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

for i in range(len(words)-2):
    bigram = (words[i], words[i+1])
    next_word = words[i+2]
    if bigram not in counts:
        counts[bigram] = [next_word]
    else:
        counts[bigram].append(next_word)

for key in counts:
    print('{}: {}'.format(key, counts[key]))
