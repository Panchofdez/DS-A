# my implementation of mergesort

def mergesort(array):
	if len(array) == 1:
		return array
	midpoint = len(array) // 2

	left = mergesort(array[:midpoint])
	right = mergesort(array[midpoint:])
	
	i=0
	j=0
	sorted_arr = []
	while i < len(left) or j <len(right):
		if i >= len(left):
			sorted_arr.append(right[j]) 
			j += 1
		elif j >= len(right):
			sorted_arr.append(left[i])
			i += 1
		elif left[i] <= right[j]:
			sorted_arr.append(left[i])
			i += 1
		else:
			sorted_arr.append(right[j])
			j+=1

	return sorted_arr


test = [21, 4, 1, 3, 9, 20, 25, 6, 40, 14]
sorted_arr = mergesort(test) 
print(sorted_arr)