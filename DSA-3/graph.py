# this is how a directed graph look like when  buld it

# self.graph = {
#     "A": ["B", "C"],
#     "B": ["D"],
#     "C": ["D"],
#     "D": []
# }
# visited = {"A"}   # A is already visited
# node = "A"


# undirected graph look like->

# A → B → D
#  \
#   → C → D

# self.graph = {
#     "A": ["B", "C"],
#     "B": ["A", "D"],
#     "C": ["A", "D"],
#     "D": ["B", "C"]
# }

#--------------------------------------------------------------------------------------

class Node:
    def __init__(self):
        self.graph = {}

    def add_node(self,node):
        if node not in self.graph:
            self.graph[node]=[]

    def add_edge(self,u,v):
        if u not in self.graph:
            self.add_node(u)
        if v not in self.graph:
            self.add_node(v)
        self.graph[u].append(v)
        self.graph[v].append(u) #undirected

    def remove_node(self,node):
        if node in self.graph:
            del self.graph[node]

        for neighbors in self.graph.values():
            if node in neighbors:
                neighbors.remove(node)

    def remove_edge(self,u,v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and v in self.graph[v]:
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

    def dfs(self,start):
        visited = set()
        self._dfs_helper(start,visited)
        print()

    def _dfs_helper(self,node,visited):
        if node not in visited:
            print(node,end=' ')
            visited.add(node)
            for neighbor in self.graph[node]:
                self._dfs_helper(neighbor,visited)

    