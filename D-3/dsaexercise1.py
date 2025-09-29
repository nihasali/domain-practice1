# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None

    
#     def insert(self,value):
#         self.root = self.insert_rec(self.root,value)

#     def insert_rec(self,node,value):
#         if node is None:
#             return Node(value)

#         if value < node.value:
#             node.left = self.insert_rec(node.left,value)

#         elif value > node.value:
#             node.right = self.insert_rec(node.right,value)

#         return node


#     def search(self,value):
#         return self.search_rec(self.root,value)

#     def search_rec(self,node,value):
#         if node is None:
#             return False

#         if node.value==value:
#             return True

#         if value < node.value:
#             return self.insert_rec(node.left,value)

#         elif value > node.value:
#             return self.insert_rec(node.right,value)

#     def preorder(self):
#         self.preorder_rec(self.root)
    
#     def preorder_rec(self,node):
#         if node:
#             print(node.value,end=' ')
#             self.preorder_rec(node.left)
#             self.preorder_rec(node.right)

#     def delete(self,value):
#         self.root = self.delete_rec(self.root,value)

#     def delete_rec(self,node,value):
#         if node is None:
#             return None
        
#         if value < node.value:
#             node.left = self.delete_rec(node.left,value)
#         elif value > node.value:
#             node.right = self.delete_rec(node.right,value)

#         else:
#             if node.left is None:
#                 return node.right
#             elif node.right is None:
#                 return node.left

#             min_large = self.get_min(node.right)
#             node.value = min_large.value
#             node.right = self.delete_rec(node.right,min_large.value)

#         return node

#     def get_min(self,node):
#         while node.left:
#             node = node.left

#         return node


# a=BST()
# a.insert(10)
# a.insert(20)
# a.insert(30)
# a.insert(40)
# a.insert(5)
# print("Before deletion:")
# a.preorder()
# print("\nAfter deleting 10:")
# a.delete(10)
# a.preorder()


# class Hashtable:
#     def __init__(self,size):
#         self.table = [[] for x in range(size)]
#         self.size = size

#     def hash_function(self,key):
#         return hash(key)%self.size

#     def insert(self,k,v):
#         index = self.hash_function(k)
#         self.table[index].append((k,v))

#     def get(self,k):
#         index = self.hash_function(k)
#         for i in self.table[index]:
#             if i[0] == k:
#                 return i[1]

#         return 'not found'

#     def display(self):
#         for k,v in enumerate(self.table):
#             print(f'{k} : {v}')


# ht = Hashtable(5)
# ht.insert(1,2)
# ht.insert(5,6)
# ht.insert(6,7)
# ht.insert(7,8)
# ht.insert(8,9)
# print(ht.get(1))
# ht.display()


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None


# def height(root):
#     if root is None:
#         return 0

#     return 1+max(height(root.left),height(root.right))

# root = Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.left.right=Node(7)
# root.left.left.left = Node(6)

# print(height(root))



class Node:
    def __init__(self):
        self.children={}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self,word):
        node = self.root
        if word is None:
            return 'not possible'

        for i in word:
            if i not in node.children:
                node.children[i]=Node()
            node = node.children[i]

        node.end_of_word = True

    def search(self,word):
        node = self.root
        if word is None:
            return 'not found'
        
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]

        return node.end_of_word

    def autocomplete(self,prefix):
        if prefix is None:
            return 'not possible'
        