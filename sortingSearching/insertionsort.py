# def insertionsort(array):

# 	for i in range(1, len(array)):
# 		for j in range(i-1 , -1, -1):
# 			if array[j]>array[i]:
# 				array[i], array[j] = array[j], array[i]
# 				i-=1
# 			elif array[j]<array[i]:
# 				break
# 	print(array)

#another better way

def insertionsort(array):
	for i in range(1, len(array)):
		val = array[i]
		j = i-1
		while j >=0 and array[j]>val:
			array[j+1] = array[j]
			j-=1

		array[j+1] = val
	return array

print(insertionsort([7,3,4,8,6,5,1,2,9,10]))
