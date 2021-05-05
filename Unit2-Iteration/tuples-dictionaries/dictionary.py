'''
Mr. Chung
3/15: Dictionaries
'''

# Dictionaries are declared using curly brackets
empty_dict = {}

# Dictionaries store info in key-value pairs
dict = {'hello': 1, 'goodbye': 2, 'yo': 5}
print(dict['hello'])
# Use the 'in' operator to check for keys
print('hello' in dict)

# Change the value associated with the key 'hello'
dict['hello'] = 10
print(dict['hello'])

print(dict)

######## SEPARATOR ########
print('=' * 30)
###########################

# Example: use a dictionary to count occurrences
word_list = ['one', 'two', 'three', 'four', 'three', 'six', 'three', 'two', 'seven', 'three']

counts = {}

for word in word_list:
    # If we haven't seen the word before
    if word not in counts:
        # Add it to the dictionary with count 1
        counts[word] = 1
    # Otherwise (if we've already seen the word)
    else:
        # Bump the count by 1
        counts[word] += 1

print(counts)

# By the end of the loop, the dictionary looks like this: {'one': 1, 'two': 2, 'three': 4, 'four': 1, 'six': 1, 'seven': 1}

######## SEPARATOR ########
print('=' * 30)
###########################

# Dictionary keys must be immutable
# We cannot use a list as a key since lists can change, but we can use a tuple since they're immutable
dict2 = {(1, 2, 3): 'hello'}
print(dict2[(1, 2, 3)])
