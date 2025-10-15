class Heap:
    def __init__(self):
        self.heap = []
        
    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        
    def heapify_up(self,index):
        parent = (index-1)//2
        
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            self.heapify_up(parent)
            
    def extract_max(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            data = self.heap.pop()
            return data
            
        max_value = self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        
        return max_value
        
    def heapify_down(self,index):
        left = index*2 + 1
        right = index*2 + 2
        largest = index
        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
            
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
            
        if largest!=index:
            self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
            self.heapify_down(largest)
            
x1 = Heap()
x1.insert(10)
x1.insert(20)
x1.insert(30)
x1.insert(40)
x1.extract_max()
print(x1.heap)




