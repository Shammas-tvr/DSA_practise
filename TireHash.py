class TrieNode:
    def __init__(self):
        self.childrens={}
        self.is_end=False


class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.childrens:
                node.childrens[char]=TrieNode()
            node=node.childrens[char]
        node.is_end=True    


    def delete(self,word):
        def _delete(node,word,depth):
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end=False
                return len(node.childrens) ==0
            char=word[depth]
            if char not in node.childrens:
                return False
            deleting=_delete(node.childrens[char],word,depth+1)

            if deleting:
                del node.childrens[char]
                return len(node.childrens) == 0 and not node.is_end
            return False     
        return _delete(self.root,word,0) 
    
    def longest_prefix(self):
        node=self.root
        prefix=""

        while node and len(node.childrens) ==1 and not node.is_end:
            char=next(iter(node.childrens))
            prefix+=char
            node=node.childrens[char]
        return prefix


    def autocompletion(self,prefix):
        node=self.root
        words=[]
        for char in prefix:
            if char not in node.childrens:
                return []
            node=node.childrens[char]

        def dfs(node,prefix):
            if node.is_end:
                words.append(prefix)
            for char in node.childrens:
                dfs(node.childrens[char],prefix+char)    
        dfs(node,prefix)
        return words


            
    def unique_words(self):
        count=0
        def find_words(node):
            nonlocal count
            if node.is_end:
                count+=1
            for char in node.childrens:
                find_words(node.childrens[char])
        find_words(self.root)        
        return count  
    
    def prefix_words(self,prefix):
        node=self.root
        count=0
        for char in prefix:
            if char not in node.childrens:
                return 0
            node=node.childrens[char]
        def dfs(node):
            nonlocal count
            if node.is_end:
                count+=1
            for char in node.childrens:
                dfs(node.childrens[char])
        dfs(node)
        return count            

           
        
tr=Trie()
tr.insert("hallo")
tr.insert("hi")
tr.insert("shamm")
tr.insert("going")
tr.insert("want")
print(tr.unique_words())
print(tr.prefix_words("want"))