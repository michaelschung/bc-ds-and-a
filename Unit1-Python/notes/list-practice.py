# Michel Chung
# 2/8: List Practice Problems

# 1) Find sum of all numbers in a list
num_lst = [6, 3, 8, 3, 4, 5]

total = 0
for val in num_lst:
    total += val
print(total)

# 2) Create a copy of a list
new_lst = []
for val in num_lst:
    new_lst.append(val)
print(new_lst)

#############################################################
### Extra example problems that we didn't get to in class ###
#############################################################

# 3) Create copy of list, but don't repeat any values
new_lst = []
for val in num_lst:
    # Only append val if it's not already in new_lst
    if val not in new_lst:
        new_lst.append(val)
print(new_lst)

# 4) Count how many words are at least 4 characters long
word_lst = ['hello', 'hmm', 'nope', 'why', 'coffee']

count = 0
for word in word_lst:
    if len(word) >= 4:
        count += 1
print(count)
