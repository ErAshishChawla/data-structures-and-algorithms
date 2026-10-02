def search(arr:list[int], target: int) -> int:
    n = len(arr)
    low = 0
    high = n-1
    res = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            res = mid
            break
        elif arr[mid] <= arr[high]:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return res

arr = [4,5,6,7,0,1,2]
print(search(arr, 0))


