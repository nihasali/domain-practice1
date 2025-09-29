# def rev(string):
#     if len(string)<=0:
#         return ''
#     else:
#         return rev(string[1:]) + string[0]

# print(rev(input('enter the element: ')))


# def fact(num):
#     if num ==1:
#         return 1
#     else:
#         return num * fact(num-1)

# print(fact(5))


# def pal(string):
#     if len(string) <= 0:
#         return True
#     if string[0] != string[-1]:
#         return False
    
#     return pal(string[1:-1])

# print(pal(input('enter the value : ')))



# def summ(a):
#     if len(a) <= 0:
#         return 0
#     else:
#         return a[0]+summ(a[1:])

# a = [1,2,3,4,5,6]

# print(summ(a))


# def find_largest(arr,index=0,largest=None,second=None):
#     if len(arr)==index:
#         return largest,second

#     current = arr[index]
#     if largest is None or current > largest:
#         second = largest
#         largest = current
#     if current != largest and (second < largest or second is None):
#         second = current

#     return find_largest(arr,index+1,largest,second)


# a,b=find_largest([10,50,60,20,40,90,35,58,87,96])
# print(a,b)


# def remove_l(string):
#     if len(string)==0:
#         return ''
#     if string[0]=='l':
#         return remove_l(string[1:])
#     else:
#         return string[0] + remove_l(string[1:])


# print(remove_l('hlellol'))


# def remov_dup(string,seen=''):
#     if len(string)==0:
#         return ''
    
#     if string[0] in seen:
#         return remov_dup(string[1:],seen)
#     else:
#         return string[0]+remov_dup(string[1:],seen+string[0])


# print(remov_dup('hlellouh world'))



# def linear_search(arr,target,index=0):
#     if len(arr)==index:
#         return -1

#     if arr[index] == target:
#         return index
#     else:
#         return linear_search(arr,target,index+1)

# print(linear_search([1,2,3,4,5,6,7],4))



# def binary_search(arr,target,low,high):
#     if low > high:
#         return -1
    
#     mid = (low+high)//2
#     if arr[mid]==target:
#         return mid

#     if target < arr[mid]:
#         return binary_search(arr,target,low,mid-1)
    
#     if target > arr[mid]:
#         return binary_search(arr,target,mid+1,high)

# arr  = [1,2,3,4,5,6]
# target =3

# print(binary_search(arr,target,0,len(arr)-1))


# def fibbonacci(num):
#     if num <= 1:
#         return num
#     else:
#         return fibbonacci(num-1)+fibbonacci(num-2)

# def print_fib(num):
#     for i in range(num+1):
#         print(fibbonacci(i),end=' ')

# print_fib(10)