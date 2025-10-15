class Node:
    def __init__(self,value):
        self.value = value
        self.pref=None
        self.nref=None

class Doublelist:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print('ll is empty')
            return
        n = self.head
        while n is not None:
            print(n.value,end='-->')
            n=n.nref

    
    def add_begin(self,value):
        new_node = Node(value)
        new_node.nref = self.head
        if self.head is not None:
            self.head.pref = new_node
        self.head = new_node

    def add_after(self,x,value):
        if self.head is None:
            return 'not possible'

        n = self.head
        while n is not None:
            if n.value == x:
                break
            n = n.nref

        if n is None:
            return f'{x} is not in ll'

        else:
            new_node = Node(value)
            new_node.nref = n.nref
            new_node.pref = n
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node
    
    def middle(self):
        if self.head is None:
            print('not possible')
            return
        slow = self.head
        fast = self.head
        while fast and fast.nref:
            slow = slow.nref
            fast = fast.nref.nref
        return slow.value

ll1 = Doublelist()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
ll1.add_begin(40)
ll1.add_begin(50)
ll1.add_after(20,25)
ll1.add_after(40,45)
ll1.print_ll()
print('haii')
print(ll1.middle())