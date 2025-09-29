# 1)input = [10,20,30,40,50]
#  output = [30,10,20,40,50]

# def fun(input1):
#     for i in range(2,0,-1):
#         input[i],input[i-1]=input[i-1],input[i]
#     return input
# input=[10,20,30,40,50]
# val=fun(input)
# print(val)


# 2) third largest
# def fun(new):
#     largest=float('-inf')
#     second=float('-inf')
#     third=float('-inf')
#     for num in new:
#         if num>largest:
#             third=second
#             second=largest
#             largest=num
#         elif num>second and  num!=largest:
#             third=second
#             second=num
#         elif num>third and num !=second and num !=first:
#             third=num
#     return second
# new=[27, 83, 14, 96, 51, 62, 7, 39, 88, 45]
# val=fun(new)
# print(val)
# 4)Delete prime number in the array without using methods and should update original array
# from  math import sqrt
# def fun(nums):
#     i=0
#     while i<len(nums):
#         num=nums[i]
#         if num<2:
#             i+=1
#             continue
#         is_prime=True
#         for j in range(2,int(sqrt(num))+1):
#             if num%j==0:
#                 is_prime=False
#                 break
#         if is_prime:
#             del nums[i]
#         else:
#             i+=1
#     return nums    
    
# nums=[3, 17, 42, 8, 95, 61, 27, 14, 73, 5]
# val=fun(nums)
# print(val)

# #remove max value key
# my_dict={'a':10,'b':5,'c':14,'d':10}
# max_value=None
# key=None
# for k,v in my_dict.items():
#   if max_value is None or v>max_value:
#     max_value=v
#     key=k
# if key is not None:
#   del my_dict[key]
# print(my_dict)

# 5)Sort a array by using while loop
# nums = [42, 3, 17, 8, 95, 61, 27, 14, 73, 5]
# i=0
# n=len(nums)
# while i<n-1:
#     j=0
#     while j<n-i-1:
#         if nums[j]>nums[j+1]:
#             nums[j],nums[j+1]=nums[j+1],nums[j]
#         j+=1
#     i+=1
# print(nums)
# 6)sort array by using for loop
# nums = [42, 3, 17, 8, 95, 61, 27, 14, 73, 5]
# n=len(nums)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if nums[j]>nums[j+1]:
#             nums[j],nums[j+1]=nums[j+1],nums[j]
# print(nums)
# 7)Let a =[1,2,3,4,5]
# Let b =[3,4,7,8]

# Find the the non-common numbers
# a=[1,2,3,4,5,6]
# b=[3,4,7,8]
# res=[]
# for i in a:
#     if i not in b:
#         res.append(i)
# print(res)
# 8)write the string in to revise by word.
# word="how are you"
# res=" ".join(word[::-1] for word in words.split())
# print(res)
# 9)merge two dict
# dict1={"a":1,"b":2}
# dict2={"c":3,"d":4}
# dict1.update(dict2)
# print(dict1)
# 10)If two dictionaries have the same key, and you want to add the values instead of overwriting
# dict1 = {"a": 10, "b": 20, "c": 30}
# dict2 = {"b": 5, "c": 15, "d": 25}
# merged=dict1.copy()
# for k,v in dict2.items():
#     if k in merged:
#         merged[k]+=v
#     else:
#         merged[k]=v
# print(merged)
# 11)find frequency of an list and find the max value of the list.
# nums=[12, 47, 5, 89, 23, 61, 34, 76, 3, 58]
# frq={}
# for i in nums:
#     if i in frq:
#         frq[i]+=1
#     else:
#         frq[i]=1
# maximum=nums[0]
# for i in nums:
#     if i>maximum:
#         maximum=i
# print(frq)
# print(maximum)
# 12)sort a list of dict
# students = [
#     {"name": "Alice", "age": 22, "marks": 82},
#     {"name": "Bob", "age": 22, "marks": 82},
#     {"name": "Charlie", "age": 23, "marks": 78},
#     {"name": "David", "age": 24, "marks": 88}
# ]
# this case is age is ascending and marks is descending 

