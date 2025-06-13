
# use stack with delete the earliest element when reches the specified size 
class Stack:
    def __init__(self,size):
        self.stack=[]
        self.size=size
        
    def push(self,val):
        if len(self.stack) == self.size:
            self.stack.pop(0)
            self.stack.append(val)
            return
        self.stack.append(val)
        
    def display(self):
        print(self.stack)
        
        
st=Stack(5)
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)
st.push(60)
st.display()

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
        
class Stack:
    def __init__(self):
        self.head=None
        
    def push(self,val):
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        
    def is_empty(self):
        return self.head is None
        
        
    def Pop(self):
        if self.is_empty():
            return "the node is empty"
        poped=self.head.val
        self.head=self.head.next
        return poped 
        
    def peek(self):
        if self.is_empty():
            return "the node is empty"
        print(self.head.val)
        
        
    def display(self):
        if self.is_empty():
            print(" the node is empty ")
        else:
            curr=self.head
            while curr:
                print(curr.val,end=" ")
                curr=curr.next
                
    def max_val(self):
        max_val=self.head.val
        curr=self.head
        while curr:
            if curr.val > max_val:
                max_val=curr.val
            curr=curr.next
        print(" the largest value ",max_val)  
        
    def min_val(self):
        max_val=self.head.val
        curr=self.head
        while curr:
            if curr.val < max_val:
                max_val=curr.val
            curr=curr.next
        print(" the largest value ",max_val)             
            
st=Stack()
st.push(100)
st.push(10)
st.push(80)
st.push(90)
st.peek()
st.peek()
st.display()
st.max_val()
st.min_val()            