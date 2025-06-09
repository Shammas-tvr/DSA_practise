def bubble_sort(arr):
    if len(arr) <=1:
        return arr
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
    
    
arr=[13,6,43,77,1,67,77]
print(bubble_sort(arr))