# def compare(a,b):
#     if a["age"]!=b["age"]:
#         return a["age"]>b["age"]
#     elif a["marks"]!=b["marks"]:
#         return a["marks"]<b["marks"]
#     else:
#         return a["name"]>b["name"]
# n=len(students)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if compare(students[j],students[j+1]):
#             students[j],students[j+1]=students[j+1],students[j]
# for s in  students:
#     print(s)
# students = [
#     {"name": "Alice", "age": 22, "marks": 95},
#     {"name": "Bob", "age": 21, "marks": 70},
#     {"name": "Charlie", "age": 23, "marks": 50},
#     {"name": "David", "age": 24, "marks": 40}
# ]

# new = sorted(students, key=lambda x: (x["age"], x["marks"]))
# print(new)
# 👉 Output:

# bash
# Copy code
# [{'name': 'Bob', 'age': 21, 'marks': 70},
#  {'name': 'Alice', 'age': 22, 'marks': 95},
#  {'name': 'Charlie', 'age': 23, 'marks': 50},
#  {'name': 'David', 'age': 24, 'marks': 40}]
# Notice:
# Bob comes first because 21 < 22 < 23 < 24 (age decides order).

# Even though Alice has higher marks than Bob, she’s after Bob, because her age is higher.

# Marks only matter if two students have the same age.
# 14)find the frequency of the array without dict.
# ✅ Method 1: Using set() and count()
# arr = [1, 2, 2, 3, 1, 4, 2, 3, 5]

# for num in set(arr):   # unique elements
#     print(num, "→", arr.count(num))


# 👉 Output:

# 1 → 2
# 2 → 3
# 3 → 2
# 4 → 1
# 5 → 1


# set(arr) gives unique elements.

# .count(num) counts how many times each appears.

# Method 2: Manual Loop (without dict, using a visited list)
# arr = [1, 2, 2, 3, 1, 4, 2, 3, 5]
# visited = []

# for i in range(len(arr)):
#     if arr[i] not in visited:
#         count = 0
#         for j in range(len(arr)):
#             if arr[i] == arr[j]:
#                 count += 1
#         print(arr[i], "→", count)
#         visited.append(arr[i])
# 15)give an example of decorator.
# def my_decorator(func):
#     def wrapper():
#         print("before the function runs")
#         func()
#         print("after the function runs")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("hello")
# say_hello()

# from datetime import datetime
# from zoneinfo import ZoneInfo
# import time
# def time_it(func):
#     def wrapper():
#         tz=ZoneInfo("Asia/Kolkata")
#         start=datetime.now(tz)
#         print("Start:",start.strftime("%H:%M:%S"))
#         func()
#         end=datetime.now(tz)
#         print("End :",end.strftime("%H:%M:%S"))
#         print(f"Execution time is {(end-start).total_seconds():.4f}seconds")
#     return wrapper
# @time_it
# def slow_function():
#     print("starting the slow function")
#     time.sleep(2)
#     print("finished the slow function")
# slow_function()
# def logger(func):
#     def wrapper(*args,**kwargs):
#         print(f"start:with {args},{kwargs}")
        
#         result=func(*args,**kwargs)
      
#         print(f"{result}")
        
        
#     return wrapper

# @logger
# def add(a,b):
#     return a+b

# @logger
# def greet(name,greeting="hello"):
#     return f"{greeting} {name} !"
# add(5,7)
# greet("Alice",greeting="Hi")

# 16)Generator
# def fun(n):
#     cnt=1
#     while cnt<=n:
#         yield cnt
#         cnt+=1
# gen=fun(10)
# for i in gen:
#     print(i)
# 17)find the area of a rectangle
# class rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         print(self.length * self.breadth)
# rect=rectangle(12,14)
# rect.area()
# 18)reverse a list
# numbers = [1, 2, 3, 4, 5]
# num=numbers[::-1]
# print(num)
# 19)create a function that return the two varible division
# def div(a,b):
#     res=a/b
#     return res
# new=div(12,4)
# print(new)
# 20)try:
#     num=int(input("Enter the num to divide by 10 :"))
#     result=10/num
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except Exception as e:
#     print(f"something happened:{e}")
# else:
#     print(result)
# finally:
#     print("this part always run")
# 21)kth largest element:
# arr = [3, 1, 4, 2, 5]
# k=2
# largest=[]
# for num in arr:
    
