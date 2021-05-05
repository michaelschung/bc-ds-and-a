'''
Mr. Chung
4/5: File reading review
'''

counts = {}

with open('txt/small1.txt', 'r') as f:
    for line in f:
        word = line.strip()
        # Check the first letter of word
        first = word[0]
        # If we have not seen it before, add it to
        # counts with count of 1
        if first not in counts:
            counts[first] = 1
        # Otherwise, bump up the current count by 1
        else:
            counts[first] += 1

print(counts)

# {'a': 3, 'b': 26, }
