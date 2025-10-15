# a = 'how are you'
# x = a.split()

# for i in range(0,len(x)):
#     x[i]=x[i][::-1]

# b = ' '.join(x)
# print(b)



# def fact(num):
#     x = 1
#     for i in range(1,num+1):
#         x = i*x
#     return x

# print(fact(4))


# a = 'life is very beutiful'
# x = ''
# y='sssssssssssssssssssssss'
# word = a.split()

# for i in word:
#     if len(i)>len(x):
#         x = i
#     if len(i) < len(y):
#         y = i

# print(x,y)



# a = [10,20,30,40,5,25,45,30,60,28]
# largest = 0
# second = 1
# smallest = 100

# for i in a:
#     if largest < i:
#         second = largest
#         largest = i
#     if i < largest and i > second:
#         second = i

#     if smallest > i:
#         smallest=i

# print(f'largest : {largest},second:{second} , smallest : {smallest}')



# def pal(string):
#     x = ''
#     for i in string:
#         x = i+x
#     return x == string

# print(pal('malayalam'))


# def anagram(string1,string2):
#     a = {}
#     b = {}
#     for i in string1:
#         if i not in a:
#             a[i]=1
#         else:
#             a[i]+=1
#     for i in string2:
#         if i not in b:
#             b[i]=1
#         else:
#             b[i]+=1
    
#     return a==b

# print(anagram('nishsas','sahinss'))


# a = [1,2,3,4,5,2,4,8,1]
# b= {}
# for i in a:
#     if i not in b:
#         b[i]=1
#     else:
#         b[i]+=1

# print(b)



# def mult(num):
#     mul = 1
#     for i in range(1,11):
#         mul = i*num
#         print(f"{num}x{i}={mul}")

# mult(5)


# def fun(word):
#     s=''
#     a = {}
#     for i in word:
#         if i not in a:
#             a[i] = 1

#         else:
#             a[i] +=1
    

#     for i in a:
#         if a[i] ==1:
#             s+=i
#     return s

# b = fun("helloh")
# print(b)



# def fun(word):
#     a = {}
#     for i in word:
#         if i not in a:
#             a[i] = 1

#         else:
#             a[i] +=1
    

#     for i in word:
#         if a[i] ==1:
#             return i 

# b = fun("helloh")
# print(b)


# str1 = 'nihedas'
# func1 = lambda x: x[-1]+x[1:-1]+x[0]
# print(func1(str1))