# Michael Chung
# HW 1: Lists & Loops
# 2) List Max

lst = [2, 1, 4, 3]

max = lst[0]
# Check each value in the list
for val in lst:
    # If we find a value larger than our current max
    if val > max:
        # Update our current max to this new value
        max = val

print(max)
