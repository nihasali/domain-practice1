students = [
    {
        "id": 1,
        "name": "Alice",
        "age": 20,
        "math": 95
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 21,
        "math": 85
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 19,
        "math": 88
    }
]


max_age=0
max_key = None

for stud in students:
    if stud['age'] > max_age:
        max_age = stud['age']
        max_key = stud

students.remove(max_key)
print(students)



# # sort_stud = sorted(students,key=lambda x: x['age'],reverse=True)
# # print(sort_stud)




# max_student = max(students, key=lambda s: s["age"])
# students.remove(max_student)
# print("Removed student:", max_student)
# print("Remaining students:", students)