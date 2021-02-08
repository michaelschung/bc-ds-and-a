# Michael Chung
# 2/8: Lists & Loops

lst = [1, 2, 3, 4, 5, 6]
#      0  1  2  3  4  5

# ===Access by index (a.k.a. position)===
print(lst[4])
# Can use index to set values
lst[4] = 200
print(lst)

# ===Add to the end of the list using .append()===
lst.append(10)
print(lst)

# ===Remove from list using .remove(); removes by value, not index===
lst.remove(2)
print(lst)

# ===Concatenating lists===
lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]

# Without changing original lists
lst3 = lst1 + lst2
print(lst3)

# Changes the first list
lst1.extend(lst2)
print(lst1)

# ===List slicing: lst[start, end]===
# [start, end) - inclusive start, exclusive end
lst = [1, 2, 3, 4, 5, 6]
#      0  1  2  3  4  5

# Start at index 2, end before index 4
print(lst[2:4])
# Start at index 0, end before index 4
print(lst[0:4])
# Start at beginning, end before index 4
print(lst[:4])
# Start at index 3, end at the end
print(lst[3:])
# Start at beginning, end at end
print(lst[:])

# ==="in" operator===
print(2 in lst)
print(20 in lst)
word = 'hello'
print('e' in word)

# ===Looping through lists===
# Loop through one value at a time
for val in lst:
    if val != 4:
        print(val)
