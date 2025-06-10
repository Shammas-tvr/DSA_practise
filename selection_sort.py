def insertion_sort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(len(arr)):
        minInd=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minInd]:
                minInd=j
        arr[i],arr[minInd] = arr[minInd],arr[i]
    return arr
    
    
arr=[13,63,66,77,11,66]    
print(insertion_sort(arr))
