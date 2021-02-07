# Michael Chung
# HW 1: Lists & Loops
# 2) List Max

lst = [2, 1, 4, 3]

max = lst[0]
for val in lst:
    if val > max:
        max = val

print(max)
