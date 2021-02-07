# Michael Chung
# HW 1: Lists & Loops
# 5) Sorted List

lst = ['hello', 'nope', 'garbage', 'carrot', 'rip', 'um']

sorted_lst = []
for i in range(1, 10):
    for word in lst:
        if len(word) == i:
            sorted_lst.append(word)

print(sorted_lst)
