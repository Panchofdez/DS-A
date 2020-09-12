def shellsort(arr):
    gap = len(arr)//2
    while gap > 0:
        print(arr)
        for i in range(gap, len(arr)):
            j = i - gap
            while j >=0:
                if arr[i]<arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]
                i = j
                j -= gap
        gap = gap//2
    return arr


array = [5,10,4,2,7,1,6,9,8,3]
print(shellsort(array))