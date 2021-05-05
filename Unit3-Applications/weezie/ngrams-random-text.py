#Weezie Wilson
#4/19/21: Same as bigrams-random-text.py, but with ngrams

counts = {}
words = []
n = 5

with open('txt/tiny.txt', 'r') as f:
    for line in f:
        words.extend(line.strip().split())

print(words)

for i in range(len(words)-n+1):
    lst = []
    for j in range(n):
        lst.append(words[i+j])
    tup = tuple(lst)
    print(tup)

    if tup in counts:
        counts[tup].append(words[i+n])
    else:
        counts[tup] = [words[i+(n-1)]]

print(counts)
