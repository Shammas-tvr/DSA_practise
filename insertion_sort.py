def insertion_sort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j] > temp:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            j-=1 
        arr[j+1] = temp
    return arr
    
arr=[1,37,54,88,4,7]
print(insertion_sort(arr))
    