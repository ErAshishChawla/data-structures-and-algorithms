def searchInsertPos(arr:list[int], x:int) -> int:
    n = len(arr)

    low = 0
    high = n - 1

    res = n

    while low<=high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res
