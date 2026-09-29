def upperBound(arr, target):
    n = len(arr)

    res = n 
    low = 0
    high = n-1

    while low<=high:
        mid = (low + high) // 2

        if arr[mid] > target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res