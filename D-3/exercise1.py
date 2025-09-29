# import random

# num = random.randint(1,100)
# num1 = random.randrange(5,101,5)
# print(num1)


# a = 'abc123'
# for i in a:
#     if i.isdigit():
#         print(i)



# def fibbonacci(num):
#     if num <=1:
#         return num

#     return fibbonacci(num-1) + fibbonacci(num-2)

# def print_fib(n):
#     for i in range(n+1):
#         print(fibbonacci(i),end=' ')

# print_fib(10)



# a = 'my name is nihas'
# result = ''

# for i in a:
#     if a.count(i)==2:
#         result += i.upper()
#     else:
#         result += i

# print(result)



# def sum_arr(arr):
#     if len(arr)==0:
#         return 0

#     return arr[0] + sum_arr(arr[1:])

# print(sum_arr([1,2,3,4,5]))



# str1 = 'name is nihas'
# dict1 = {}
# for i in str1:
#     if i not in dict1 and i != ' ':
#         dict1[i]=1
#     elif i in dict1 and i != ' ':
#         dict1[i]+=1

# print(dict1)



# str1 = 'name is nihaas'
# dict1 = {}
# result = ''
# for i in str1:
#     if i not in dict1:
#         dict1[i]=1
#         result+=i
#     else:
#         dict1[i]+=1
#         if dict1[i]==2:
#             result+=i.upper()
#         else:
#             result+=i

# print(result)



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