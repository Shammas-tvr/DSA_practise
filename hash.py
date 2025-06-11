class Hash:
    def __init__(self,size):
        self.table=[[] for _ in range(size)]
        self.size=size
        
    def hashfunction(self,key):
        if isinstance(key,str):
            index=sum(ord(i)for i in key)
            return index % self.size
        return index % self.size
        
    def insert(self,key,val):
        index=self.hashfunction(key)
        bucket=self.table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i]=(key,val)
                return 
        bucket.append((key,val))
        return 
    
    
    def delete(self,key):
        index=self.hashfunction(key)
        bucket=self.table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
        return "The key is not found in the Hash" 
        
        
    def get(self,key):
        index=self.hashfunction(key)
        bucket=self.table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                print(f"key : {bucket[i][0]} value :{bucket[i][1]}")
                return 
        return "The key is not found in the Hash" 
        
    def display(self):
        print(self.table)
        
        
        
        
h1 = Hash(5)

h1.insert("name", "shammas")
h1.insert("age", 23)
h1.insert("city", "Kozhikode")
h1.insert("email", "shammas@example.com")
h1.insert("gender", "male")
h1.display()
h1.delete("email")
h1.display()