#     if len(largest)<k:
#         largest.append(num)
#     else:
#         min_largest=min(largest)
#         if num>min_largest:
#             largest.remove(min_largest)
#             largest.append(num)
# kth_largest=min(largest)
# print(kth_largest)
# 22)# 2. find the frequency of the array string give the count of the which only one
# def count_char(str1):
#     char_count={}
#     for char in str1:
#         if char in char_count:
#             char_count[char]+=1
#         else:
#             char_count[char]=1
#     return char_count
# string="google.com"
# char_count=count_char(string)
# only_once=[]
# for k,v in char_count.items():
#     if v==1:
#         only_once.append(k)
# print(only_once)
# 23)# Count and display the vowels of a given word
# def vowel_count(str1):
#   count={}
#   vowel="aeiou"
#   for letter in str1:
#     if letter in vowel:
#       if letter in count:

#         count[letter]+=1
#       else:

#         count[letter]=1
#   return count
# #count and display vowels in text      
# def vowel_count(str1):
#     vowel="aeiouAEIOU"
#     total_vowel=[letter for letter in str1 if letter in vowel]
#     unique=[]
#     for letter in total_vowel:

# if letter not in unique:
#             unique.append(letter)
#     total_count=len(total_vowel)
#     return unique,total_count

# unique,total_count=vowel_count("Welcome to w3resource.com")
# print(unique)
# print(total_count)
# # Write a Python program to capitalize the first and last letters of each word in a given string.
# def first_last(str1):
#     result=[]
#     for word in str1.split():
#         if len(word)==1:
#             result.append(word)
#         else:
#             result.append(word[0].upper()+word[1:-1]+word[-1].upper())
#     return " ".join(result)
# print(first_last("hello world python"))
# string palindrome if true then return in list 1 else 0
# def new(str1):
#     reverse=""
#     for i in str1:
#         reverse=i+reverse
#     if str1==reverse:
#         return "Palindrome"
#     else:
#         return "not palindrome"
# print(new("madam"))

# def is_palindrom(str1):
#     reverse=[]
#     for i in str1:
#         reverse=[i]+reverse
#     if str1==reverse:
#         return "Palindrome"
#     else:
#        return "not palindrome"

# new=[1,2,2]
# print(is_palindrom(new))
 
# def first_non_repeating_character(str1):
#     ctr={}
#     char_order=[]
#     for c in str1:
#         if c in ctr:
#             ctr[c]+=1
#         else:
#             ctr[c]=1
#             char_order.append(c)
#     for c in char_order:
#         if ctr[c]==1:
#             return c
#     return None
# print(first_non_repeating_character("swiss"))

# swap first and last letter of string using lambda function
# new=lambda s:s[-1]+s[1:-1]+s[0] if len(s)>1 else s

# string="hello"
# print(new(string))
# # remove duplicates
# def remove_duplicates(list1):
#     dup=set()
#     unique=[]
#     for i in list1:
#         if i not in dup:
#             unique.append(i)
#             dup.add(i)
#     return unique
# list1=[-12,20,-27,20,45,-12,60]
# print(remove_duplicates(list1))

# remove an element
# def remove_element(nums,val):
#     k=0
#     for i in range(len(nums)):
#         if nums[i]!=val:
#             nums[k]=nums[i]
#             k+=1
#     return nums[:k]
# list1=[-12,20,-27,20,45,-12,60]

# factorial using recursion 
# def factorial(n):
#     if n<=1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

# fiboncii
# def fib(n):
#     a,b=0,1
#     for _ in range(n):
#         print(a,end=" ")
#         a,b=b,a+b
# fib(5)

# # Write a dictionary comprehension that counts the frequency of each character in the string "hello world"

# word="hello world"
# dict_count={k:word.count(k) for k in word}
# print(dict_count)


# # list to dict conversion
# list1=["apple","cherry","grapes"]
# dict_new={i:list1[i] for i in range(len(list1))}
# print(dict_new)


# # program to print enumerated key values pairs of a list
# list1=["apple","cherry","grapes"]
# dict_new={k:v for k,v in enumerate(list1)}
# print(dict_new)


# # list comprhension to extract non_string values from a list
# list1=[10,"hello","world",True,42,"python",None]
# result=[item for item in list1 if isinstance(item,str)]
# print(result)


