def lowerBound(arr:list[int], target:int) -> int:
    n = len(arr)

    low = 0
    high = n - 1

    res = n

    while low <= high:
        mid = (low + high) // 2
    
        if arr[mid] >= target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
print(lowerBound(arr, 1))
print(lowerBound(arr, 12))
print(lowerBound(arr, 20))