def canMakeSubarrays(arr:list[int], k:int, max_sum:int) -> bool:
    curr_subarray = 1
    curr_sum = 0

    for val in arr:
        if curr_sum + val > max_sum:
            curr_subarray += 1
            curr_sum = val
        else:
            curr_sum += val

        if curr_subarray > k:
            break

    return curr_subarray <= k

def splitArray(arr: list[int], k:int) -> int:
    n = len(arr)

    low = max(arr)
    high = sum(arr)
    res = -1

    if k > n:
        return res

    if k == 1:
        return high

    if k == n:
        return low

    while low <= high:
        mid = (low + high) // 2

        if canMakeSubarrays(arr, k, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res

print(splitArray([2,3,1,2,4,3], 5))