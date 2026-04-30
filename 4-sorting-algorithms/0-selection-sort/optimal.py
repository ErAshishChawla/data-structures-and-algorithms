def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def selectionSortDesc(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

arr1 = [5,7,8,4,1,6,9,2]
arr2 = [5,7,8,4,1,6,9,2]
selectionSort(arr1)
selectionSortDesc(arr2)
print(arr1)
print(arr2)