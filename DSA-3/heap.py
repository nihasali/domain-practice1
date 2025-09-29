class Heap:
    def __init__(self):
        self.heap = []

    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)

    def get_min(self):
        if not self.heap:
            return None

        if len(self.heap)==1:
            return self.heap.pop()

        data = self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return data

    def heapify_up(self,index):
        parent = (index-1)//2
        
        if index > 0 and self.heap[index]<self.heap[parent]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            self.heapify_up(parent)

    def heapify_down(self,index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[smallest] > self.heap[left]:
            smallest = left

        if right < len(self.heap) and self.heap[smallest] > self.heap[right]:
            smallest = right
        
        if smallest != index:
                self.heap[smallest],self.heap[index]=self.heap[index],self.heap[smallest]
                self.heapify_down(smallest)
