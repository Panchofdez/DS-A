class Heap:
	def __init__(self, items):
		self.items = []
		for i in range(len(items)):
			self.items.append(items[i])
			self.trickle_up(i)
	def peak(self):
		return self.items[0]
	def heapsort(self):
		for i in range(len(self.items)-1, 0, -1):
			self.swap(0, i)
			self.trickle_down(0, i)
		return self.items
	def swap(self,index1, index2):
		self.items[index1], self.items[index2] = self.items[index2], self.items[index1]
		return 
	def trickle_up(self, index):
		parent_index = (index-1)//2
		if parent_index >= 0:	
			if self.items[parent_index] < self.items[index]:
				self.swap(parent_index, index)
				self.trickle_up(parent_index)
		return 		
	def trickle_down(self, index, end):
		parent = index
		leftchild = 2*parent + 1
		rightchild = 2*parent + 2		
		if leftchild < end and self.items[parent] < self.items[leftchild]:
			parent = leftchild
		if rightchild < end and self.items[parent] < self.items[rightchild]:
			parent = rightchild
		
		if parent != index:
			self.swap(index, parent)
			self.trickle_down(parent, end)



heap = Heap([12,11,13,5,6,7, 1,3,4])

print(heap.items)
print(heap.peak())
print(heap.heapsort())


#another alternative using functions
# # Python program for implementation of heap Sort 
  
# # To heapify subtree rooted at index i. 
# # n is size of heap 
# def heapify(arr, n, i): 
#     largest = i # Initialize largest as root 
#     l = 2 * i + 1     # left = 2*i + 1 
#     r = 2 * i + 2     # right = 2*i + 2 
  
#     # See if left child of root exists and is 
#     # greater than root 
#     if l < n and arr[i] < arr[l]: 
#         largest = l 
  
#     # See if right child of root exists and is 
#     # greater than root 
#     if r < n and arr[largest] < arr[r]: 
#         largest = r 
  
#     # Change root, if needed 
#     if largest != i: 
#         arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
#         # Heapify the root. 
#         heapify(arr, n, largest) 
  
# # The main function to sort an array of given size 
# def heapSort(arr): 
#     n = len(arr) 
  
#     # Build a maxheap. 
#     for i in range(n//2 - 1, -1, -1): 
#         heapify(arr, n, i) 
  
#     # One by one extract elements 
#     for i in range(n-1, 0, -1): 
#         arr[i], arr[0] = arr[0], arr[i] # swap 
#         heapify(arr, i, 0) 
  
# # Driver code to test above 
# arr = [ 12, 11, 13, 5, 6, 7] 
# heapSort(arr) 
# n = len(arr) 
# print ("Sorted array is") 
# for i in range(n): 
#     print ("%d" %arr[i]), 
# # This code is contributed by Mohit Kumra 
