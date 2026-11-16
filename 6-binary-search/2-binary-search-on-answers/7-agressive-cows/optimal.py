def canPlaceCows(arr:list[int], cows:int, distance:int) -> bool:
    n = len(arr)

    remaining_cows = cows-1
    prev_idx = 0

    for i in range(1, n):
        if arr[i] - arr[prev_idx] >= distance:
            prev_idx = i
            remaining_cows -=1

        if remaining_cows ==0:
            break
    
    return remaining_cows == 0

def agressiveCows(arr:list[int], cows:int) -> int:
    n = len(arr)

    if cows > n:
        return -1

    arr.sort()

    low = 1
    high = arr[n-1] - arr[0]

    res = -1

    while low<=high:
        mid = (low + high) // 2

        if canPlaceCows(arr, cows, mid):
            res = mid
            low = mid + 1
        else:
            high = mid - 1

    return res

print(agressiveCows([1, 2, 4, 8, 9], 3))
print(agressiveCows([10, 1, 2, 7, 5],3))


