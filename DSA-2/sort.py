# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]

# arr=[20,30,10,50,40]
# bubble_sort(arr)
# print(arr)


# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_pos=i
#         for j in range(i+1,n):
#             if arr[j] < arr[min_pos]:
#                 min_pos=j
        
#         arr[i],arr[min_pos]=arr[min_pos],arr[i]

# arr = [30,60,10,20,50,40]
# selection_sort(arr)
# print(arr)


# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1,n):
#         j = i
#         while j > 0 and arr[j-1] > arr[j]:
#             arr[j-1],arr[j]=arr[j],arr[j-1]
#             j-=1

# arr = [30,60,10,20,50,40]
# insertion_sort(arr)
# print(arr)


# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr

#     smallest = []
#     largest = []
#     pivot=arr[-1]
#     for i in range(len(arr)-1):
#         if pivot >= arr[i]:
#             smallest.append(arr[i])
#         if pivot < arr[i]:
#             largest.append(arr[i])
    
#     return quicksort(smallest) + [pivot] + quicksort(largest)

# arr = [30,60,10,20,50,40]
# print(quicksort(arr))


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr)//2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     return merge(left,right)



# def merge(left,right):
#     result = []
#     i=j=0

#     while i<len(left) and j<len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
    
#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# arr = [10,50,20,60,40,30]
# a = merge_sort(arr)
# print(a)



students = [
    {"id": 1, "name": "Alice", "age": 20, "math": 95},
    {"id": 2, "name": "Bob", "age": 21, "math": 85},
    {"id": 3, "name": "Charlie", "age": 19, "math": 88}
]

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    smallest = []
    largest = []
    pivot = arr[-1]  # last element as pivot
    for i in range(len(arr) - 1):
        if pivot["age"] >= arr[i]["age"]:
            smallest.append(arr[i])
        else:
            largest.append(arr[i])
    
    return quicksort(smallest) + [pivot] + quicksort(largest)

sorted_students = quicksort(students)

for s in sorted_students:
    print(s)