class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        
class Hash_Table:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
        
    def hash(self,key):
        if isinstance(key,str):
            index=sum(ord(c) for c in key)
        else:
            index=key
        return index % self.size
        
    def insert(self,key,val):
        index=self.hash(key)
        curr=self.table[index]
    
        if self.table[index] is None:
            self.table[index]=Node(key,val)
            return
        while curr:
            if curr.key == key:
                curr.val = val
                return 
            if curr.next is None:
                break
            curr=curr.next
        curr.next=Node(key,val)
        
    def delete(self,key):
        index=self.hash(key)
        curr=self.table[index]
        prev=None
        
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                    return
                else:
                    self.table[index]=curr.next
                    return
            prev=curr
            curr=curr.next
        return False
        
        
    def get(self,key):
        index=self.hash(key)
        curr=self.table[index]
        while curr:
            if curr.key == key:
                print(curr.key,curr.val)
            curr=curr.next
        return " the key is not found "
h1=Hash_Table(5)
h1.insert("name","shammas")
h1.insert("place",'vadakar')
h1.insert("age",23)   
h1.get("age")        
        
    
    
    
    
    
    
    
    
    
    
    
    
            