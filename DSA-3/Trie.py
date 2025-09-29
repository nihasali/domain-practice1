class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word=False
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self,word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i]=Node()
            node=node.children[i]

        node.end_of_word = True
    
    def search(self,word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            
            node = node.children[i]
        
        return node.end_of_word
    
    def autocomplete(self,prefix):
        node = self.root
        result=[]
        for i in prefix:
            if i not in node.children:
                return []
            node = node.children[i]
            
        self._dfs(node,prefix,result)
        return result

    def _dfs(self,node,prefix,result):
        if node.end_of_word:
            result.append(prefix)

        for i,j in node.children.items():
            self._dfs(j,prefix+i,result)


x = Trie()
x.insert('apple')
x.insert('appeil')
print(x.search('apple'))
print(x.autocomplete('app'))