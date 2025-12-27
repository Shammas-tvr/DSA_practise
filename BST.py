class Node:
    def __init__(self,val):
        self.left=None
        self.val=val
        self.right=None
        
        
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self,val):
        if self.root is None:
            self.root=Node(val)
            return
        self.insert_rec(self.root,val)
        
    def insert_rec(self,node,val):
        if val < node.val:
            if node.left is None:
                node.left=Node(val)
                return
            else:
                self.insert_rec(node.left,val)
                
        elif val > node.val:
            if node.right is None:
                node.right=Node(val)
                return
            else:
                self.insert_rec(node.right,val)
                
        return 
    
    
    def delete(self,key):
        if self.root is None:
            print("The Tree is empty ")
            return 
        self.root=self.delete_rec(self.root,key)
        
    def delete_rec(node,key):
        if key < node.val:
            node.left=self.delete_rec(node.left,key)
        elif key > node.val:
            node.right=self.delete_rec(node.right,key)
            
        else:
            if node.left is None:
                return node.right
                
            if node.right is None:
                return node.left
                
            else:
                temp=self.find_min(node.right)
                node.val=temp
                node.right=self.delete_rec(node.right,temp)
                
        return
    
    def find_min(self,node):
        while node.left:
            node=node.left
        return node.val
        
        
        
        
                

