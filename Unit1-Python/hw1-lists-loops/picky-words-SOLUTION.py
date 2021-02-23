'''
Create a list of words of varying lengths. Then, count the number of words that are 3 letters long *and* begin with the letter 'c'. The count should be printed at the end of your code.
• Example: given the list ['bat', 'car', 'cat', 'door', 'house', 'map', 'cyst', 'pear', 'can', 'spike'], there are exactly 3 qualifying words.
'''

words = ['bat', 'car', 'cat', 'door', 'house', 'map', 'cyst', 'pear', 'can', 'spike', 'ace', 'cpe']

count = 0
for word in words:
    if len(word) == 3 and word[0] == 'c':
        count += 1
print(count)
