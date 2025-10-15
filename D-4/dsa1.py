# class Hashtable:
#     def __init__(self,size):
#         self.size = size
#         self.table = [[] for x in range(size)]

#     def hash_function(self,key):
#         return hash(key)%self.size

#     def insert(self,k,v):
#         index = self.hash_function(k)
#         self.table[index].append((k,v))

#     def get(self,key):
#         if key is None:
#             return False
#         index = self.hash_function(key)
#         for k in self.table[index]:
#             if k[0] == key:
#                 return k[1]

#         return False

#     def delete(self,key):
#         if key is None:
#             return 'deletion not possible'

#         index = self.hash_function(key)
#         for i,(k,v) in enumerate(self.table[index]):
#             if k == key:
#                 return self.table[index].pop(i)

#         return False

#     def display(self):
#         for k,v in enumerate(self.table):
#             print(f'{k}:{v}')

# ht = Hashtable(5)
# ht.insert('a',1)
# ht.insert('b',2)
# ht.insert('c',3)
# ht.insert('d',4)
# ht.insert('e',5)
# ht.display()

# print('find :')
# print(ht.get('d'))
# print(ht.delete('f'))
# ht.display()



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
#         if not node:
#             return Node(value)

#         if value < node.value:
#             node.left = self.insert_rec(node.left,value)
        
#         elif value > node.value:
#             node.right = self.insert_rec(node.right,value)

#         return node

#     def inorder(self):
#         self.inorder_rec(self.root)

#     def inorder_rec(self,node):
#         if node:
#             self.inorder_rec(node.left)
#             print(node.value,end=' ')
#             self.inorder_rec(node.right)

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
#             if not node.left:
#                 return node.right
#             elif not node.right:
#                 return node.left

#             min_large = self.get_min(node.right)
#             node.value = min_large.value
#             node.right = self.delete_rec(node.right,min_large.value)

#     def get_min(self,node):
#         while node.left:
#             node = node.left

#         return node



class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self,node):
        if node not in self.graph:
            self.graph[node]=[]

    def add_edge(self,node1,node2):
        if node1 not in self.graph:
            self.graph[node1]=[]

        if node2 not in self.graph:
            self.graph[node2]=[]

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def delete_node(self,node):
        if node not in self.graph:
            return None
        del self.graph[node]

        for neighbor in self.graph.values():
            if node in neighbor:
                self.graph.remove(node)

    def delete_edge(self,u,v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)

        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def bfs(self,start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node and node not in visited:
                print(node,end=' ')
                visited.add(node)
                queue.extend([x for x in self.graph[node] if x not in visited])

        print()

    def dfs(self,)