"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array) <=1:
        return array
    i = 0
    j=0
    pivot = array[-1]
    while j <= (len(array)-1):
        if j == len(array)-1:
            array[j], array[i] = array[i], array[j]
        elif array[j] < pivot:
           array[i], array[j] = array[j], array[i]
           i += 1
        j += 1
    sorted_array  = quicksort(array[:i]) + [array[i]] + quicksort(array[i+1:])
    return sorted_array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))