def squareRoot(n:int) -> int:
    low = 1
    high = n

    res = -1

    while low<=high:
        mid = (low + high) // 2

        if mid**2 == n:
            res = mid
            break
        elif mid ** 2 < n:
            res = mid
            low = mid + 1
        else:
            high = mid - 1

    return res

print(squareRoot(11))