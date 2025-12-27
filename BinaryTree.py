from collections import deque
class Node:
    def __init__(self,val):
        self.left=None
        self.val=val 
        self.right=None


class BT:
    def __init__(self):
        self.root=None

    def insert(self,val):
        if self.root is None:
            self.root=Node(val)
            return 
        que=deque([self.root])      
        while que:
            curr=que.popleft()
            if curr.left is None:
                curr.left=Node(val)
                return
            else:
                que.append(curr.left)

            if curr.right is None:
                curr.right=Node(val)
                return
            else:
                que.append(curr.right)

                

    def delete(self,delet):
        if self.root is None:
            print("The Tree is empty ")
            return 
        if self.root.left is None and self.root.right is None: 
            if self.root.val == delet:
                self.root=None
                return 
        target=None
        last_node=None
        last_parent=None
        que=deque([self.root])
        while que:
            curr=que.popleft()
            if curr.val == delet:
                target=curr

            if curr.left:
                que.append(curr.left)
                last_parent=curr
                last_node=curr.left

            if curr.right:
                que.append(curr.right)
                last_parent=curr
                last_node=curr.right

        if target:
            target.val=last_node.val
            if last_parent.left == last_node:
                last_parent.left=None
            else:
                last_parent.right=None
            return True 
        else:
            print("Given value not found in Tree")



    def level_order(self):
        if self.root is None:
            print("The Tree is empty ")
            return 
        res=[]
        que=deque([self.root])
        while que:
            curr=que.popleft()
            res.append(curr.val)  
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)

        return res
    
    def inorder(self):
        if self.root is None:
            print("The Tree is empty ")
            return
        self.inorder_rec(self.root)
        print()
            
    def inorder_rec(self,node):
        if node is None:
            return 
        self.inorder_rec(node.left)
        print(node.val, end=" ")
        self.inorder_rec(node.right)

    def preorder(self):
        if self.root is None:
            print("The Tree is empty")
            return 
        self.preorder_rec(self.root)
        print()

    def preorder_rec(self,node):
        if node is None:
            return 
        print(node.val,end=" ")
        self.preorder_rec(node.left)
        self.preorder_rec(node.right)


    def postorder(self):
        if self.root is None:
            print("The Tree is empty")
            return 
        self.postorder_rec(self.root)
        print()

    def postorder_rec(self,node):
        if node is None:
            return 
        self.postorder_rec(node.left)
        self.postorder_rec(node.right)
        print(node.val,end=" ")

    def find_min(self):
        mini=float('inf')
        que=deque([self.root])
        while que:
            curr=que.popleft()
            mini=min(mini,curr.val)
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
        return mini
    
    def find_max(self):
        maxi=float('-inf')
        que=deque([self.root])
        while que:
            curr=que.popleft()
            maxi=max(maxi,curr.val)
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)

        return maxi  


    def find_sec_larg(self):
        larg=0
        sec_larg=0
        que=deque([self.root])
        while que:
            curr=que.popleft()
            val=curr.val
            if val > larg:
                sec_larg=larg
                larg=val
            elif val < larg and val > sec_larg:
                sec_larg=val
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
        return sec_larg   



    def find_sec_smal(self):
        smal=float('inf')
        sec_smal=float('inf')
        que=deque([self.root])
        while que:
            curr=que.popleft()
            val=curr.val
            if val < smal:
                sec_smal=smal
                smal=val
            elif val > smal and val < sec_smal:
                sec_smal=val

            if curr.left:
                que.append(curr.left)

            if curr.right:
                que.append(curr.right)
        return sec_smal      

    def height(self):
        if self.root is None:
            print("The Tree is Empty ")
            return 
        return self.height_rec(self.root)

    def height_rec(self,node):
        if node is None:
            return 0
        left=self.height_rec(node.left)
        right=self.height_rec(node.right)
        return max(left,right)+1    
                                
    def find_leaf_nodes(self):
        if self.root is None:
            print("The Tree is empty")
            return
    def find_leafs(self,node):

        if node is None:
            return 0

        leafs=self.find_leafs(node.left)

    

                   


            







bt=BT()  
bt.insert(20)
bt.insert(30)
bt.insert(85)
bt.insert(57)
bt.insert(23)
bt.insert(85)
bt.insert(75)
print(bt.level_order())
bt.inorder()
bt.preorder()
bt.postorder()
print(bt.find_min())
print(bt.find_max())
print(bt.find_sec_larg()) 
print(bt.height())                



