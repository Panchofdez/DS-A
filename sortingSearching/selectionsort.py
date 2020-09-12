#The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. 
def selectionsort(array):
    for i in range(len(array)):
        min_index = i  
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


array = [ 1,5,2,3,7,4,6,9,10,8]
selectionsort(array)