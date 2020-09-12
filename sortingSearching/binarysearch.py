"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


# def binary_search(input_array, value):
#     """Your code goes here."""
#     for i in range(len(input_array)):
#         if input_array[i]== value:
#             return i
#     return -1

#Using iteration

# def binary_search(input_array, value):
#     """Your code goes here."""
#     low = 0
#     high = len(input_array)-1
#     mid = (low + high)//2
#     while low <= high:
#         mid = (low + high)//2
#         if input_array[mid] == value:
#             return mid
#         elif input_array[mid] > value:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1
    
#using recursion

def binary_search(input_array, high, low, value):
    mid = (low + high)//2
    if high<low:
        return -1
    if input_array[mid] == value:
        return mid
    elif input_array[mid] > value:
        high = mid - 1
        return binary_search(input_array, high, low, value)
    else:
        low = mid + 1
        return binary_search(input_array, high, low, value)
        
test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list,len(test_list), 0, test_val1))
print(binary_search(test_list, len(test_list), 0, test_val2))