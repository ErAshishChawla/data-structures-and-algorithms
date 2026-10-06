def canFinish(piles:list[int], rate:int, available_hours:int) -> bool:
    total_hrs = 0

    for pile in piles:
        pile_hrs = pile//rate
        rem_pile = pile % rate

        if rem_pile !=0:
            pile_hrs += 1

        total_hrs += pile_hrs

        if total_hrs > available_hours:
            return False

    return True

def minEatingSpeed(piles:list[int], h:int):
    n = len(piles)

    if h < n:
        return -1

    max_pile = max(piles)
    res = max_pile

    if h == n:
        return res

    low = 1
    high = max_pile

    while low<=high:
        mid = (low + high) // 2

        if canFinish(piles, mid, h):
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res

print(minEatingSpeed([3,6,7,11], 8))
print(minEatingSpeed([30,11,23,4,20], 5))
print(minEatingSpeed([30,11,23,4,20], 6))