def partition(arr, low, high):
    pivot = arr[low]

    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i < high:
            i += 1

        while arr[j] > pivot and j > low:
            j -=1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[j], arr[low] = arr[low], arr[j]

    return j

def quickSort(arr, low, high):
    if low >= high:
        return
    
    pivot_idx = partition(arr, low, high)
    quickSort(arr, low, pivot_idx-1)
    quickSort(arr, pivot_idx+1, high)

arr = [1,6,3,7,2,3,1,9,1]
quickSort(arr, 0, len(arr)-1)
print(arr)