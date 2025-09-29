# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr)//2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     return merge(left,right)

# def merge(left,right):
#     i=j=0
#     result = []
#     while i < len(left) and j < len(right):
#         if left[i]<=right[j]:
#             result.append(left[i])
#             i +=1
#         else:
#             result.append(right[j])
#             j +=1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# arr = [30,20,40,10,50]
# print(merge_sort(arr))



# def quicksort(arr):
#     if len(arr) <=1:
#         return arr

#     pivot = arr[-1]
#     smallest = []
#     largest = []
#     for i in range(len(arr)-1):
#         if arr[i] < pivot:
#             smallest.append(arr[i])
#         else:
#             largest.append(arr[i])

#     return quicksort(smallest)+[pivot]+quicksort(largest)

# arr = [30,20,40,10,50]
# print(quicksort(arr))