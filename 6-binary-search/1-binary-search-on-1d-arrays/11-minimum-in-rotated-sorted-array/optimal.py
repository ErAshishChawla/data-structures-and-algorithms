def findMin(arr:list[int]) -> int:
    n = len(arr)

    res = float("Inf")
    low = 0
    high = n -1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] < res:
            res = arr[mid]

        if arr[low] <= arr[mid]:
            if arr[mid] <=arr[high]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            high = mid - 1

    return res

arr = [4,5,6,7,0,1,2]
print(findMin(arr))
