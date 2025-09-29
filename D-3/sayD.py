# dict1 = {'a':'nihas','b':'janiiiis','c':'khan'}
# longest=''
# long_key = None
# for k,v in dict1.items():
#     if len(v) > len(longest):
#         longest = v
#         long_key = k

# del dict1[long_key]
# print(dict1)



# for k,v in dict1.items():
#     v = v[0] + v[1].upper() + v[2:]
#     dict1[k]=v

# print(dict1)



# def decorator(alpha):
#     def wrapper(name):
#         print(name.upper())
#     return wrapper

# @decorator
# def words(name):
#     print(name)

# words('nihas')



# def decorator(alpha):
#     def wrapper(name):
#         name = name[0] + name[1].upper()+ name[2:]
#         print(name)
    
#     return wrapper

# @decorator
# def Words(name):
#     print(name)

# Words('nihas')



# class Car:
    
#     age = 23
    
#     def __init__(self,name):
#         self.name=name
      
#     def print(self):
#         print(self.name)              
#         print(Car.age)
        
#     @classmethod
#     def show(cls):
#         print(cls.age)


# class Company(Car):
    
#     def __init__(self,title,name):
#         self.title=title
#         super().__init__(name)
        
    
#     def hello(self):
#         self.print()
#         print(Car.age)

# obj = Company('Tata','ijaz') 
# obj.hello()


# class Counter():
#     count = 0
#     def __init__(self):
#         Counter.count +=1

# a = Counter()
# d = Counter()
# b = Counter()
# c = Counter()

# print(Counter.count)



# class Parent():
#     class_var = 'i am a parent class variable'

#     def __init__(self,name):
#         self.name = name

# class Child(Parent):
#     def show_var(self):
#         print(Parent.class_var)

# obj1 = Child('nihas')
# print(obj1.name)
# obj1.show_var()



# class Hashmap:
#     def __init__(self,size):
#         self.size = size
#         self.table = [[] for x in range(size)]

#     def hash_function(self,key):
#         return hash(key)%self.size

#     def insert(self,key,value):
#         index = self.hash_function(key)
#         self.table[index].append((key,value))

#     def get(self,key):
#         index = self.hash_function(key)
#         for k in self.table[index]:
#             if k[0] == key:
#                 return k[1]

#         return 'not found'

#     def delete(self,key):
#         index = self.hash_function(key)
#         for i,(k,v) in enumerate(self.table[index]):
#             if k == key:
#                 self.table[index].pop(i)
#                 return True
#         return False


#     def display(self):
#         for k,v in enumerate(self.table):
#             print(f'{k}:{v}')


# ht = Hashmap(5)
# ht.insert('name','nihas')
# ht.insert('age',22)
# ht.insert('place','wayanad')
# print(ht.get('name'))
# ht.display()
# print('hai')
# ht.delete('place')
# ht.display()


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self,value):
#         self.root = self.insert_rec(self.root,value)

#     def insert_rec(self,node,value):
#         if node is None:
#             return Node(value)

#         if value < node.value:
#             node.left = self.insert_rec(node.left,value)

#         elif value > node.value:
#             node.right = self.insert_rec(node.right,value)

#         return node

#     def search(self,value):
#         return self.search_rec(self.root,value)

#     def search_rec(self,node,value):
#         if node is None:
#             return 'not found'

#         if node.value == value:
#             return True

#         if value < node.value:
#             return self.search_rec(node.left,value)

#         if value > node.value:
#             return self.search_rec(node.right,value)

#     def delete(self,value):
#         self.root = self.delete_rec(self.root,value)

#     def delete_rec(self,node,value):
#         if node is None:
#             return None

#         if value < node.value:
#             node.left = self.delete_rec(node.left,value)

#         elif value > node.value:
#             node.right = self.delete_rec(node.right,value)

#         else:
#             if node.left is None:
#                 return node.right

#             if node.right is None:
#                 return node.left

#             min_large = self.get_min(node.right)
#             node.value = min_large.value
#             node.right = self.delete_rec(node.right,min_large.value)

#         return node

#     def get_min(self,node):
#         while node.left:
#             node = node.left

#         return node

#     def inorder(self):
#         self.inorder_rec(self.root)

#     def inorder_rec(self,node):
#         if node:
#             print(node.value,end=' ')
#             self.inorder_rec(node.left)
#             self.inorder_rec(node.right)

# bst = BST()
# bst.insert(50)
# bst.insert(30)
# bst.insert(70)
# bst.insert(20)
# bst.insert(40)
# bst.insert(60)
# bst.insert(80)

# print(bst.search(40))
# print(bst.search(90))

# print('hai')

# bst.inorder()

# bst.delete(40)
# bst.delete(60)
# print('hai')
# bst.inorder()
