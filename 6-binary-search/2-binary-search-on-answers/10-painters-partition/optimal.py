def canPaint(arr:list[int], k: int, max_time: int) -> bool:
    curr_painter = 1
    curr_time = 0

    for time in arr:
        if time + curr_time > max_time:
            curr_painter += 1
            curr_time = time
        else:
            curr_time += time

        if curr_painter > k:
            break

    return curr_painter <= k

def minTime(arr:list[int], k:int) -> int:
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

        if canPaint(arr, k, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res