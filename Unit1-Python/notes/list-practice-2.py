# Michael Chung
# 2/10: More lists practice



### 1) Given a string, convert that string to a list of characters ###
str = 'hello'

letters = []
for letter in str:
    letters.append(letter)
print(letters)



### 2) Check if these two lists have at least one common member ###
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]

# Start by assuming that there's no overlap
result = False
# Loop through lst1
for val in lst1:
    # Check if any member of lst1 is also in lst2
    if val in lst2:
        result = True
print(result)

'''
In #2, we started by assuming no overlap - note that this assumption was not arbitrary. Since the problem only requires that we find *one* common member, all we need is kind of a one-way switch that detects when we've found one. If we find a common member, flip the switch on; if we happen to find more later on, they'll just reinforce the "on-ness" of the switch, but the boolean will already have been set to True.
'''
