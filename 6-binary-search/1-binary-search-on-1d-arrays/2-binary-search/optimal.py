def binarySearch(arr:list[int], target:int) -> int:
    n = len(arr)

    low = 0
    high = n-1
    res = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            res = mid
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return res