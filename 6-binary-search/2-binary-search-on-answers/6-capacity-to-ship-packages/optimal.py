def canShip(weights:list[int], days:int, capacity:int):
    n = len(weights)

    curr_weight = 0
    curr_days = 1

    for i in range(0, n):
        weight = weights[i]

        if weight > capacity:
            return False

        curr_weight += weight

        if curr_weight > capacity:
            curr_weight = weight
            curr_days += 1

        if curr_days > days:
            return False

    return True

def shipWithinDays(weights:list[int], days:int) -> int:
    n = len(weights)

    low = max(weights)
    high = sum(weights)

    if days < 1:
        return -1

    if days == 1:
        return high

    res = -1

    while low <= high:
        mid = (low + high) // 2

        if canShip(weights, days, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res

print(shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
print(shipWithinDays([1,2,3,1,1], 4))

