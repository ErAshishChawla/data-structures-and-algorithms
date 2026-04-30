def recursiveBubbleSort(arr, i):
    if i < 0:
        return
    
    def swap_pass(arr, limit, j, count):
        if j > limit:
            return count

        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            return swap_pass(arr, limit, j+1, count + 1)

        return swap_pass(arr,limit, j+1, count)

    swap_count = swap_pass(arr, i, 0, 0)

    if swap_count == 0:
        return

    return recursiveBubbleSort(arr, i-1)

def recursiveBubbleSortDesc(arr, i):
    if i < 0:
        return

    def swap_pass(arr, limit, j, count):
        if j > limit:
            return count

        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            return swap_pass(arr, limit, j+1, count+1)
        return swap_pass(arr, limit, j+1, count)
    
    swap_count = swap_pass(arr, i, 0, 0)

    if swap_count == 0:
        return

    return recursiveBubbleSortDesc(arr, i-1)

def recursiveBubbleSortSingle(arr, i, j):
    if i < 0:
        return

    if j > i:
        return recursiveBubbleSortSingle(arr, i-1, 0)
    
    if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return recursiveBubbleSortSingle(arr, i, j+1)
    


arr1 = [5,7,8,4,1,6,9,2]
arr2 = [5,7,8,4,1,6,9,2]
arr3 = [5,7,8,4,1,6,9,2]
recursiveBubbleSort(arr1, len(arr1) - 2)
recursiveBubbleSortDesc(arr2, len(arr2) - 2)
recursiveBubbleSortSingle(arr3, len(arr3) - 2, 0)
print(arr1)
print(arr2)
print(arr3)