# Michael Chung
# 2/10: More Lists (+ extra stuff)

words = ['bat', 'car', 'cat', 'door', 'house', 'map', 'cyst', 'pear', 'can', 'spike', 'ace', 'cpe']

# ===Negative indexes===
print(words[-1])
words_slice = words[-5:]
print(words_slice)

# ===String indexes===
str = 'hello'
print(str[-4:])

for letter in str:
    print(letter)

# ===Looping through lists===
print('===Looping through lists===')

# Looping by value
print('---Loop by value---')
for word in words:
    print(word)

# Looping by index
print('---Loop by index---')
for i in range(len(words)):
    print(i, words[i])

# Looping by index and value (looping by index-value pairs)
print('---Loop by index and value---')
# [(0, bat), (1, car), (2, cat), (3, door), ...]
for i, word in enumerate(words):
    print(i, word)

# ===Back to conditionals===
cond = 5 < 3
if (cond):
    print('Yes')
else:
    print('No')

x = 15
if x < 10:
    print('x less than 10')
elif x < 20:
    print('x is between 10 and 20')
elif x < 30:
    print('x is between 20 and 30')
else:
    print('x >= 30')
