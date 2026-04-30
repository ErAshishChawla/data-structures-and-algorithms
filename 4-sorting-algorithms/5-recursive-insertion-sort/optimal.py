def recursiveInsertionSort(arr, i):
    if len(arr) <=1:
        return

    if i >= len(arr):
        return

    if i == 0:
        return recursiveInsertionSort(arr, i+1)

    if arr[i-1] <= arr[i]:
        return recursiveInsertionSort(arr, i+1)

    def swap_pass(arr, unsorted, j):
        if j < 0:
            arr[j+1] = unsorted
            return 

        if arr[j] > unsorted:
            arr[j+1] = arr[j]
            return swap_pass(arr, unsorted, j-1)
        
        arr[j+1] = unsorted
        return

    swap_pass(arr, arr[i], i-1)

    return recursiveInsertionSort(arr, i+1)

def recursiveInsertionSortDesc(arr, i):
    if len(arr) <=1:
        return

    if i >= len(arr):
        return

    if i == 0:
        return recursiveInsertionSortDesc(arr, i+1)

    if arr[i-1] >= arr[i]:
        return recursiveInsertionSortDesc(arr, i+1)

    unsorted = arr[i]
    j = i-1

    def swap_pass(arr, unsorted, j):
        if j < 0:
            arr[j+1] = unsorted
            return

        if arr[j] < unsorted:
            arr[j+1] = arr[j]
            return swap_pass(arr, unsorted, j-1)

        arr[j+1] = unsorted

        return
    
    swap_pass(arr, unsorted, j)

    return recursiveInsertionSortDesc(arr, i+1)

def recursiveInsertionSortSingle(arr, i, j):
    if i>= len(arr):
        return

    if j >= 0 and arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        return recursiveInsertionSortSingle(arr, i, j-1)

    return recursiveInsertionSortSingle(arr, i+1, i) 

arr1 = [5,7,8,4,1,6,9,2]
arr2 = [5,7,8,4,1,6,9,2]
arr3 = [5,7,8,4,1,6,9,2]
recursiveInsertionSort(arr1, 1)
recursiveInsertionSortDesc(arr2, 1)
recursiveInsertionSortSingle(arr3, 1, 0)
print(arr1)
print(arr2)
print(arr3)
