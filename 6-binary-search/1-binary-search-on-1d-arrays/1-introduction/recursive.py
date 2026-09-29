def recursiveBinarySearch(arr:list[int], low:int, high:int, target:int) -> int:
    # Base Case
    if low > high:
        return -1

    # Recursion
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    
    elif arr[mid] < target:
        return recursiveBinarySearch(arr, mid + 1, high, target)

    else:
        return recursiveBinarySearch(arr, low, mid - 1, target) 

arr = [2, 4, 6, 7, 9, 11, 18, 19]
print(recursiveBinarySearch(arr, 0, len(arr) - 1, 6))
print(recursiveBinarySearch(arr, 0, len(arr) - 1, 13))

