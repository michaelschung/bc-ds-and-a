# Michael Chung
# 2/23: Sorting preliminary functions

# 1) Method that takes a list of numbers as a parameter, and prints the first and last values in the list.
def first_and_last(lst):
    print(lst[0])
    print(lst[-1])

# 2) Method: takes a list of numbers and an index as parameters; returns True if the number at the given index is 0 or more, or False if the number is negative
def geq_0(lst, i):
    if lst[i] >= 0:
        return True
    else:
        return False

# 3) Method: takes a list of numbers and two indexes as parameters; swaps the two values in the list at the given indexes
def swap(lst, i, j):
    temp = lst[j]
    lst[j] = lst[i]
    lst[i] = temp

nums = [1, 2, 3, 4, 5]
#       0, 1, 2, 3, 4
# save = 3
swap(nums, 0, 2)
print(nums)












#
