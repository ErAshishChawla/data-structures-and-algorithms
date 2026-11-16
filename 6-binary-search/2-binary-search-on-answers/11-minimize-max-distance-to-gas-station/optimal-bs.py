import math as m

def canPlace(arr:list[int], k:int, max_dist:float) -> bool:
    n = len(arr)
    needed = 0

    for i in range(1, n):
        gap = arr[i] - arr[i-1]
        curr_needed = m.ceil((gap / max_dist)) - 1
        needed += curr_needed

        if needed > k:
            break

    return needed <= k 


def minMaxDistance(arr:list[int], k: int):
    n = len(arr)
    max_dist = float("-Inf")
    for i in range(1, n):
        max_dist = max(max_dist, arr[i] - arr[i-1])
    
    low = 0
    high = max_dist
    res = high

    tolerance = 1e-7

    while high - low > tolerance:
        mid = (low + high) / 2

        if canPlace(arr, k, mid):
            res = mid
            high = mid
        else:
            low = mid

    return res

print(minMaxDistance([1, 13, 17, 23], 5))
print(minMaxDistance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
print(minMaxDistance([1, 2, 3, 4, 5], 2))