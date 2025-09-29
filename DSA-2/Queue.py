class Que:
    def __init__(self):
        self.que = []

    def enque(self,data):
        self.que.append(data)

    def deque(self):
        if self.is_empty():
            return 'que is empty'
        return self.que.pop(0)
    
    def peek(self):
        if self.is_empty():
            return 'que is empty'
        return self.que[0]

    def is_empty(self):
        return len(self.que)==0
    
    def display(self):
        print(self.que)

    def recursive_rev(self):
        if self.is_empty():
            return
        front = self.deque()
        self.recursive_rev()
        self.enque(front)


q = Que()
q.enque('h')
q.enque('e')
q.enque('l')
q.enque('l')
q.enque('o')
q.display()

print(q.is_empty())
q.display()
q.recursive_rev()
q.display()
print(q.deque())