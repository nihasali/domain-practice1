students = [
    {
        "id": 1,
        "name": "Alice",
        "age": 20,
        "grade": "A",
        "courses": {"math": 95, "science": 90, "history": 85}
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 21,
        "grade": "B",
        "courses": {"math": 85, "science": 80, "history": 88}
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 19,
        "grade": "B",
        "courses": {"math": 88, "science": 82, "history": 80}
    }
]


# for i in students:
#     print(i['name'])


# a = len(students)
# print(a)

# for i in students:
#     print(i['name'],i['age'])


# for i in students:
#     if i['grade'] == 'B':
#         print(i)


# for i in students:
#     print(i['name'],i['courses']['math'])


# sum=0
# for i in students:
#     sum+=i['age']

# print(sum//len(students))


# largest=0
# high_scorer = None
# for i in students:
#     if i['courses']['math'] > largest:
#         largest = i['courses']['math']
#         high_scorer = i['name']

# print(high_scorer)


# for i in students:
#     courses = i['courses']
#     total = sum(courses.values())
#     avg = total//(len(courses))
#     print(avg,i['name'])


# for stud in students:
#     if stud['courses']['history'] >= 85:
#         print(stud['name'])


# count=0
# for stud in students:
#     if stud['courses']['math'] >86:
#         count+=1

# print(f'count:{count}')


# x= sorted(students,key=lambda x:x['age'], reverse=True)
# print(x)


# sorted_students = sorted(students,key=lambda student: sum(student['courses'].values())/len(student['courses']) , reverse=True)

# for stud in sorted_students:
#     avg = sum(stud['courses'].values())//len(stud['courses'])
#     print(stud['name'],avg)


