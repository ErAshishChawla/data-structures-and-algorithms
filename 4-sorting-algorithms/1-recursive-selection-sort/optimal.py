def recursiveSelectionSort(arr, i):
    if i >= len(arr):
        return

    # This array checks if array of current min_index
    # is greater than the pointer then it changes the min_index
    # If the pointer exhausts the min_index is returned
    def findMinIndex(arr, min_index, j):
        if j >= len(arr):
            return min_index

        if arr[min_index] > arr[j]:
            return findMinIndex(arr, j, j+1)
        
        return findMinIndex(arr, min_index, j+1)
    
    # We need to find min index, we have a start of min_index and 
    # search area start as well. 
    min_idx = findMinIndex(arr, i, i+1)

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return recursiveSelectionSort(arr, i+1)

def recursiveSelectionSortDesc(arr, i):
    # Same as asc, just we need to find max element
    if i >= len(arr):
        return

    def findMaxIndex(arr, max_index, j):
        if j >= len(arr):
            return max_index

        if arr[j] > arr[max_index]:
            return findMaxIndex(arr, j, j+1)

        return findMaxIndex(arr, max_index, j+1)

    max_index = findMaxIndex(arr, i, i+1)

    arr[i] , arr[max_index] = arr[max_index], arr[i]

    return recursiveSelectionSortDesc(arr, i+1)

def recursiveSelectionSortSingle(arr:list[int], i:int , j:int, min_index:int):
    if i >= len(arr):
        return

    if j >= len(arr):
        arr[i], arr[min_index] = arr[min_index], arr[i]
        return recursiveSelectionSortSingle(arr, i+1, i+1, i+1)

    # this stops the i from incrementing until j loop is complete
    if arr[min_index] > arr[j]:
        return recursiveSelectionSortSingle(arr, i, j+1, j)
    
    return recursiveSelectionSortSingle(arr, i,j+1, min_index)



arr1 = [5,7,8,4,1,6,9,2]
arr2 = [5,7,8,4,1,6,9,2]
arr3 = [5,7,8,4,1,6,9,2]
recursiveSelectionSort(arr1, 0)
recursiveSelectionSortDesc(arr2, 0)
recursiveSelectionSortSingle(arr3, 0, 0, 0)
print(arr1)
print(arr2)
print(arr3)

