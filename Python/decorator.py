# def decorator(alpha):
#     def wrapper(name):
#         print(f'before function run{name}')
#         alpha(name)
#         print(f'after function run{name}')

#     return wrapper

# @decorator
# def say_hello(name):
#     print(f'hello {name}')

# say_hello('nihas')



# def decorator(alpha):
#     def wrapper(a,b):
#         print((a+b)//2)
#         alpha(a,b)
#         print((a+b)*2)

#     return wrapper

# @decorator
# def sum_dec(a,b):
#     print(a+b)

# sum_dec(4,2)



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


# def decorator(alpha):
#     def wrapper(name1,name2):
#         name1 = name1.upper()
#         name2 = name2.upper()
#         name3 = name1+' '+name2
#         print(name3)
#     return wrapper

# @decorator
# def say_name(name1,name2):
#     print(name1,name2)

# say_name('nihas','ali')


# def decorator(alpha):
#     def wrapper(name1,name2):
#         name1 = name1[0]+name1[1].upper()+name1[2:]
#         name2 = name2.upper()
#         name3 = name1+' '+name2
#         print(name3)
#     return wrapper

# @decorator
# def say_name(name1,name2):
#     print(name1,name2)

# say_name('nihas','ali')



# def decorator(alpha):
#     def wrapper(name):
#         print(name[::-1])
#     return wrapper

# @decorator
# def words(name):
#     print(name)

# words('nihas')


# def decorator(alpha):
#     count = 0
#     def wrapper(name):
#         nonlocal count
#         count +=1
#         print(count,name)

#     return wrapper

# @decorator
# def fun(name):
#     print(name)

# fun('nihas')
# fun('ali')
# fun('k')



# import time

# def execution_timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()   # start time
#         result = func(*args, **kwargs)
#         end = time.perf_counter()     # end time
#         print(f"Execution time: {end - start:.5f} seconds")
#         return result
#     return wrapper


# @execution_timer
# def slow_function():
#     total = 0
#     for i in range(1, 10_000_00):  # just a big loop to make it slow
#         total += i
#     return total


# slow_function()



# def numbers():
#     for i in range(1,11):
#         yield(i)

# for n in numbers():
#     print(n)


# def count_n(n):
#     for i in range(1,n+1):
#         yield(i)

# for num in count_n(5):
#     print(num)


# def count_n(n):
#     for i in range(1,n+1):
#         yield(i)

# gen = count_n(5)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))



# import random
# rand_num = lambda : random.randint(1,100)
# print(rand_num())



# import random
# rand_multiple_of_5 = lambda: random.randrange(5, 51, 5)
# print(rand_multiple_of_5())
# print(rand_multiple_of_5())
# print(rand_multiple_of_5())