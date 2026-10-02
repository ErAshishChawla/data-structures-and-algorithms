def findMinIdx(arr:list[int]) -> int:
    n = len(arr)
    low = 0
    high = n-1

    min = float("Inf")
    min_idx = 0

    if arr[low] > arr[high]:
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < min:
                min = arr[mid]
                min_idx = mid
            
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return min_idx

def search(arr:list[int], target:int) -> int:
    n = len(arr)
    res = -1
    min_idx = findMinIdx(arr)

    low = min_idx
    high = n-1

    if min_idx != 0 and arr[0] <= target <= arr[min_idx-1]:
        low = 0
        high = min_idx-1

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

arr = [4,5,6,7,0,1,2]
print(search(arr, 0))
    