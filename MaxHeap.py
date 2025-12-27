class MaxHeap:
    def __init__(self):
        self.heap=[]

    def parent(self,i):
        return (i-1)//2
    def left_child(self,i):
        return 2 * i + 1
    def right_child(self,i):
        return 2 * i + 2
    def swap(self,i,j):
        self.heap[j],self.heap[i]=self.heap[i],self.heap[j]
        return
    def insert(self,val):
        self.heap.append(val)
        if len(self.heap) > 1:
            self.heapify_up(len(self.heap)-1)  
            
    def heapify_up(self,index):
        while index >0:
            parent=(index-1)//2
            if self.heap[index] > self.heap[parent]:
                self.swap(index,parent)
                index=parent
            else:
                break    

    def delete(self):
        if len(self.heap) ==0:
            print("The Heap is Empty")
            return 
        
        if len(self.heap) ==1:
            return self.heap.pop()
        deleted=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return deleted

    def heapify_down(self,index):
        right= 2 * index +2
        left= 2 * index + 1
        largest=index
        size=len(self.heap)
        if  left < size  and self.heap[left] > self.heap[largest]:
            largest=left
        if right < size and self.heap[right] > self.heap[largest]:
            largest=right
        if index != largest:
            self.swap(index,largest)
            self.heapify_down(largest)

    def get_heap(self):
        return self.heap


    def MinHeapToMaxHeap(self,arr):
        self.heap=list(arr)
        for i in range((len(self.heap)//2)-1,-1,-1):
            self.heapify_down(i)     
        return self.heap      
h=MaxHeap()
h.insert(10)
h.insert(40)
h.insert(60)
h.insert(80)
h.insert(70)
print(h.get_heap())
h1=MaxHeap()
print(h1.MinHeapToMaxHeap(h.get_heap()))

                     