# # remove dict keys that hold non-string values
# my_dict = {"a":"apple","b":5,"c":7}

# filtered_dict = {k: v for k, v in my_dict.items() if  isinstance(v, str)}
# print(filtered_dict)
# #generator to print multiples of 5

#   def fun(n,limit):


#     cnt=1
    
#     while cnt<=limit:
#         yield n*cnt
#         cnt+=1
# for i in fun(4,7):
#     print(i)

# floyd traingle:
# n=5
# num=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
    
#     print()
# star pyramid
# n = 5
# for i in range(1, n+1):
#     print(" " * (n-i) + "*" * (2*i-1))
# if we want space between star reduce the count of from (2*i-1) to i and put a space "* "
# inverted pyramid change limit to (n,0,-1)

# collect non-string values in a dict into a tuple
# my_dict = {'a': "apple", 'b': 5, 'c': 14, 'd':"orange"}
# new=tuple(v for v in my_dict.values() if isinstance(v,int))
# print(new)

# collect non-string values in a dict into a tuple

# my_dict = {'a': "apple", 'b': 5, 'c': 14, 'd':"orange"}
# t=()
# for v in my_dict.values():
#     if  isinstance(v,int):
#         t=t+(v,)
# print(t)
# my_dict = {'a': "apple", 'b': 5, 'c': 14, 'd':"orange"}
# new=tuple(v for v in my_dict.values() if isinstance(v,int))
# print(new)


# print only all key value present in the string
# lst = [
#     {"name": "fathima", "age": 19, "course": "python", "location": "thrissur"},
#     {"name": "rahul", "age": 22, "course": "java", "location": "kochi"},
#     {"name": "meera", "age": 20},
#     {"name": "arun", "age": 21}
# ]

# new=[d for d in lst if "course" and "location" in d]
# print(new)

# collect values of specific key into a tuple in a list of dictionary
# result=tuple([d["name"] for d in lst])
# print(result)

# new="i am nafeesath"
# reverse=""
# for i in new.split():
#     reverse=i +" "+ reverse
# print(reverse)

# maximum length value string need to remove
# my_dict={"a":"apple","b":"ball","c":"cat"}

# max_value=None
# key=None
# for k,v in my_dict.items():
#     if max_value is None or len(v)>max_value:
#         max_value=len(v)
#         key=k
# if key is not None:
#     del my_dict[key]
# print(my_dict)
# list of dictionary to dict
# list_of_dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
# new={}
# for d in list_of_dicts:
#     for k,v in d.items():
#         new[k]=v
# print(new)

# list1 = [12, "hi", "hell","cat","execrices", 123]
# maxval=0
# for i in list1:
#     if isinstance(i,str):
#         if len(i)>maxval:
#             maxval=len(i)
# for i in range(len(list1)-1,-1,-1):
#     if isinstance(list1[i],str) and len(list1[i])==maxval:
#         del list1[i]
# print(list1)

# Python program to remove keys with same values in a dictionary.
# d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
# count={}
# for v in d1.values():
#     if v in count:
#         count[v]+=1
#     else:
#         count[v]=1
# result={k:v for k,v in d1.items() if count[v]==1}
# print(result)

# """print even numbers from 100 to 0 using while loop"""
# num = 100
# while num>0:
#     if num%2==0:
#         print(num)
#     num -= 1
# def fizzbuzz(n):
#     result=[]
#     for i in range(1,n+1):
#         if i%15==0:
#             result.append("FizzBuzz")
#         elif i%5==0:
#             result.append("Buzz")
#         elif i%3==0:
#             result.append("Fizz")
#         else:
#             result.append(str(i))
#     return result
# n=15
# print(fizzbuzz(n))

# using class method adding two numbers
# class addition:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print(self.a + self.b)
# add1=addition(12,14)
# add1.add()

# check all argument are same or not 
# def allsame(*args):
#     if not args:
#         return True
#     first=args[0]
#     for arg in args[1:]:
#         if arg!=first:
#             return False
#     return True
# print(allsame(1,2,1))
  
# return firts and alst key of dict in atuple

# def new(my_dict):
#     keys=list(my_dict.keys())
#     return (keys[0],keys[-1])

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(new(my_dict))