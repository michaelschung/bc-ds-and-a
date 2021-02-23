# Mr. Chung
# 2/23: Sorting!

nums = [4, 8, 2, 1, 3, 7, 5, 6]
# nums = [1, 2, 3, 4, 5, 6, 7, 8]

def swap(lst, i, j):
    temp = lst[j]
    lst[j] = lst[i]
    lst[i] = temp

def my_reverse(lst):
    # Start a variable at either end
    i = 0
    j = len(lst) - 1

    # Loop as long as variables don't cross:
    #   Swap
    #   Move variables "inwards"
    for _ in range(len(lst) // 2):
        swap(lst, i, j)
        i += 1
        j -= 1

def bubble_sort(lst):
    # Do this thing 7 times
    for rep in range(len(lst)-1):
        # Loop through each pair
        for i in range(len(lst)-1):
            # if lst[i] and lst[i+1] are out of order, then swap them
            if lst[i] >= lst[i+1]:
                swap(lst, i, i+1)

bubble_sort(nums)
print(nums)







#
