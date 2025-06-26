class circularqueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None] * size
        self.rear=-1
        self.front=-1
        
    def enqueue(self,data):
        if (self.rear +1 ) % self.size == self.front:
            print(" queue is full ")
            return 
        if self.front == -1:
            self.rear = 0
            self.front=0
            self.queue[self.rear] = data
            return
        else:
            self.rear=(self.rear +1 ) % self.size
            self.queue[self.rear]=data
            
            
    def dequeue(self):
        if self.front == -1:
            print("the queue is empty")
            return 
        if self.front == self.rear:
            self.rear=-1
            self.front=-1
        else:
            self.front= (self.front +1) % self.size
            return 
    def display(self):
        print(self.queue)
q1=circularqueue(3)
q1.enqueue(10)
q1.enqueue(20)
q1.dequeue()
q1.enqueue(50)
q1.display()
        
        
        
        
        
        
        
        
        
        
        