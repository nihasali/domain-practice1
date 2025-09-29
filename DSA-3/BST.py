class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        self.root = self.insert_rec(self.root,value)

    def insert_rec(self,node,value):
        if node is None:
            return Node(value)
        
        if value < node.value:
            node.left = self.insert_rec(node.left,value)
        elif value > node.value:
            node.right=self.insert_rec(node.right,value)
        
        return node
    
    def search(self,value):
        return self.search_rec(self.root,value)
    
    def search_rec(self,node,value):
        if node is None:
            return False
        
        if value == node.value:
            return True
        
        if value < node.value:
            return self.search_rec(node.left,value)
        
        elif value > node.value:
            return self.search_rec(node.right,value)

    def delete(self,value):
        self.root = self.delete_rec(self.root,value)

    def delete_rec(self,node,value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = delete_rec(node.left,value)
        
        elif value > node.value:
            node.right = delete_rec(node.right,value)
        
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            min_large=self.get_min(node.right)
            node.value=min_large.value
            node.right = self.delete_rec(node.right,min_large.value)
        
        return node
    
    def get_min(self,node):
        while node.left:
            node=node.left
        return node

    
    def inorder(self):
        self.inorder_rec(self.root)
    
    def inorder_rec(self,node):
        if node:
            self.inorder_rec(node.left)
            print(node.value,end=' ')
            self.inorder_rec(node.right)


a=BST()
a.insert(10)
a.insert(20)
a.insert(30)
a.insert(40)
a.insert(5)
print("Before deletion:")
a.inorder()
print("\nAfter deleting 10:")
a.delete(30)
a.inorder()