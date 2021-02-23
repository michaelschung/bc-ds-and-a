# Michael Chung
# 2/17: Methods

# Type 1: Procedure (no parameters, no return)
def greetings():
    print('hello')
    print('goodbye')

# Type 2: Provider (no parameters, yes return)
def get_5():
    return 5

# Type 3: Consumer (yes parameters, no return)
def print_n_times(n):
    for i in range(n):
        print('hi')

# Type 4: Function (yes parameters, yes return)
def add_nums(a, b):
    return a + b

############ PRACTICE ############

# Sum a list
def sum_list(lst):
    total = 0
    for val in lst:
        total += val
    return total

print(sum_list([1, 2, 3, 4]))
print(sum_list([1, 2, 3, 4, 5, 6, 7]))

# Write a function that takes two numbers as parameters, and returns the value of the first number raised to the power of the second
def square_nums(x, y):
    total = 1
    for i in range(y):
        total *= x
    return total

print(square_nums(2, 3))

#############

# Subset
def is_subset(list1, list2):
    overlap = True
    for val in list1:
        if val not in list2:
            overlap = False
    return overlap

list1 = [4, 6, 2]
list2 = [3, 6, 2, 8, 5, 4, 1, 0]

print(is_subset(list1, list2))
















#
