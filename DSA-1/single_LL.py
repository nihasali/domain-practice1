class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def print_ll(self):
        if self.head is None:
            print("linkedlist is empty")
            return
        else:
            n=self.head
            while n is not None:
                print(n.data,end='-->')
                n=n.ref
    
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node


    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def add_after(self,data,x):
        if self.head is None:
            print('linkedlist is empty')
            return
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print('not found')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print('deletion not possible')
            return
        self.head = self.head.ref
    
    def delete_end(self):
        if self.head is None:
            print('deletion not possible')
            return
        
        if self.head.ref is None:
            self.head = None
            return

        n = self.head
        while n.ref.ref is not None:
            n=n.ref
        n.ref = None

    def delete_value(self,data):
        if self.head is None:
            print('deletion not possible')
            return
        if data == self.head.data:
            self.head = self.head.ref
            return
        
        n = self.head
        while n.ref is not None:
            if data == n.ref.data:
                break
            n = n.ref
        
        if n.ref is None:
            print(f'{data} not found')
        else:
            n.ref = n.ref.ref
    
    def reverse_ll(self):
        prev = None
        current = self.head

        while current is not None:
            next_node=current.ref
            current.ref= prev
            prev = current
            current = next_node

        self.head = prev

    def middlle_delete(self):
        if self.head is None or self.head.ref is None:
            print('not possible')
            return
        
        prev = None
        slow = self.head
        fast = self.head
        while fast is not None and fast.ref is not None:
            prev = slow
            slow = slow.ref
            fast = fast.ref.ref
        
        if prev:
            prev.ref = slow.ref


# How it works

# slow → moves one step at a time.

# fast → moves two steps at a time.

# When fast reaches the end, slow is at the middle.

# prev keeps track of the node before slow, so we can unlink the middle.


    def circular_ll(self):
        if self.head is None:
            print('not possible to make circular')
            return

        n = self.head
        while n.ref is not None:
            n=n.ref
        
        n.ref = self.head

    def print_circular(self):
        if self.head is None:
            print('ll is empty')
            return
        
        n= self.head
        while True:
            print(n.data,end='-->')
            n = n.ref
            if n == self.head:
                break
        print('(head)')

    def remov_dup(self):
        if self.head is None:
            print("ll is Empty")
            return
        
        prev = None
        current = self.head
        seen = set()

        while current is not None:
            if current.data in seen:
                prev.ref = current.ref
            else:
                seen.add(current.data)
                prev=current
            current = current.ref
    
    