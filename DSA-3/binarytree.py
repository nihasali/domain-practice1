class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
def height(root):
    if root is None:
        return 0

    return 1+max(height(root.left),height(root.right))

root = Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right=Node(7)
root.left.left.left = Node(6)

print('height of tree is :',height(root))



from collections import deque

def find_max_iterative(root):
    if root is None:
        return float('-inf')
    
    q = deque([root])
    max_val = float('-inf')

    while q:
        node = q.popleft()
        max_val = max(max_val, node.value)
        
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    return max_val
