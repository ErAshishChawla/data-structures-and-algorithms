def isValidDivisor(arr:list[int], divisor:int, threshold:int) -> bool:
    total = 0

    for val in arr:
        quo = val // divisor
        rem = val % divisor

        if rem != 0:
            quo += 1

        total += quo

        if total > threshold:
            return False

    return True


def smallestDivisor(arr:list[int], threshold:int) -> int:
    low = 1
    high = max(arr)

    res = -1

    while low<=high:
        mid = (low + high) // 2

        if isValidDivisor(arr, mid, threshold):
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res
