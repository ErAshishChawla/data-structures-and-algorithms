def firstLast(arr: list[int], target:int):
    n = len(arr)

    low = 0
    high = n-1

    start = -1
    end = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            if arr[mid] == target:
                start = mid
            high = mid - 1
        else:
            low = mid + 1

    if start == -1:
        return -1,-1

    low = start
    high = n-1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid]<=target:
            if arr[mid] == target:
                end = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return start, end
