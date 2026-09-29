def binarySearch(arr: list[int], target: int) -> int:
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

arr = [2, 4, 6, 7, 9, 11, 18, 19]
print(binarySearch(arr, 6))
print(binarySearch(arr, 13))

