def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2 
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return (merge(left,right))
    
    
def merge(left,right):
    i=j=0
    result=[]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result
    
    
arr=[15,66,11,77,14,72,73,34]
print(merge_sort(arr))
            