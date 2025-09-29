class Stack:
    def __init__(self):
        self.item = []
    
    def push(self,data):
        self.item.append(data)
    
    def pop(self):
        if self.is_empty():
            return 'deletion not possible!'

        return self.item.pop()
    
    def peek(self):
        if self.is_empty():
            return 'stack is empty'
        
        return self.item[-1]


    def size(self):
        return len(self.item)
    
    def is_empty(self):
        return len(self.item)==0

    def print(self):
        print(self.item[::-1])
   
    # @staticmethod
    # def reverse_stack(orginal_stack):
    #     reversed = Stack()
    #     while not orginal_stack.is_empty():
    #         item = orginal_stack.pop()
    #         reversed.push(item)
        
    #     return reversed

    def reverse_stack(self):
        reversed_stack = Stack()
        while not self.is_empty():
            item = self.pop()
            reversed_stack.push(item)
        return reversed_stack

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.print()
s.print()
print(s.is_empty())
print(s.peek())

# rev = Stack.reverse_stack(s)
# rev.print()

print("Reversed stack:")
rev = s.reverse_stack()
rev.print()




# def rev_string(s):
#     stack = []

#     for i in s:
#         stack.append(i)
    
#     rev_str = ''
#     while stack:
#         rev_str += stack.pop()

#     return rev_str

# a = "hello"
# print(rev_string(a))



# def isvalid(s):
#     stack = []
#     dictt = {')':'(',']':'[','}':'{'}

#     for i in s:
#         if i in dictt:
#             if not stack or stack[-1]!=dictt[i]:
#                 return False
            
#             stack.pop()

#         else:
#             stack.append(i)
    
#     return len(stack)==0

# s = "{[()]}"
# print(isvalid(s))





