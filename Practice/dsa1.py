# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.ref = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def print_ll(self):
#         if self.head is none:
#             return 'not possible'

#         n = self.head
#         while n is not None:
#             print(n.value,end='-->')
#             n = n.ref

#     def add_begin(self,value):
#         new_node = Node(value)
#         new_node.ref = self.head
#         self.head = new_node

#     def add_end(self,value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node

#         else:    
#             n = self.head
#             while n.ref is not None:
#                 n= n.ref

#             n.ref = new_node

#     def delete_begin(self):
#         if self.head is None:
#             return 'not possible'

#         self.head = self.head.ref

#     def delete_end(self):
#         if self.head is None:
#             return 'not possible'

#         if self.head.ref is None:
#             self.head = None
#             return
        
#         n = self.head
#         while n.ref.ref is not None:
#             n = n.ref

#         n.ref = None

#     def delete_value(self,value):
#         if self.head is None:
#             return 'deletion not possible'

#         if value==self.head.value:
#             self.head = self.head.ref
#             return

#         n = self.head

#         while n.ref is not None:
#             if n.value == value:
#                 break
#             n = n.ref
        
#         if n.ref is None:
#             return 'not found'
        
#         else:
#             n.ref = n.ref.ref

#     def reverse(self):
#         prev = None
#         current = self.head
#         while current:
#             next_node = current.ref
#             current.ref = prev
#             prev = current
#             current = next_node

#         self.head = prev

#     def middle(self):
#         slow = self.head
#         fast = self.head
#         while fast and fast.ref and fast.ref.ref: #the extra fast.ref.ref is for finding if ll is has even nodes and to find first middle.
#             slow = slow.ref
#             fast = fast.ref.ref
        
#         return slow.value

        

# def summ(arr):
#     if len(arr)<1:
#         return 0

#     return arr[0] + summ(arr[1:])

# arr = [10,20,30,40]

# print(summ(arr))



# def fibonacci(num):
#     if num <=1:
#         return num

#     return fibonacci(num-1)+fibonacci(num-2)

# def print_fib(n):
#     for i in range(n+1):
#         print(fibonacci(i),end=' ')

# print_fib(10)



# class Maxheap:
#     def __init__(self):
#         self.heap = []

#     def insert(self,value):
#         self.heap.append(value)
#         self.heapify_up(len(self.heap)-1)

#     def heapify_up(self,index):
#         parent = (index-1)//2

#         if index > 0 and self.heap[parent] < self.heap[index]:
#             self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
#             self.heapify_up(parent)

#     def get_max(self):
#         if self.heap is None:
#             return None
#         if len(self.heap)==1:
#             return self.heap.pop()
        
#         max_value = self.heap[0]
#         self.heap[0]=self.heap.pop()
#         self.heapify_down(0)
#         return max_value

#     def heapify_down(self,index):
#         largest = index
#         left = index * 2 +1
#         right = index * 2 + 2

#         if left < len(self.heap) and self.heap[largest] < self.heap[left]:
#             largest = left

#         if right < len(self.heap) and self.heap[largest] < self.heap[right]:
#             largest = right

#         if largest != index:
#             self.heap[largest],self.heap[index]=self.heap[index],self.heap[largest]
#             self.heapify_down(largest)



# h = Maxheap()
# h.insert(10)
# h.insert(20)
# h.insert(5)
# h.insert(30)

# print(h.heap)

# print(h.get_max())
# print(h.heap)

