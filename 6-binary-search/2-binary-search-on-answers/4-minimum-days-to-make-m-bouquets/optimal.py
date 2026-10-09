def canMakeBouquets(arr:list[int], m:int, k:int, day:int) -> bool:
    remaining_bouquets = m
    curr_flower_count = 0

    for bloom_day in arr:
        if bloom_day <= day:
            curr_flower_count += 1
            if curr_flower_count == k:
                remaining_bouquets -= 1
                curr_flower_count = 0
        else:
            curr_flower_count = 0

        if remaining_bouquets == 0:
            break

    return remaining_bouquets == 0


def minDays(arr:list[int], m:int, k:int) -> int:
    n = len(arr)
    flowers_req = m * k

    if flowers_req > n:
        return -1

    max_day = float("-Inf")
    min_day = float("Inf")

    for day in arr:
        max_day = max(max_day, day)
        min_day = min(min_day, day)

    if flowers_req == n:
        return max_day

    low = min_day
    high = max_day

    res = -1

    while low<=high:
        mid = (low + high) // 2

        if canMakeBouquets(arr, m, k, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res


print(minDays([1,10,3,10,2], 3, 1))
print(minDays([1,10,3,10,2], 3, 2))
print(minDays([7,7,7,7,12,7,7], 2, 3))