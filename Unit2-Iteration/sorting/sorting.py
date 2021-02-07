def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def bubble_sort(lst):
    done = False
    while not done:
        done = True
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                swap(lst, i, i+1)
                done = False
    return lst

def insertion_sort(lst):
    for i in range(1, len(lst)):
        curr = lst[i]
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            swap(lst, j, j-1)
            j -= 1
    return lst

def selection_sort(lst):
    for i in range(len(lst)-1):
        min_i = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_i]:
                min_i = j
        swap(lst, i, min_i)
    return lst
