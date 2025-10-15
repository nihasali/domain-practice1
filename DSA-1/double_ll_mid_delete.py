class Node:
    def __init__(self,value):
        self.value = value
        self.nref = None
        self.pref = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def print_l(self):
        if self.head is None:
            return None
            
        n = self.head
        while n is not None:
            print(n.value,end='-->')
            n = n.nref
            
    def insert(self,value):
        new_node = Node(value)
        new_node.nref = self.head
        if self.head is not None:
            self.head.pref = new_node
            
        self.head = new_node
        
    def middle_delete(self):
        prev = None
        slow = self.head
        fast = self.head
        while fast and fast.nref:
            prev = slow
            slow = slow.nref
            fast = fast.nref.nref
            
        if prev:
            prev.nref = slow.nref
            if slow.nref:
                slow.nref.pref = prev
        
ll1 = Linkedlist()
ll1.insert(10)
ll1.insert(20)
ll1.insert(30)
ll1.insert(5)
ll1.insert(60)
ll1.insert(40)
ll1.insert(50)
ll1.print_l()
print('\nmiddle-->')
ll1.middle_delete()
ll1.print_l()