# list1 = [x for x in range(1,11) if x%2==0]
# print(list1)

# list2 = map(lambda x:x**2,list1)
# print(list(list2))


# arr = [1,2,3,4,5,6,2,7,4,1,1]
# dict1 = {}
# for i in arr:
#     if i not in dict1:
#         dict1[i]=1
#     else:
#         dict1[i]+=1

# print(dict1)



# a = [1, 3, 5, 7]
# b = [2, 4, 6, 8]

# c = sorted(a+b)
# print(c)



# def decorator(alpha):
#     def wrapper(name):
#         print(f'how are you {name}')
#         alpha(name)
#         print('bye')

#     return wrapper

# @decorator
# def fun(name):
#     print(f'{name} says fine')

# fun('nihas')


# def decorator(alpha):
#     def wrapper(name1,name2):
#         name3 = name1.upper()+' '+name2
#         print(name3)
#     return wrapper
# @decorator
# def fun(name1,name2):
#     print(nam1,name2)

# fun('nihas','ali')




# arr = [1,2,3,4,5,6,2,7,4,1,1]

# list1 = [x for x in arr if arr.count(x)==1]
# list2 = [x for x in set(arr)]
# print(list2)



# str1 = 'my name is nihas'
# vowels = 'aeiuo'
# list1 = {k:str1.count(k) for k in str1 if k in vowels}

# print(list1)


# class student:
#     def __init__(self,name,place,age):
#         self.name=name 
#         self.place = place
#         self.age = age

#     def show_details(self):
#         print(f'{self.name} - {self.place} - {self.age}')

# stud1 = student('nihas','wayanad',22)
# stud2 = student('jan','kochi',19)
# stud1.show_details()
# stud2.show_details()


# class parent:
#     def name(self,name):
#         print(f'{name} is parent')

# class child(parent):
#     def cname(self,name):
#         print(f'{name} is child')

# x = child()
# x.name('nihas')
# x.cname('jan')


# dict1 = {'a':1,'b':2,'c':3}
# dict2 = {'d':4,'e':5,'a':2}


# merged = dict1.copy()

# for k,v in dict2.items():
#     if k in merged:
#         merged[k] +=v
#     else:
#         merged[k]=v

# print(merged)



# num = 1
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(num,end=' ')
#         num+=1
#     print()



# a = [1, 3, 5, 7]
# b = [2, 4, 6, 8]

# dict1 = dict(zip(a,b))
# print(dict1)


# class Counter:
#     count = 0

#     def __init__(self):
#         Counter.count+=1

# a = Counter()
# b = Counter()
# c = Counter()
# d = Counter()
# print(Counter.count)



# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None


# def height(root):
#     if root is None:
#         return 0

#     return 1 + max(height(root.left),height(root.right))

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left=Node(4)
# root.left.left.left = Node(5)

# print(height(root))


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.nref = None
#         self.nref = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def print_ll(self):
#         if self.head is None:
#             return None

#         n = self.head
#         while n is not None:
#             print(n.value,end=' ')
#             n = n.nref

#     def insert(self,value):
#         new_node = Node(value)
#         new_node.nref = self.head
#         if self.head is not None:
#             self.head.pref = new_node
#         self.head = new_node

#     def middle(self):
#         slow = self.head
#         fast = self.head
#         while fast and fast.nref:
#             slow = slow.nref
#             fast = fast.nref.nref

#         return slow.value

# ll1 = Linkedlist()
# ll1.insert(10)
# ll1.insert(20)
# ll1.insert(30)
# ll1.insert(40)
# ll1.insert(50)

# ll1.print_ll()
# def summ(arr):
#     if len(arr)==0:
#         return 0

#     return arr[0]+summ(arr[1:])

# arr=[1,2,3,4,5]
# print(summ(arr))
# print('middle = ')
# print(ll1.middle())


# class Maxheap:
#     def __init__(self):
#         self.heap = []

#     def insert(self,value):
#         self.heap.append(value)
#         self.heapify_up(len(self.heap)-1)

#     def heapify_up(self,index):
#         parent = (index-1)//2

#         if index > 0 and self.heap[parent]<self.heap[index]:
#             self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
#             self.heapify_up(parent)

# hp1 = Maxheap()
# hp1.insert(10)
# hp1.insert(20)
# hp1.insert(5)
# hp1.insert(15)
# print(hp1.heap)