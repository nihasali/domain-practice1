# class Car:
#     price = 1000

#     def __init__(self,name):
#         self.name = name

#     def print_l(self):
#         print('parent class is called')
#         print(self.name)
#         print(Car.price)

# class Vehicle(Car):
#     def __init__(self,name):
#         self.name = name
#         super().__init__(name)

#     def show_p(self):
#         self.print_l()

# obj1 = Vehicle('honda')
# obj1.show_p()



# dict1 = {'a':'nihas','b':'janiiiis','c':'khan'}

# max_length = 0
# max_key = None
# for k,v in dict1.items():
#     if len(v) > max_length:
#         max_length = len(v)
#         max_key = k

# del dict1[max_key]
# print(dict1)

# for k,v in dict1.items():
#     v = v[0] + v[1].upper() + v[2:]
#     dict1[k] = v

# print(dict1)



# def delete(self,key):
#     index = self.hash_function(key)
#     for i,(k,v) in enumerate(self.table[index]):
#         if k == key:
#             self.table[index].pop(i)
#             return True

#     return False


# def delete(self,value):
#     self.root = self.delete_rec(self.root,value)

# def delete_rec(self,node,value):
#     if not node:
#         return None

#     if value < node.value:
#         node.left = self.delete_rec(node.left,value)

#     elif value > node.value:
#         node.right = self.delete_rec(node.right,value)

#     else:
#         if not node.left:
#             return node.right
#         if not node.right:
#             return node.left

#         min_large = self.get_v(node.right)
#         node.value = min_large.value
#         node.right = self.delete_rec(node.right,min_large.value)

#     return node

# def get_v(self,node):
#     while node.left:
#         node = node.left

#     return node



# def summ(arr):
#     if len(arr)==0:
#         return 0

#     return arr[0]+summ(arr[1:])

# arr=[1,2,3,4,5]
# print(summ(arr))




