'''
1) Subset (subset.py)
Create two lists of numbers, one containing at least 4 values and the other containing at least 8; neither list should contain repeats. Then, write code that determines whether or not *all* of the values from the smaller list also appear in the larger list. Print either True or False at the end of your code.
• Example: Given list1 = [4, 6, 9, 2] and list2 = [3, 6, 2, 8, 5, 4, 1, 0], the result should be False, since the larger list does not contain the value 9.
'''

list1 = [4, 6, 9, 2, 60]
list2 = [3, 6, 2, 8, 5, 4, 1, 0]

overlap = True

for val in lst1:
    if val not in lst2:
        overlap = False

print(overlap)
