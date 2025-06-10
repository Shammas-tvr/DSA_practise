
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

            