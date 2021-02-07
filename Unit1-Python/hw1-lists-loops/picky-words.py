# Michael Chung
# HW 1: Lists & Loops
# 4) Picky Words

lst = ['bat', 'car', 'cat', 'door', 'house', 'map', 'cyst', 'pear', 'can', 'spike']

count = 0
for word in lst:
    if len(word) == 3 and word[0] == 'c':
        count += 1

print(count)
