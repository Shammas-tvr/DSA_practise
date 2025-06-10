def reverse(queue,po):
    if po <=0 or po > len(queue):
        return "invalid value of position "
    k=po    
    for j in range(k//2+1):
        queue[j],queue[k]=queue[k],queue[j]
        k-=1
    return queue
    
que=[2,1,6,2,6,16,77,88,33,55]    
print(reverse(que,5)) 