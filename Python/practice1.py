# def square(arr):
#     arr2=[]
#     return [x for x in arr if x not in arr2 and not arr2.append(x)]

# arr = [1,2,3,4,5,2,4,6]

# print(square(arr))


# class Animal:
#     def Sound(self):
#         print('animal makes sound')
    
# class Dog(Animal):
#     def Bark(self):
#         print('dog barks!')

# x = Dog()

# x.Sound()

# x.Bark()


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print(f'my name is {self.name} and {self.age} old')

# class Student(Person):
#     def __init__(self,name,age,college):
#         super().__init__(name,age)
#         self.college = college

#     def show(self):
#         print(f'my college is {self.college}')

# x = Student('nihas',23,'mes')

# x.display()
# x.show()


# def fun(word):
#     vowels = 'aeiou'
#     count=0
#     for i in word:
#         if i in vowels:
#             count+=1
#     return count

# print(fun('how old are you'))

# def fun(word):
#     count = 0
#     vowels='aeiou'
#     return sum([1 for x in word if x in vowels])

# word = 'hello who are you'
# print(fun(word))


# def square(arr):
#     return [x**2 if x%2==0 else x**3 for x in arr]

# arr=[1,2,3,4,5,6]
# print(square(arr))



# def fun(arr1,arr2):
#     xx=dict(zip(arr1,arr2))
#     print(xx)

# fun([1,2,3,4,5],['q','w','e','r','t'])


# def make_dict(keys,values):
#     return {keys[i]:values[i] for i in range(min(len(keys),len(values)))}

# keys = [1,2,3,4,5]
# values = ['q','w','e','r','t']

# print(make_dict(keys,values))



# def vow_count(word):
#     vowels = 'aeiou'
#     return {v:word.lower().count(v) for v in vowels if word.lower().count(v) > 0}

# print(vow_count('hello World'))

# def vow_count(word):
#     vowels = 'aeiou'
#     return {v: sum(1 for x in word if x==v) for v in vowels if v in word}

# print(vow_count('hello worldaaa'))


# students = [
#     {'name':'nihas','age':22},
#     {'name':'shani','age':24},
#     {'name':'farhas','age':19},
# ]

# students.sort(key=lambda x:x['age'],reverse=True)

# sorted_students = sorted(students,key=lambda x:x['age'])

# def get_age(student):
#     return student["age"]

# # use function as key
# sorted_students = sorted(students, key=get_age)

# print(sorted_students)



# class Number:
#     count = 0
#     def __init__(self):
#         Number.count+=1

# a = Number()
# b = Number()
# c = Number()

# print(Number.count)


# def Decorator(alpha):
#     def wrapper():
#         print('hello')
#         alpha()
#         print('how are you')
#     return wrapper

# @Decorator
# def fun():
#     print('nihas')

# fun()


# def fun():
#     yield 'hai'
#     yield 'hello'
#     yield 'good'

# gen = fun()
# print(next(gen))
# print(next(gen))
# print(next(gen))


# def fun(n):
#     for i in range(1,n+1):
#         yield i

# for num in fun(6):
#     print(num)

# n = 5
# gen=fun(n)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))



# def Decorator(alpha):
#     def wrapper(*args,**kwargs):
#         print('hai')
#         alpha(*args,**kwargs)
#         print('hello')
#     return wrapper

# @Decorator
# def fun(name,age):
#     print(f'my name is {name} and {age} old')

# fun('nihas',22)



# numbers=[1,2,3,4,5,6]
# squares = list(map(lambda x : x**2,numbers))
# result = list(map(lambda x: x**2 if x%2==0 else x**3,numbers))

# print(result)


# def get_numbers():
#     return [1, 2, 3, 4, 5]

# squares = list(map(lambda x: x**2, get_numbers()))
# print(squares)



# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}

# dict1.update(dict2)
# print(dict1)
# merged = {**dict1,**dict2}
# print(merged)



# n=5
# k=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(k,end=' ')
#         k+=1
#     print()


class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")

# Create objects
s1 = Student("Nihas", 20, "S101")
s2 = Student("Rahul", 21, "S102")

# Display info
s1.display_info()
print("----")
s2.display_info()