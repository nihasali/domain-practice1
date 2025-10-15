# str1 = 'nihedas'
# func1 = lambda x: x[-1]+x[1:-1]+x[0]
# print(func1(str1))


# func = lambda x : 'even' if x%2==0 else 'odd'
# print(func(6))


# func = lambda a,b: a if a>b else b
# print(func(5,8))


# a = [1,2,3,4,5]
# func = map(lambda x: x**2 if x%2==0 else x**3,a)
# print(list(func))


# func = lambda x: True if x[0] in 'aeiou' else False
# print(func('ihas'))


# func = lambda x: True if x[::-1]==x else False
# print(func('madam'))


# func = lambda x: sum(int(i) for i in str(abs(x))) # abs() for handling negative numbers
# print(func(1234))


# func = lambda a,b: a if len(a) > len(b) else b
# print(func('nihas','khanss'))


# func = lambda x: sum(1 for i in x if i in 'aeiou')
# print(func('nihasu'))


# func = lambda x: x[::-1]
# print(func('nihas'))


# list1 = [1,2,3,4,5,6,7]
# even = list(filter(lambda x : x if x%2==0 else None ,list1))
# print(even)


# list1 = [1,2,3,4,5,6,7]
# even = list(filter(lambda x : x%2==0,list1))
# print(even)


# data = [(1,2),(3,9),(4,6)]
# sort_data = sorted(data,key=lambda x: x[1])
# print(sort_data)


# d = {'a':3, 'b':1, 'c':2}
# sorted_items = sorted(d.items(), key=lambda x: x[1])
# print(sorted_items)



# is_anagram = lambda a,b: sorted(a)==sorted(b)
# print(is_anagram('listen','silent'))



