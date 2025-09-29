# class Node:
#     def __init__(self):
#         self.graph = {}

#     def add_node(self,node):
#         if node not in self.graph:
#             self.graph[node]=[]

#     def add_edge(self,node1,node2):
#         if node1 not in self.graph:
#             self.graph[node1]=[]

#         if node2 not in self.graph:
#             self.graph[node2]=[]

#         self.graph[node1].append(node2)
#         self.graph[node2].append(node1)

#     def remove_node(self,node):
#         if node in self.graph:
#             del self.graph[node]

#         for neighbors in self.graph.values():
#             if node in neighbors:
#                 neighbors.remove(node)

#     def remove_edge(self,node1,node2):
#         if node1 in self.graph and node2 in self.graph[node1]:
#             self.graph[node1].remove(node2)
#         if node2 in self.graph and node1 in self.graph[node2]:
#             self.graph[node2].remove(node1)

#     def bfs(self,start):
#         visited = set()
#         queue = [start]
#         while queue:
#             if 



# class Heap:
#     def __init__(self):
#         self.heap = []

#     def insert(self,value):
#         self.heap.append(value)
#         self.heapify_up(len(self.heap)-1)

#     def get_min(self):
#         if self.heap is None:
#             return 'deletion not possible'

#         if len(self.heap)==1:
#             self.heap.pop()
        
#         data = self.heap[0]
#         self.heap[0]=self.heap.pop()
#         self.heapify_down(0)
#         return data

#     def heapify_up(self,index):
#         parent = len(self.heap)//2
#         if index > 0 and self.heap[index] < self.heap[parent]:
#             self.heap[parent],self.heap[index]=self.heap[index],self.heap[parent]
#             self.heapify_up(parent)

#     def heapify_down(self,index):
#         smallest = index
#         left = 2 * index +1
#         right = 2 * index +2

#         if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#             smallest = left
#         if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#             smallest = right
        
#         if smallest != index:
#             self.heap[smallest],self.heap[index]=self.heap[index],self.heap[smallest]
#             self.heapify_down(smallest)

#     def peek(self):
#         return self.heap[0]

#     def size(self):
#         return len(self.heap)



